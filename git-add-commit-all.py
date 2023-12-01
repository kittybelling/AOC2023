
from datetime import datetime 

now = datetime.now() 
dt = now.strftime("%Y%m%d_%H%M%S")


import os
from git import Repo
cwd = os.getcwd()
repo = Repo(cwd)
git = repo.git 

git.add(".")
git.commit("-m","auto-commit from python : "+dt)