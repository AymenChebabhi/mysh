# mysh

**A lightweight, zero-dependency interactive REPL and batch Git workspace manager built from scratch in Python.**

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=flat&logo=python&logoColor=white)
![Git](https://img.shields.io/badge/Git-Plumbing%20API-F05032?style=flat&logo=git&logoColor=white)
![Dependencies](https://img.shields.io/badge/Dependencies-0%20(Standard%20Lib)-success)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-lightgrey)

---

## Overview

`mysh` is a custom terminal shell designed to eliminate the overhead of managing dozens of scattered local repositories. Built purely using standard-library primitives, it acts as an interactive REPL with built-in recursive workspace discovery and batch execution capabilities.

### Key Highlights
- **Zero Third-Party Dependencies:** Powered strictly by Python's built-in `os`, `sys`, and `subprocess` modules.
- **$O(1)$ Command Dispatch Table:** Decoupled execution architecture eliminating messy conditional chains.
- **Pruned Tree Traversal:** Recursive directory scanner (`os.walk`) engineered to detect `.git` roots while pruning internal trees to optimize scan performance.
- **Git Porcelain Interception:** Communicates directly with machine-readable Git output streams (`--porcelain`, `--show-current`) for consistent parsing.
- **Native OS Fallback:** Transparently delegates non-internal commands to the host operating system.

---

## Built-In Commands

| Command | Arguments | Description |
| :--- | :--- | :--- |
| `repos` | None | Recursively scans for repositories and displays branch name and clean/dirty status. |
| `gexec` | `<git_subcmd>` | Dispatches an arbitrary Git command across every detected repository. |
| `cd` | `<path>` | Changes working directory (natively supports paths with spaces). |
| `pwd` | None | Prints the current working directory path. |
| `ls` | None | Lists items within the current working directory. |
| `clear` | None | Wipes the terminal screen buffer. |
| `echo` | `[text]` | Prints input strings to stdout. |
| `help` | None | Displays the interactive command guide. |
| `exit` | None | Terminates the REPL session cleanly. |

---

## Quickstart

### Prerequisites
- Python 3.10 or newer
- Git installed and accessible via system `PATH`

### Running Locally
Clone the repository and launch the script directly:

```bash
git clone [https://github.com/AymenChebabhi/mysh.git](https://github.com/AymenChebabhi/mysh.git)
cd mysh
python mycli.py
