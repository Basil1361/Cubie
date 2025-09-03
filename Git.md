Some git codes to remmeber

1) Creating a repo
cd D:\Path\To\Project
git init
echo "# My Project" > README.md
git add .
git commit -m "init: scaffold project"
git remote add origin https://github.com/USER/REPO.git
git push -u origin main

2) Existing project (want to clone)
cd D:\Code
git clone https://github.com/USER/REPO.git
cd REPO
# work → add → commit → push

3) Bring collaborator files
git fetch origin
git switch main
git pull --rebase origin main

4) Branches
git branch -M main
git switch main
git merge feature/x    
git rebase origin/main

5) git remote set-url origin https://github.com/USER/CorrectRepo.git
git fetch origin --prune
git branch --set-upstream-to=origin/main main
git pull --rebase
git push

6) Undo, Fix mistakes
git restore --staged file.py           # unstage
git restore file.py                    # discard local changes to a file
git checkout -- path/to/file           # older Git equivalent

git commit --amend                     # edit last commit message / include forgotten files
git reset --soft HEAD~1                # undo last commit, keep changes staged
git reset --mixed HEAD~1               # undo last commit, keep changes unstaged
git reset --hard HEAD~1                # ❗ discard last commit + changes (careful)

git reflog                             # timeline of HEAD moves (life saver)
git reset --hard <reflog-hash>         # jump back to a good state 
