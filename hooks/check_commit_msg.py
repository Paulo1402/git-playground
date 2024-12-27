import sys
import subprocess


def get_current_branch_name():
    result = subprocess.run(
        ["git", "rev-parse", "--abbrev-ref", "HEAD"], capture_output=True, text=True
    )
    return result.stdout.strip()


def main():
    commit_msg_filepath = sys.argv[1]

    with open(commit_msg_filepath, "r") as file:
        commit_msg = file.read().strip()

    branch_name = get_current_branch_name()

    if branch_name.startswith("feature/") or branch_name.startswith("bugfix/"):
        task_id = branch_name.split("/")[1]
        commit_msg += f"\nRelated to {task_id}"

        with open(commit_msg_filepath, "w") as file:
            file.write(commit_msg)

    return 0


if __name__ == "__main__":
    sys.exit(main())
