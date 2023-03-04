#!/bin/sh

STOCK_ANALYZE_TOOL=/root/maingit/Bella/python/stock/previousV/advanced
PUSH_PLUS_TOOL=/root/maingit/Bella/python/push
#IMG_CDN_DIR=/root/maingit/cdn/img/analyze/stock
IMG_CDN_DIR=/root/maingit/qiniu-image-bed/stockanalyze
SCRIPT_ROOT=/export/scripts


cd $STOCK_ANALYZE_TOOL
rm -f ./pic/*

chmod +x saverun
for line in $(<$SCRIPT_ROOT/stocklist);
do
  echo $line;
  ./saverun $line
done

TODAY=$(date "+%Y%m%d")
echo $TODAY



cd $IMG_CDN_DIR
git reset HEAD --hard
git pull

mkdir -p $IMG_CDN_DIR/$TODAY
cp $STOCK_ANALYZE_TOOL/pic/* $IMG_CDN_DIR/$TODAY/

git add $TODAY
git commit -m"update img for stock analyze"
git push

pwd

cd ..
chmod +x ./zqshell.sh
./zqshell.sh

IMGS=$(ls $IMG_CDN_DIR/$TODAY)
echo $IMGS

cd $PUSH_PLUS_TOOL
git reset HEAD --hard
git pull

echo "$IMGS"
python3 ./pushgroupimgs.py "$IMGS"
