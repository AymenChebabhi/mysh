\# mysh — Lightweight Multi-Repository Management Shell



A modular interactive shell built from first principles in pure Python (zero external dependencies). Designed to streamline batch operations and working-tree monitoring across nested Git repositories.



\---



\## Features



\- \*\*Interactive REPL:\*\* Built-in command prompt dynamically tracking the Current Working Directory (CWD).

\- \*\*Dispatch Table Architecture:\*\* Modular, O(1) command lookup eliminating nested condition branching.

\- \*\*Recursive Repo Discovery (`repos`):\*\* Pruned depth-first filesystem traversal via `os.walk` to identify nested repositories without scanning `.git` internals.

\- \*\*Plumbing-Level Status Checks:\*\* Queries Git using machine-readable porcelain flags (`git status --porcelain`, `git branch --show-current`) with ANSI color-coded status reporting.

\- \*\*Batch Git Execution (`gexec`):\*\* Dispatches arbitrary Git commands across all detected repositories simultaneously.

\- \*\*Native OS Fallback:\*\* Unrecognized commands are delegated directly to the host operating system subprocess runner.



\---



\## Built-In Commands



| Command | Arguments | Description |

|---|---|---|

| `repos` | None | Recursively scans for Git repos and prints branch \& clean/dirty state |

| `gexec` | `<git\_subcmd>` | Runs a Git command (e.g. `gexec pull`, `gexec fetch -p`) in all repos |

| `cd` | `<path>` | Changes working directory (supports paths with spaces) |

| `pwd` | None | Displays current working directory |

| `ls` | None | Lists directory contents |

| `clear` | None | Clears the terminal screen |

| `echo` | `\[text]` | Prints arguments to the terminal |

| `help` | None | Displays the interactive command menu |

| `exit` | None | Closes the shell |



\---



\## Getting Started



\### Prerequisites

\- Python 3.10+

\- Git installed and available in system `PATH`



\### Running the Shell

```bash

python mycli.py

