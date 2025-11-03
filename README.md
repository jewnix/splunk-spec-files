# Splunk Spec Files

This repository tracks Splunk default configuration and specification files across different versions of Splunk Enterprise. The `.spec` files define the configuration options and syntax for various Splunk components and features, and the `.conf` files contain the default values for each option.

## What's in this repository

This repository contains three types of files:

### 1. Configuration Specification Files (`.spec`)

These files define the configuration options, syntax, and documentation for Splunk settings. They contain:
- Available configuration parameters
- Valid value types and ranges
- Detailed descriptions and usage notes
- Default values (when applicable)

Examples:
- `authentication.conf.spec` - Authentication and authorization settings
- `inputs.conf.spec` - Data input configurations
- `indexes.conf.spec` - Index and storage settings
- `limits.conf.spec` - Search and indexing limits
- `server.conf.spec` - Server and deployment settings
- `transforms.conf.spec`, `props.conf.spec` - Data transformation rules
- And many more

### 2. Default Configuration Files (`.conf`)

These files contain the actual default values shipped with Splunk Enterprise. They complement the `.spec` files by showing:
- Factory defaults for each setting
- Example configurations
- Working baseline configurations

When comparing versions, these files show how Splunk's out-of-the-box behavior has changed.

### 3. CLI Command Reference (`splunkrc_cmds.xml`)

This XML file defines the Splunk command-line interface structure, including:
- Available CLI commands and verbs (add, edit, list, show, enable, etc.)
- Command syntax and parameters
- Help text for each command
- URI mappings for REST API endpoints
- Argument mappings between CLI and API

This file is useful for tracking changes to the `splunk` CLI tool across versions.

---

Each version of Splunk is tagged in this repository, making it easy to track changes across releases.

## Available Versions

This repository tracks Splunk versions from **6.5.0** to **10.0.1**. You can see all available versions with:

```bash
git tag --list
```

## Comparing Configuration Changes Between Versions

### Method 1: Command Line (using git)

#### Compare two specific versions

To see what changed between two Splunk versions:

```bash
git diff <older-version> <newer-version>
```

Example - see all changes between Splunk 9.0.0 and 10.0.0:
```bash
git diff 9.0.0 10.0.0
```

#### Compare a specific file between versions

To see changes in a particular configuration file:

```bash
git diff <older-version> <newer-version> -- <filename>
```

Example - see changes in `indexes.conf.spec` between versions 9.0.0 and 10.0.0:
```bash
git diff 9.0.0 10.0.0 -- indexes.conf.spec
```

#### View file contents at a specific version

To see what a file looked like at a specific version:

```bash
git show <version>:<filename>
```

Example - view `server.conf.spec` as it was in version 9.0.0:
```bash
git show 9.0.0:server.conf.spec
```

#### Compare current working directory to a version

To see what's changed since a specific version:

```bash
git diff <version>
```

Example:
```bash
git diff 10.0.0
```

### Method 2: GitHub Website

#### Compare two versions using GitHub's compare view

1. Navigate to the repository on GitHub
2. Use the compare URL pattern:
   ```
   https://github.com/jewnix/splunk-spec-files/compare/<older-version>...<newer-version>
   ```

   For example, to compare version 9.0.0 to 10.0.0:
   ```
   https://github.com/jewnix/splunk-spec-files/compare/9.0.0...10.0.0
   ```

3. The page will show:
   - All commits between the two versions
   - Files changed
   - Line-by-line differences

## Common Use Cases

### Find what configuration options were added in a new version

```bash
git diff 9.4.3 10.0.0 --stat
```

This shows a summary of which files changed and how many lines were added/removed.

### Filter out noise when comparing versions

When comparing versions, you often want to ignore version number changes and log file references. Use the `-I` flag to ignore lines matching patterns:

```bash
git diff 9.4.3 10.0.0 -I"Version " -Iscripts/logs -- *spec
```

This filters out:
- Lines containing "Version " (which change in every release)
- Lines containing "scripts/logs" (log file path references)
- Only compares `.spec` files

Add `--stat` to get a summary:
```bash
git diff 9.4.3 10.0.0 -I"Version " -Iscripts/logs -- *spec --stat
```

### Get a clean summary of what changed

**Numeric statistics** - see exact line counts:
```bash
git diff 9.4.3 10.0.0 --numstat -- *spec
```
Output format: `<lines-added> <lines-removed> <filename>`

**Summary statistics** - quick overview:
```bash
git diff 9.4.3 10.0.0 --shortstat -- *spec
```
Output: `X files changed, Y insertions(+), Z deletions(-)`

**Show which files changed** - names only:
```bash
git diff 9.4.3 10.0.0 --name-only -- *spec
```

**Show status of each file** - Added, Modified, Deleted:
```bash
git diff 9.4.3 10.0.0 --name-status -- *spec
```

### Find new or removed files between versions

**Show only newly added files:**
```bash
git diff 9.4.3 10.0.0 --diff-filter=A --name-only -- *spec
```

**Show only deleted files:**
```bash
git diff 9.4.3 10.0.0 --diff-filter=D --name-only -- *spec
```

**Show only modified files (no additions or deletions):**
```bash
git diff 9.4.3 10.0.0 --diff-filter=M --name-only -- *spec
```

### View differences with better formatting

**Show stanzas with their changes**:
```bash
git diff 9.4.3 10.0.0 -U100 -- server.conf.spec | grep -E '^ \[.*\]$|^[-+][^-+]'
```
This shows each `[stanza]` header followed by only the changed lines within that stanza, filtering out all the unchanged content. Very clean and easy to read.

**Compact summary with change counts:**
```bash
git diff 9.4.3 10.0.0 --compact-summary -- *spec
```

### Search for specific configuration changes

**Find when a specific setting was added or removed:**
```bash
git log -S "setting_name" --source --all -- *spec
```

**Find commits that changed a specific setting:**
```bash
git log -G "setting_name.*=" --oneline -- server.conf.spec
```

**Check if a specific setting exists in a version:**
```bash
git show 9.0.0:server.conf.spec | grep "setting_name"
```

### Compare only specific files

**Compare a single file between versions:**
```bash
git diff 9.4.3 10.0.0 -- indexes.conf.spec
```

**Compare multiple specific files:**
```bash
git diff 9.4.3 10.0.0 -- indexes.conf.spec inputs.conf.spec outputs.conf.spec
```

**Show only added lines in a file** (useful for finding new features):
```bash
git diff 9.4.3 10.0.0 -- indexes.conf.spec | grep "^+"
```

**Show only removed lines in a file:**
```bash
git diff 9.4.3 10.0.0 -- indexes.conf.spec | grep "^-"
```

**Note:** All of these commands work for `.conf` files as well - just change the filename (e.g., `server.conf` instead of `server.conf.spec`).

### Track CLI command changes

**Compare CLI command definitions:**
```bash
git diff 9.4.3 10.0.0 -- splunkrc_cmds.xml
```

**See what CLI commands were added or removed:**
```bash
git diff 9.4.3 10.0.0 -- splunkrc_cmds.xml | grep -E "^\+.*<item obj=|^\-.*<item obj="
```

**Check if a specific CLI command exists in a version:**
```bash
git show 9.0.0:splunkrc_cmds.xml | grep 'obj="command_name"'
```

### Advanced comparisons

**Compare across multiple versions** - see the evolution of a file:
```bash
git log -p 9.0.0..10.0.0 -- server.conf.spec
```
This shows all changes to the file across all commits between versions.

**Find files with the most changes:**
```bash
git diff 9.4.3 10.0.0 --stat -- *spec | sort -k2 -n -r | head -10
```

## Quick Reference: Most Useful Commands

Here are the commands you'll likely use most often:

```bash
# Clean diff ignoring version numbers and noise
git diff 9.4.3 10.0.0 -I"Version " -Iscripts/logs -- *spec

# Summary of changes
git diff 9.4.3 10.0.0 --shortstat -- *spec

# List all changed files
git diff 9.4.3 10.0.0 --name-status -- *spec

# Detailed stats per file
git diff 9.4.3 10.0.0 --numstat -- *spec

# Find new files
git diff 9.4.3 10.0.0 --diff-filter=A --name-only -- *spec

# Word-level diff for a specific file
git diff 9.4.3 10.0.0 --color-words -- server.conf.spec

# Search for when a setting was introduced
git log -S "setting_name" --all -- *spec

# Find all occurrences of a setting in a version
git grep "setting_name" 9.0.0 -- "*spec"
```
