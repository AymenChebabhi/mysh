import os
import shlex
import subprocess
import sys

# Enable ANSI escape sequence processing on Windows consoles
os.system("")
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"


def cmd_pwd(args):
  print(os.getcwd())


def cmd_ls(args):
  for item in os.listdir():
    print(item)


def cmd_cd(args):
  if not args:
    print("Enter a directory!")
    return
  target = args[0]
  try:
    os.chdir(target)
  except OSError as e:
    print(f"cd: {e.strerror}: {target}")


def cmd_repos(args):
  for root, dirs, files in os.walk("."):
    if ".git" in dirs:
      dirs.clear()
      status_result = subprocess.run(
          ["git", "status", "--porcelain"],
          cwd=root,
          capture_output=True,
          text=True,
      )
      is_dirty = len(status_result.stdout.strip()) > 0
      branch_result = subprocess.run(
          ["git", "branch", "--show-current"],
          cwd=root,
          capture_output=True,
          text=True,
      )
      branch_name = branch_result.stdout.strip() or "DETACHED"
      repo_name = os.path.basename(os.path.abspath(root))
      status_text = (
          f"{YELLOW}Modified{RESET}" if is_dirty else f"{GREEN}Clean{RESET}"
      )
      print(f"[{repo_name}] ({CYAN}{branch_name}{RESET}) -> {status_text}")


def cmd_gexec(args):
  if not args:
    print("Specify a git command to run (e.g., gexec status)")
    return
  for root, dirs, files in os.walk("."):
    if ".git" in dirs:
      dirs.clear()
      repo_name = os.path.basename(os.path.abspath(root))
      print(f"Running git {' '.join(args)} in {repo_name}...")
      subprocess.run(["git"] + args, cwd=root)


def cmd_clear(args):
  os.system("cls" if os.name == "nt" else "clear")


def cmd_help(args):
  print(f"""{CYAN}exit{RESET}: exits the shell
{CYAN}help{RESET}: lists the commands
{CYAN}echo{RESET}: prints arguments
{CYAN}pwd{RESET}: prints current working directory
{CYAN}ls{RESET}: prints every item in the current working directory
{CYAN}clear{RESET}: wipes the terminal screen
{CYAN}cd{RESET}: changes the current working directory into an existing one
{CYAN}repos{RESET}: checks the status of Repos
{CYAN}gexec{RESET}: run git command across every Repo""")


def cmd_echo(args):
  print(" ".join(args))


COMMANDS = {
    "pwd": cmd_pwd,
    "ls": cmd_ls,
    "cd": cmd_cd,
    "repos": cmd_repos,
    "gexec": cmd_gexec,
    "clear": cmd_clear,
    "help": cmd_help,
    "echo": cmd_echo,
}


def main():
  while True:
    try:
      user_input = input(f"{os.getcwd()} mysh> ")
    except (KeyboardInterrupt, EOFError):
      print()
      continue

    try:
      parts = shlex.split(user_input)
    except ValueError as err:
      print(f"Syntax error: {err}")
      continue

    if not parts:
      continue

    cmd_name = parts[0].lower()
    args = parts[1:]

    if cmd_name == "exit":
      break
    elif cmd_name in COMMANDS:
      COMMANDS[cmd_name](args)
    else:
      try:
        subprocess.run(parts)
      except FileNotFoundError:
        print(f"Command not found: {cmd_name}")


if __name__ == "__main__":
  main()