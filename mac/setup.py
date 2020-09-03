import subprocess
import sys

if len(sys.argv) > 3: print("Faulty arguments, please enter message"); exit();
else: message = sys.argv[1];
if len(message) < 3: print("Please enter valid commit message"); exit();

push = False
if len(sys.argv) == 3: push = True;


subprocess.run(["git", "add", "."])
git_status = subprocess.run(["git", "status"])
git_commit = subprocess.run(["git", "commit", "-m", message])

if push: git_push = subprocess.run(["git", "push"])

print(git_status.git_push)
