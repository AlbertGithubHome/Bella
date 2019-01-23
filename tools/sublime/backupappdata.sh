#!/bin/bash

src_path="C:/Users/Administrator/AppData/Roaming/Sublime Text 3"
dst_path="E:/GitProject/Bella/tools/sublime"
zip_name=appdata_roaming_st3.zip

cd "$src_path"
zip -r $zip_name *
mv -f $zip_name "$dst_path"
cd "$dst_path"

cp -f "$src_path/Installed Packages/"*.sublime-package "./Installed Packages/"

cp -f "$src_path""/Packages/User/"*.sublime-settings ./User/
cp -f "$src_path""/Packages/User/"*.sublime-keymap ./User/
cp -f "$src_path""/Packages/User/"*.sublime-build ./User/
cp -f "$src_path""/Packages/User/"*.json ./User/
cp -f "$src_path""/Packages/User/"*.py ./User/

git pull
git add .
git commit -m"update sublime configuration"
git push
