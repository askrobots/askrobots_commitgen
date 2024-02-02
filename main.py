from git_helper import get_git_diff
from commit_generator import generate_commit_message

def main():
    diff = get_git_diff()
    if not diff:
        print("No changes detected.")
        return

    commit_message = generate_commit_message(diff)
    if commit_message:
        print("Generated commit message:")
        print(commit_message)
    else:
        print("Failed to generate a commit message.")

if __name__ == "__main__":
    main()
