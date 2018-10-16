#!/bin/bash

function add_head()
{
#这里`为esc下面的按键符号
  for file in `ls $1`
  do
#这里的-d表示是一个directory，即目录/子文件夹
    if [ -d $1"/"$file ]
    then
#如果子文件夹则递归
      add_head $1"/"$file
    else
#否则就能够读取该文件的地址
      #echo $1"/"$file
#读取该文件的文件名，basename是提取文件名的关键字
  	#echo `basename $file`
    echo $1"/"`basename $file`
    sed -i '.bak' '1i\ peptide  ic50' $1"/"`basename $file`
    fi
  done
}

folder="../normal"
add_head $folder