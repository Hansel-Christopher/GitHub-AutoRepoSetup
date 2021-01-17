read -p "Enter GitHub remote URL: " remoteUrl

git init
git add .
git commit -m "first commit"
git branch -M main
git remote add origin $remoteUrl
git push -u origin main