import subprocess

def get_git_diff() -> str:
    try:
        # Using --cached to get the diff of staged changes
        diff = subprocess.check_output(["git", "diff", "--cached"], text=True)
        return diff
    except subprocess.CalledProcessError as e:
        print(f"Error getting git diff: {e}")
        return ""
