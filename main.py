import json
import time
from dotenv import load_dotenv

from tasks.repo_analysis_task import repo_analysis_task
from tasks.code_review_task import code_review_task
from tasks.security_scan_task import security_scan_task
from tasks.documentation_task import documentation_task
from tasks.issue_generation_task import issue_generation_task

load_dotenv()

CHECKPOINT_FILE = "checkpoint.json"


# -------------------------
# Default checkpoint state
# -------------------------
DEFAULT_CHECKPOINT = {
    "repo_url": "",
    "repo_analysis": False,
    "code_review": False,
    "security_scan": False,
    "documentation": False,
    "issue_generation": False
}


# -------------------------
# Load checkpoint safely
# -------------------------
def load_checkpoint():

    try:
        with open(CHECKPOINT_FILE, "r") as f:
            data = json.load(f)

        # Ensure all keys exist
        for key in DEFAULT_CHECKPOINT:
            if key not in data:
                data[key] = DEFAULT_CHECKPOINT[key]

        return data

    except FileNotFoundError:
        return DEFAULT_CHECKPOINT.copy()


# -------------------------
# Save checkpoint
# -------------------------
def save_checkpoint(data):
    with open(CHECKPOINT_FILE, "w") as f:
        json.dump(data, f, indent=2)


# -------------------------
# Reset checkpoint if new repo
# -------------------------
def reset_if_new_repo(repo_url, checkpoint):

    if checkpoint.get("repo_url") != repo_url:
        print("\n🔄 New repository detected. Resetting checkpoint...\n")

        checkpoint = DEFAULT_CHECKPOINT.copy()
        checkpoint["repo_url"] = repo_url

        save_checkpoint(checkpoint)

    return checkpoint


# -------------------------
# Run task safely
# -------------------------
def run_task(task_name, task, inputs, checkpoint):

    if checkpoint[task_name]:
        print(f"✔ Skipping {task_name} (already completed)")
        return

    while True:
        try:
            print(f"\n🚀 Running task: {task_name}")

            result = task.execute_sync(
                agent=task.agent,
                context=str(inputs)  # FIX: CrewAI requires string context
            )

            checkpoint[task_name] = True
            save_checkpoint(checkpoint)

            return result

        except Exception as e:

            print("\n⚠ Error:", e)
            print("⏳ Rate limit or API error. Waiting 30 seconds...\n")

            time.sleep(30)


# -------------------------
# Main
# -------------------------
def main():

    repo_url = input("Enter GitHub repository URL: ").strip()

    inputs = {"repo_url": repo_url}

    checkpoint = load_checkpoint()

    checkpoint = reset_if_new_repo(repo_url, checkpoint)

    # Task 1
    run_task(
        "repo_analysis",
        repo_analysis_task,
        inputs,
        checkpoint
    )

    # Task 2
    run_task(
        "code_review",
        code_review_task,
        inputs,
        checkpoint
    )

    # Task 3
    run_task(
        "security_scan",
        security_scan_task,
        inputs,
        checkpoint
    )

    # Task 4
    run_task(
        "documentation",
        documentation_task,
        inputs,
        checkpoint
    )

    # Task 5
    run_task(
        "issue_generation",
        issue_generation_task,
        inputs,
        checkpoint
    )

    print("\n🎉 All tasks completed successfully!")


if __name__ == "__main__":
    main()