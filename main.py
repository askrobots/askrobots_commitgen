import sys
import subprocess
from git_operations import get_git_diff
from ai_commit import generate_commit_message

def commit_changes(commit_message):
    try:
        subprocess.run(["git", "commit", "-m", commit_message], check=True)
        print(f"Changes committed with message: {commit_message}")
    except subprocess.CalledProcessError as e:
        print(f"Error during git commit: {e}")
        return

def main():
    # Check if only displaying the message or also committing
    only_show_message = "--show-only" in sys.argv

    diff = get_git_diff()
    if not diff:
        print("No changes detected.")
        return

    commit_message = generate_commit_message(diff)
    if commit_message:
        if only_show_message:
            print("Generated commit message:")
            print(commit_message)
        else:
            commit_changes(commit_message)
    else:
        print("Failed to generate a commit message.")

if __name__ == "__main__":
    main()
