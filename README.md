# mysh

**A lightweight, zero-dependency interactive REPL and batch Git workspace manager built from scratch in Python.**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-CLI%20Integration-F05032?style=flat&logo=git&logoColor=white)
![Dependencies](https://img.shields.io/badge/Dependencies-0%20(Stdlib)-success)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

---

## Overview

`mysh` is a custom terminal shell designed to simplify managing multiple local Git repositories.

Built entirely with Python's standard library, it combines an interactive REPL with recursive workspace discovery and batch Git command execution, allowing developers to inspect and manage multiple repositories from a single interface.

## Key Highlights

- **Zero Third-Party Dependencies:** Implemented exclusively using Python's built-in `os`, `sys`, and `subprocess` modules.
- **Command Dispatch Architecture:** Uses a dictionary-based dispatch table for clean command routing, with average O(1) command lookup.
- **Pruned Tree Traversal:** Uses `os.walk()` to recursively discover Git repositories while pruning internal `.git` directories.
- **Git CLI Integration:** Uses machine-readable Git output (`--porcelain`, `--show-current`) for working-tree status and branch detection.
- **Batch Execution:** Dispatches Git commands across all discovered repositories through a single command.
- **Native OS Fallback:** Delegates unrecognized commands to the host operating system.

---

## Built-In Commands

| Command | Arguments | Description |
| :--- | :--- | :--- |
| `repos` | None | Discovers repositories and displays their branch and working-tree status. |
| `gexec` | `<git_subcmd>` | Executes a Git command across every detected repository. |
| `cd` | `<path>` | Changes the current working directory. |
| `pwd` | None | Prints the current working directory. |
| `ls` | None | Lists items in the current directory. |
| `clear` | None | Clears the terminal screen. |
| `echo` | `[text]` | Prints text to standard output. |
| `help` | None | Displays the interactive command guide. |
| `exit` | None | Terminates the REPL session. |

---

## Quickstart

### Option 1: Standalone Executable (Windows)

No Python installation required.

1. Download `mysh.exe` from the [`dist`](dist/) directory.
2. Open PowerShell or Command Prompt in the downloaded file's directory.
3. Run:

```powershell
.\mysh.exe
```

**Requirement:** Git must be installed and accessible through the system `PATH`.

### Option 2: Run from Source

#### Prerequisites

- Python 3.10 or newer
- Git installed and accessible through the system `PATH`

Clone the repository and launch the script:

```bash
git clone https://github.com/AymenChebabhi/mysh.git
cd mysh
python mycli.py
```

---

## Usage Examples

Inspect discovered repositories:

```bash
repos
```

Execute a Git command across discovered repositories:

```bash
gexec status
```

Check the current branch across repositories:

```bash
gexec branch --show-current
```

---

## Technical Concepts Demonstrated

- Python REPL design and command parsing
- Dictionary-based command dispatch
- Recursive filesystem traversal and directory pruning
- Process management and subprocess communication
- Git command execution and machine-readable output parsing
- Cross-platform filesystem and terminal operations
- Standalone application packaging with PyInstaller

---

## Project Information

| Property | Details |
| :--- | :--- |
| Language | Python |
| Minimum Version | Python 3.10 |
| Dependencies | Python Standard Library only |
| Platforms | Windows, Linux, macOS (source) |
| Windows Distribution | Standalone executable |
| Packaging | PyInstaller |

---

**Author:** [Aymen Chebabhi](https://github.com/AymenChebabhi)

**Repository:** [github.com/AymenChebabhi/mysh](https://github.com/AymenChebabhi/mysh)