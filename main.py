from git_operations import get_git_diff
from ai_commit import generate_commit_message

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
