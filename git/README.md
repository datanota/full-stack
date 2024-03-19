
# Datanota Full-Stack - GIT Version Control


### Configuration

git config --list --global  
git config --global user.name "Your Name"  
git config --global user.email "your_email@example.com"  

git config --list --local  
git config --local user.name "Your Name"  
git config --local user.email "your_email@example.com"  

q

### Directory

cd to sub-dir  
rm -rf .git  
add and commit  


### Orphan Branch

git add .  
git commit -m "updated"  
git status  
git checkout --orphan develop  
git add -A  
git commit -m "updated"  
git branch -D master  
git branch -m master  
git branch  



