import subprocess

def get_git_diff() -> str:
    try:
        diff = subprocess.check_output(["git", "diff"], text=True)
        return diff
    except subprocess.CalledProcessError as e:
        print(f"Error getting git diff: {e}")
        return ""
