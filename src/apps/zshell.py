# coding: utf8

shortcuts = {
    "zshell":{
        #https://github.com/robbyrussell/oh-my-zsh/wiki/Cheatsheet
        "Create a new tab in the current directory (macOS - requires enabling access for assistive devices under System Preferences).":"tabs",
        "Create a new directory and change to it, will create intermediate directories as required.":"take",
        "Extract an archive (supported types: tar.{bz2,gz,xz,lzma}, bz2, rar, gz, tar, tbz2, tgz, zip, Z, 7z).":"x / extract",
        "Get a list of the top 20 commands and how many times they have been run.":"zsh_stats",
        "Uninstall Oh-my-zsh.":"uninstall_oh_my_zsh",
        "Upgrade Oh-my-zsh.":"upgrade_oh_my_zsh",
        "Uptake new changes":"source ~/.zshrc",
        "list all aliases":"alias",
        "cd ..":"..",
        "cd ../..":"...",
        "cd ../../..":"....",
        "cd ../../../..":".....",
        "cd /":"/",
        "cd ~":"~",
        "switch to directory number n (2-9)":"cd +n",
        "tab-completeion ls":"ls (tab)",
        "tab-completeion cap":"cap (tab)",
        "tab-completeion rake":"rake (tab)",
        "tab-completeion ssh":"ssh (tab)",
        "tab-completeion sudo unmount":"sudo unmount(tab)",
        "tab-completeion kill":"kill (tab)",
        "tab-completeion unrar":"unrar (tab)",
        "Dynamic access to current branch name with the current_branch function":"git pull origin $(current_branch)",
        "Dynamic access to current branch name with the current_branch function":"grb publish $(current_branch) origin",
        "git":"g",
        "git add":"ga",
        "git add --all":"gaa",
        "git add --patch":"gapa",
        "git branch":"gb",
        "git branch -a":"gba",
        "git branch -d":"gbd",
        "git blame -b -w":"gbl",
        "git branch --no-merged":"gbnm",
        "git branch --remote":"gbr",
        "git bisect":"gbs",
        "git bisect bad":"gbsb",
        "git bisect good":"gbsg",
        "git bisect reset":"gbsr",
        "git bisect start":"gbss",
        "git commit -v":"gc",
        "git commit -v --amend":"gc!",
        "git commit -v -a":"gca",
        "git commit -v -a --amend":"gca!",
        "git commit -v -a --no-edit --amend":"gcan!",
        "git commit -v -a -s --no-edit --amend":"gcans!",
        "git commit -a -m":"gcam",
        "git commit -s -m":"gcsm",
        "git checkout -b":"gcb",
        "git config --list":"gcf",
        "git clone --recursive":"gcl",
        "git clean -fd":"gclean",
        "git reset --hard ^^ git clean dfx":"gpristine",
        "git checkout master":"gcm",
        "git checkout develop":"gcd",
        "git commit -m":"gcmsg",
        "git checkout":"gco",
        "git shortlog -sn":"gcount",
        "git cherry-pick":"gcp",
        "git cherry-pick --abort":"gcpa",
        "git cherry-pick --continue":"gcpc",
        "git commit -S":"gcs",
        "git diff":"gd",
        "git diff --cached":"gdca",
        "git describe --tags `git rev-list --tags --max-count=1`":"gdct",
        "git diff-tree --no-commit-id --name-only -r":"gdt",
        "git diff --word-diff":"gdw",
        "git fetch":"gf",
        "git fetch --all --prune":"gfa",
        "git fetch origin":"gfo",
        "git gui citool":"gg",
        "git gui citool --amend":"gga",
        "git pull origin $(current_branch) && git push origin $(current_branch)":"ggpnp",
        "git pull origin $(current_branch)":"ggpull",
        "git pull origin $(current_branch)":"ggl",
        "git pull --rebase origin $(current_branch)":"ggpur",
        "git pull upstream master":"glum",
        "git push origin $(current_branch)":"ggpush",
        "git push origin $(current_branch)":"ggp",
        "git branch --set-upstream-to=origin/$(current_branch)":"ggsup",
        "git update-index --assume-unchanged":"gignore",
        "git ls-files -v | grep \"^[[:lower:]]\"":"gignored",
        "git svn dcommit && git push github master:svntrunk":"git-svn-dcommit-push",
        "gitk --all --branches":"gk",
        "git pull":"gl",
        "git log --stat --max-count = 10":"glg",
        "git log --graph --max-count = 10":"glgg",
        "git log --graph --decorate --all":"glgga",
        "git log --oneline --decorate --color":"glo",
        "git log --oneline --decorate --color --graph":"glog",
        "_git_log_prettily (git log --pretty=$1)":"glp",
        "git merge":"gm",
        "git mergetool --no-prompt":"gmt",
        "git push":"gp",
        "git push origin --all && git push origin --tags":"gpoat",
        "git remote":"gr",
        "git rebase --abort":"grba",
        "git rebase --continue":"grbc",
        "git rebase --skip":"grbs",
        "git rebase -i":"grbi",
        "git reset HEAD":"grh",
        "git reset HEAD --hard":"grhh",
        "git remote rename":"grmv",
        "git remote remove":"grrm",
        "git remote set-url":"grset",
        "cd $(git rev-parse --show-toplevel || echo \".\")":"grt",
        "git remote update":"grup",
        "git remote -v":"grv",
        "git svn dcommit":"gsd",
        "git show --pretty = short --show-signature":"gsps",
        "git svn rebase":"gsr",
        "git status -s":"gss",
        "git status":"gst",
        "git stash save":"gsta",
        "git stash apply":"gstaa",
        "git stash drop":"gstd",
        "git stash list":"gstl",
        "git stash pop":"gstp",
        "git stash show --text":"gsts",
        "git tag -s":"gts",
        "git update-index --no-assume-unchanged":"gunignore",
        "git log -n 1 | grep -q -c \"--wip--\" && git reset HEAD~1":"gunwip",
        "git pull --rebase":"gup",
        "git verify-tag":"gvt",
        "git whatchanged -p --abbrev-commit --pretty = medium":"gwch",
        "git add -A; git ls-files --deleted -z | xargs -r0 git rm; git commit -m \"--wip--\"":"gwip",
        "(When using sublime plugin) Open current directory in Sublime Text 2/3":"stt",
        "(When using vi-mode plugin) Edit current command line in Vim":"v",
        "Symfony2 - php ./app/console":"sf",
        "Symfony2 - php app/console cache:clear":"sfcl",
        "Symfony2 - sf debug:container":"sfcontainer",
        "Symfony2 - sf cache:warmup":"sfcw",
        "Symfony2 - sf generate:bundle":"sfgb",
        "Symfony2 - sf debug:router":"sfroute",
        "Symfony2 - sf server:run -vvv":"sfsr",
        "tmux attach -t":"ta",
        "tmux attach -d -t":'tad',
        "tmux new-session -s":"ts",
        "tmux list-sessions":"tl",
        "tmux kill-server":"tksv",
        "tmux kill-session -t":"tkss",
        "show the status of the NAME process":"sc-status NAME",
        "show the NAME systemd .service file" :"sc-show NAME",
        "start the NAME process" : "sc-start NAME",
        "stop the NAME process" : "sc-stop NAME",
        "restart the NAME process" : "sc-restart NAME",
        "enable the NAME process to start at boot" : "sc-enable NAME",
        "disable the NAME process at boot" : "sc-disable NAME",
    }
}