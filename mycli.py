import sys
import os
import subprocess

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
    target = " ".join(args)
    try:
        os.chdir(target)
    except Exception:
        print(f"Directory doesn't exist: {target}")
def cmd_repos(args):
    for root, dirs, files in os.walk("."):
        if ".git" in dirs:
            dirs.clear()
            status_result = subprocess.run(
                ["git", "status", "--porcelain"],
                cwd=root,
                capture_output=True,
                text=True
            )
            is_dirty = len(status_result.stdout.strip()) > 0
            branch_result = subprocess.run(
                ["git", "branch", "--show-current"],
                cwd=root,
                capture_output=True,
                text=True
            )
            branch_name = branch_result.stdout.strip()
            repo_name = os.path.basename(os.path.abspath(root))
            status_text = f"{YELLOW}Modified{RESET}" if is_dirty else f"{GREEN}Clean{RESET}"
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
    os.system("cls")
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
    print(' '.join(args))


COMMANDS = {
    "pwd": cmd_pwd,
    "ls": cmd_ls,
    "cd": cmd_cd,
    "repos": cmd_repos,
    "gexec": cmd_gexec,
    "clear": cmd_clear,
    "help": cmd_help,
    "echo": cmd_echo
}


while True:
    while True:
        try:
            user_input = input(f"{os.getcwd()} mysh> ")
        except (KeyboardInterrupt, EOFError):
            print()
            continue
    parts = user_input.split()
    if not parts:
        continue

    cmd_name = parts[0].lower()
    args = parts[1:]

    if cmd_name == "exit":
        break
    elif cmd_name in COMMANDS:
        # Look up the function in the dictionary and call it with args!
        COMMANDS[cmd_name](args)
    else:
        try:
            subprocess.run(parts)
        except FileNotFoundError:
            print(f"Command not found: {cmd_name}")

