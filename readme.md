# Git & GitHub Practice Laboratory

A dedicated sandbox repository for mastering Version Control System (VCS) workflows, testing complex Git commands, and simulating multi-branch development environments.

---

## 🚀 Purpose & Objectives

*   **Muscle Memory:** Developing fluid execution of terminal-based Git workflows.
*   **Conflict Resolution:** Simulating and resolving merge conflicts safely.
*   **Branching Strategy:** Practicing Feature Branching, Rebasing, and Cherry-picking.
*   **Environment Syncing:** Mastering local-to-remote tracking, fetching, and pruning.

---

## 🛠️ Frequently Used Commands

### 1. Repository Initialization & Synchronization
| Command | Action |
| :--- | :--- |
| `git status` | Inspect the state of the working directory and staging area. |
| `git fetch origin` | Download objects and refs from the remote repository without merging. |
| `git pull origin <branch>` | Fetch from and integrate with another repository or a local branch. |

### 2. Branch Management
| Command | Action |
| :--- | :--- |
| `git branch -a` | List all local and remote branches. |
| `git checkout -b <new-branch>` | Create and switch to a new isolated feature branch. |
| `git switch <branch>` | Safely switch between existing branches. |
| `git branch -d <branch>` | Delete a fully merged local branch. |

### 3. Saving Changes
| Command | Action |
| :--- | :--- |
| `git add .` | Stage all current modifications for the next commit. |
| `git commit -m "feat: message"` | Record staging area snapshots permanently to history. |
| `git push -u origin <branch>` | Upload local commits to remote and set upstream tracking. |

---

## ⚠️ Sandbox Simulation Rules

1.  **Never Work on Main:** All edits happen on feature branches (e.g., `feature/app-init`, `fix/syntax`).
2.  **Clean History:** Practice squashing commits or rebasing before merging to simulate production-grade codebases.
3.  **Prune on Sync:** Keep the local tree clean by removing dead remote references.

---
*Generated for local terminal execution optimization.*
