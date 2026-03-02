#!/usr/bin/env python

def git_init():
    import subprocess
    import os
    
    # Check if already a git repository
    if os.path.exists('.git') or os.path.isdir('.git'):
        print("Already a git repository. Skipping git initialization.")
        return
    
    try:
        subprocess.run(["git", "init", "-b", "main"], check=True)
        subprocess.run(["git", "add", "--all"], check=True)
        subprocess.run(["git", "commit", "-m", "Initial commit"], check=True)
        print("Initialized a new git repository.")
    except Exception as e:
        print(f"Git initialization failed: {e}")

if __name__ == "__main__":
    git_init() 