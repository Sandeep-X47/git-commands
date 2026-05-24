# Complete Git & GitHub Commands Handbook 🚀

## Repository Example Used Throughout

* **GitHub Repository Name:** `git-commands`
* **Project Directory Name:** `git-practice`

---

# 1. Configure Git (First Time Setup)

```bash
git config --global user.name "someone"
git config --global user.email "someone@example.com"
```

Check configuration:

```bash
git config --list
```

---

# 2. Create Project Directory

```bash
mkdir ai-assistant-project
cd ai-assistant-project
```

Check current directory:

```bash
pwd
```

List files:

```bash
ls
```

Windows:

```bash
dir
```

---

# 3. Initialize Git Repository

```bash
git init
```

Check repository status:

```bash
git status
```

---

# 4. Create Files

Linux / macOS:

```bash
touch app.py
touch README.md
```

Windows:

```bash
type nul > app.py
type nul > README.md
```

Example Python code:

```python
# app.py

print("AI Assistant Started")
```

---

# 5. Stage Files

Add one file:

```bash
git add app.py
```

Add multiple files:

```bash
git add app.py README.md
```

Add all files:

```bash
git add .
```

Check status:

```bash
git status
```

---

# 6. Commit Changes

```bash
git commit -m "Initial project setup"
```

Another example:

```bash
git commit -m "Added AI startup message"
```

View commit history:

```bash
git log
```

Compact commit history:

```bash
git log --oneline
```

---

# 7. Connect Local Repository to GitHub

Create repository on GitHub:

* Repository Name: `AI-Assistant`

Connect remote repository:

```bash
git remote add origin https://github.com/yourusername/AI-Assistant.git
```

Check remotes:

```bash
git remote -v
```

---

# 8. Push Code to GitHub

Rename branch:

```bash
git branch -M main
```

First push:

```bash
git push -u origin main
```

Future pushes:

```bash
git push
```

---

# 9. Clone Existing Repository

```bash
git clone https://github.com/yourusername/AI-Assistant.git
```

Clone into custom directory:

```bash
git clone https://github.com/yourusername/AI-Assistant.git my-project
```

Move into project:

```bash
cd my-project
```

---

# 10. Pull Latest Changes

```bash
git pull origin main
```

Short version:

```bash
git pull
```

---

# 11. Fetch Changes Only

```bash
git fetch
```

---

# 12. Branch Commands

Create branch:

```bash
git branch feature-login
```

View branches:

```bash
git branch
```

Switch branch:

```bash
git checkout feature-login
```

Modern command:

```bash
git switch feature-login
```

Create and switch:

```bash
git checkout -b feature-dashboard
```

Modern version:

```bash
git switch -c feature-dashboard
```

---

# 13. Merge Branch

Switch to main:

```bash
git checkout main
```

Merge feature branch:

```bash
git merge feature-dashboard
```

---

# 14. Delete Branch

Delete local branch:

```bash
git branch -d feature-dashboard
```

Force delete:

```bash
git branch -D feature-dashboard
```

Delete remote branch:

```bash
git push origin --delete feature-dashboard
```

---

# 15. Check Differences

Unstaged changes:

```bash
git diff
```

Staged changes:

```bash
git diff --staged
```

Compare branches:

```bash
git diff main feature-login
```

---

# 16. Undo Changes

Discard file changes:

```bash
git checkout -- app.py
```

Modern version:

```bash
git restore app.py
```

Unstage file:

```bash
git restore --staged app.py
```

Undo last commit but keep changes:

```bash
git reset --soft HEAD~1
```

Undo last commit and remove changes:

```bash
git reset --hard HEAD~1
```

---

# 17. Remove Files

```bash
git rm app.py
```

Commit removal:

```bash
git commit -m "Removed app.py"
```

---

# 18. Rename File

```bash
git mv old.py new.py
```

---

# 19. Stash Changes

Save temporary changes:

```bash
git stash
```

View stashes:

```bash
git stash list
```

Restore stash:

```bash
git stash apply
```

Apply and remove stash:

```bash
git stash pop
```

Delete stash:

```bash
git stash drop
```

---

# 20. View Commit Details

```bash
git show
```

Specific commit:

```bash
git show commit_id
```

---

# 21. Revert Commit

```bash
git revert commit_id
```

---

# 22. Tags (Version Releases)

Create tag:

```bash
git tag v1.0
```

Push tag:

```bash
git push origin v1.0
```

View tags:

```bash
git tag
```

---

# 23. Git Ignore

Create `.gitignore`:

```bash
touch .gitignore
```

Example `.gitignore` content:

```txt
__pycache__/
.env
node_modules/
*.log
```

---

# 24. Full Real Workflow Example

## Step 1 — Create Project

```bash
mkdir ai-assistant-project
cd ai-assistant-project
git init
```

## Step 2 — Create Files

```bash
touch app.py README.md
```

## Step 3 — Add Python Code

```python
print("AI Assistant Running")
```

## Step 4 — Stage and Commit

```bash
git add .
git commit -m "Initial commit"
```

## Step 5 — Connect GitHub Repository

```bash
git remote add origin https://github.com/yourusername/AI-Assistant.git
```

## Step 6 — Push Code

```bash
git branch -M main
git push -u origin main
```

## Step 7 — Create Feature Branch

```bash
git checkout -b feature-auth
```

## Step 8 — Modify Code

```python
print("Authentication Added")
```

## Step 9 — Commit Feature

```bash
git add .
git commit -m "Added authentication feature"
```

## Step 10 — Merge Feature

```bash
git checkout main
git merge feature-auth
```

## Step 11 — Push Updated Code

```bash
git push
```

---

# 25. GitHub Authentication

GitHub no longer supports password authentication for Git operations.

Use:

* Personal Access Token (PAT)
* SSH Keys

## Generate SSH Key

```bash
ssh-keygen -t ed25519 -C "sandeep@example.com"
```

Start SSH agent:

```bash
eval "$(ssh-agent -s)"
```

Add SSH key:

```bash
ssh-add ~/.ssh/id_ed25519
```

Copy public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

Add it to:

GitHub → Settings → SSH and GPG Keys

Test SSH connection:

```bash
ssh -T git@github.com
```

Clone using SSH:

```bash
git clone git@github.com:yourusername/AI-Assistant.git
```

---

# 26. Advanced Commands

See remote information:

```bash
git remote show origin
```

Cherry-pick commit:

```bash
git cherry-pick commit_id
```

Rebase branch:

```bash
git rebase main
```

Interactive rebase:

```bash
git rebase -i HEAD~3
```

Remove untracked files:

```bash
git clean -f
```

See all branches:

```bash
git branch -a
```

See current branch:

```bash
git branch --show-current
```

---

# 27. Git Internals You Should Understand

## git add

Moves changes into the staging area.

## git commit

Creates a snapshot of staged changes.

## git push

Uploads commits to GitHub.

## git pull

Downloads and merges remote changes.

## git fetch

Downloads changes without merging.

## git merge

Combines histories.

## git rebase

Rewrites history into a cleaner linear sequence.

---

# 28. Most Common Professional Workflow

```bash
git pull
git checkout -b feature-x

# Make code changes

git add .
git commit -m "Implemented feature x"

git push origin feature-x
```

Then:

1. Open Pull Request on GitHub
2. Code Review
3. Merge

---

# 29. Dangerous Commands

These commands can permanently destroy work if misused.

```bash
git reset --hard
git clean -f
git push --force
```

Use only when you fully understand consequences.

---

# 30. Most Important Commands to Master First

```bash
git init
git status
git add
git commit
git push
git pull
git branch
git checkout
git merge
git clone
git log
git diff
```

These commands cover the majority of real-world Git usage.

---


