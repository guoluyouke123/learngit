# learngit

## SSH Key

#### How to creat SSH key

1. open terminal and type `ssh-keygen -t rsa`
2. Repeat taping return
3. Two files： “public key” and “secret key” generated

#### How to get and add SSH key on Github
1. Type `open -a TextEdit ~/.ssh/id_rsa.pub` in terminal to get SSH public key
2. Paste it on Github. The page is "https://github.com/settings/keysy"
***

## Git Command 

In this section, several important git commands has been 
used in an example, which is for installing pytorch and checking its version.

#### Clone a repo from Github to Pycharm
1. Create a new project on Pycharm
2. Clone repo from Github to Pycharm
3. Type `git clone git@github.com:guoluyouke123/learngit.git` on Pycharm terminal

#### Save changes by using git commands
1. Make directories by typing `mkdir -p src/main/python/torch/` and then make a python file called 
"utils" under torch
2. Type `git status` to check my current change. The red words refers the directory I made changes
3. Type `git status -u`, show what files I made changes on
4. Type `git checkout -b torch` to create a feature branch called torch then switch to this new generated branch
5. Start writing features and then type `git add .` or `git add -A` in Pycharm terminal to save these changes to 
local feature. This process is called pre-save
6. Type `git commit -m 'message'` to comment your changes you made. This process completes the whole process of saving all changes 
into feature branch
7. After previous step, local feature branch is finished. If you try `git status`, you can not 
see the files anymore
8. Type `git log`, we can see all changes through timeline
9. Type `git pull`, to  download remote branch and merge it into local
#### How to install a Python package
1. Create a file "requirements.txt" under the path src/main/python
2. Type "torch" and "torchvision" in the requirements.txt
3. Type `pip install -r /Users/chengpeng/PycharmProjects/learn/learngit/src/main/python/requirements.txt` 
in the Pycharm terminal to install all required packages.
4. If there is any other packages need to be installed, just type the names into requirements.txt file

####

#### Summary for some terms 
1. The master branch on Github is called “remote master”
2. The master branch on local PC is called “local master”
3. The feature branch on local PC is called “local feature”
4. The forward path: remote master - local master - local feature - file
5. The backward path: file - local feature - remote feature - remote master


#### Summary for important and most frequently used git commands
1. Check the current branch by typing `git branch` in Pycharm terminal. The green words means what the branch we are in
2. `git checkout -b torch` create a feature branch called torch then switch to this new generated branch
3. ...