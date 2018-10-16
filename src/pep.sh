#!/bin/bash


function pep()
{
  echo $1
#这里`为esc下面的按键符号
  for file in `ls $1`
  do
#这里的-d表示是一个directory，即目录/子文件夹
    if [ -d $1"/"$file ]
    then
#如果子文件夹则递归
      pep $1"/"$file
    else
#否则就能够读取该文件的地址
      #echo $1"/"$file
#读取该文件的文件名，basename是提取文件名的关键字
   echo PEP-ing `basename $file`
   awk 'NR%2==0' $1`basename $file` >>  ../pep/gs/`basename $file`.pep
   fi
  done
}

#函数定义结束，这里用来运行函数
folder="../fasta/gs/"
pep  $folder 
