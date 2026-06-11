[CmdletBinding()]
param(
  [string]$Message = "",
  [string]$Remote = "origin",
  [string]$Branch = "",
  [switch]$NoPush,
  [switch]$SkipChecks
)

$ErrorActionPreference = "Stop"
$OutputEncoding = [Console]::OutputEncoding = [System.Text.Encoding]::UTF8
$env:PYTHONIOENCODING = "utf-8"

function Write-Section {
  param([string]$Text)
  Write-Host ""
  Write-Host "== $Text =="
}

function Invoke-Native {
  param(
    [string]$Label,
    [string]$FilePath,
    [string[]]$Arguments
  )

  Write-Host "-> $Label"
  & $FilePath @Arguments
  if ($LASTEXITCODE -ne 0) {
    throw "$Label failed with exit code $LASTEXITCODE"
  }
}

function Get-NativeOutput {
  param(
    [string]$FilePath,
    [string[]]$Arguments
  )

  $output = & $FilePath @Arguments
  if ($LASTEXITCODE -ne 0) {
    throw "$FilePath $($Arguments -join ' ') failed with exit code $LASTEXITCODE"
  }
  if ($null -eq $output) {
    return @()
  }
  return $output
}

function Resolve-WikiPython {
  if ($env:WIKI_PYTHON -and (Test-Path -LiteralPath $env:WIKI_PYTHON)) {
    return $env:WIKI_PYTHON
  }

  $bundled = Join-Path $env:USERPROFILE ".cache\codex-runtimes\codex-primary-runtime\dependencies\python\python.exe"
  if (Test-Path -LiteralPath $bundled) {
    return $bundled
  }

  $python = Get-Command python -ErrorAction SilentlyContinue
  if ($python) {
    return $python.Source
  }

  throw "Python was not found. Set WIKI_PYTHON to a Python executable and retry."
}

function Format-ListBlock {
  param([string[]]$Lines)

  if (-not $Lines -or $Lines.Count -eq 0) {
    return @("- none")
  }

  return $Lines | ForEach-Object { "- $_" }
}

$repoRoot = (Get-NativeOutput git @("rev-parse", "--show-toplevel") | Select-Object -First 1).Trim()
Set-Location -LiteralPath $repoRoot

if ([string]::IsNullOrWhiteSpace($Branch)) {
  $Branch = (Get-NativeOutput git @("branch", "--show-current") | Select-Object -First 1).Trim()
}
if ([string]::IsNullOrWhiteSpace($Branch)) {
  throw "Cannot publish from a detached HEAD. Check out a branch first."
}

$timestamp = [DateTimeOffset]::Now.ToString("yyyy-MM-dd HH:mm:ss zzz")
$subjectTime = [DateTimeOffset]::Now.ToString("yyyy-MM-dd HH:mm")
$pythonExe = Resolve-WikiPython

Write-Section "Wiki Git Snapshot"
Write-Host "Repo:   $repoRoot"
Write-Host "Branch: $Branch"
Write-Host "Remote: $Remote"
Write-Host "Time:   $timestamp"
Write-Host "Python: $pythonExe"

$conflicts = @(Get-NativeOutput git @("diff", "--name-only", "--diff-filter=U"))
if ($conflicts.Count -gt 0) {
  throw "Unmerged files exist. Resolve conflicts before publishing:`n$($conflicts -join "`n")"
}

$checks = @(
  @{ Label = "curation status"; Args = @("tools/wiki/curation_status.py", "--dupes") },
  @{ Label = "corpus counts"; Args = @("tools/wiki/corpus_counts.py") },
  @{ Label = "frontmatter audit"; Args = @("tools/wiki/frontmatter_audit.py") },
  @{ Label = "index audit"; Args = @("tools/wiki/index_audit.py") },
  @{ Label = "link check"; Args = @("tools/wiki/linkcheck.py", "--orphans") },
  @{ Label = "process narration audit"; Args = @("tools/wiki/process_refs.py") },
  @{ Label = "language audit"; Args = @("tools/wiki/language_audit.py") }
)

if (Test-Path -LiteralPath "wiki/references/reference-database.json") {
  $checks += @{ Label = "reference database audit"; Args = @("tools/wiki/verify_refdb.py") }
}

if (-not $SkipChecks) {
  Write-Section "Validation"
  foreach ($check in $checks) {
    Invoke-Native $check.Label $pythonExe $check.Args
  }
} else {
  Write-Host "Skipping validation because -SkipChecks was provided."
}

Write-Section "Stage Changes"
$statusBefore = @(Get-NativeOutput git @("status", "--short"))
Write-Host "Working tree before staging:"
Format-ListBlock $statusBefore | ForEach-Object { Write-Host $_ }

Invoke-Native "git add -A" git @("add", "-A")
$staged = @(Get-NativeOutput git @("diff", "--cached", "--name-status"))

if ($staged.Count -eq 0) {
  Write-Host "No tracked changes to commit after staging."
  if (-not $NoPush) {
    Write-Section "Push"
    try {
      $upstream = (Get-NativeOutput git @("rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}") | Select-Object -First 1).Trim()
    } catch {
      $upstream = ""
    }

    if ($upstream) {
      Invoke-Native "git push" git @("push")
    } else {
      Invoke-Native "git push -u $Remote $Branch" git @("push", "-u", $Remote, $Branch)
    }
  }
  exit 0
}

Write-Host "Staged changes:"
Format-ListBlock $staged | ForEach-Object { Write-Host $_ }

if ([string]::IsNullOrWhiteSpace($Message)) {
  $subject = "wiki snapshot: $subjectTime"
} else {
  $subject = "${Message}: $subjectTime"
}

$checkNames = if ($SkipChecks) {
  @("validation skipped by -SkipChecks")
} else {
  $checks | ForEach-Object { $_.Label }
}

$listedChanges = $staged | Select-Object -First 50
$remaining = $staged.Count - $listedChanges.Count
$changeLines = @($listedChanges | ForEach-Object { "- $_" })
if ($remaining -gt 0) {
  $changeLines += "- ... and $remaining more"
}

$messageLines = @(
  $subject,
  "",
  "Automated wiki snapshot.",
  "",
  "Snapshot time: $timestamp",
  "Repo: $repoRoot",
  "Branch: $Branch",
  "Remote: $Remote",
  "",
  "Checks:"
) + ($checkNames | ForEach-Object { "- $_" }) + @(
  "",
  "Changed files:"
) + $changeLines

New-Item -ItemType Directory -Force -Path ".curation-out" | Out-Null
$messagePath = Join-Path ".curation-out" "git-snapshot-commit-message.txt"
Set-Content -LiteralPath $messagePath -Value $messageLines -Encoding UTF8

Write-Section "Commit"
Invoke-Native "git commit" git @("commit", "-F", $messagePath)
$commit = (Get-NativeOutput git @("rev-parse", "--short", "HEAD") | Select-Object -First 1).Trim()
Write-Host "Commit created: $commit"

if (-not $NoPush) {
  Write-Section "Push"
  try {
    $upstream = (Get-NativeOutput git @("rev-parse", "--abbrev-ref", "--symbolic-full-name", "@{u}") | Select-Object -First 1).Trim()
  } catch {
    $upstream = ""
  }

  if ($upstream) {
    Invoke-Native "git push" git @("push")
  } else {
    Invoke-Native "git push -u $Remote $Branch" git @("push", "-u", $Remote, $Branch)
  }
} else {
  Write-Host "Push skipped because -NoPush was provided."
}

Write-Section "Done"
Write-Host "Published snapshot: $commit"
