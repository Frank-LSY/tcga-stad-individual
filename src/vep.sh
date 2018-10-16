#!/bin/bash

echo vep.sh

function vep()
{
  echo $1
#这里`为esc下面的按键符号
  for file in `ls $1`
  do
#这里的-d表示是一个directory，即目录/子文件夹
    if [ -d $1"/"$file ]
    then
#如果子文件夹则递归
      vep $1"/"$file
    else
#否则就能够读取该文件的地址
      #echo $1"/"$file
#读取该文件的文件名，basename是提取文件名的关键字
   echo VEP-ing `basename $file`
   echo `date +%H:%M`
	../ref/ensembl-vep/./vep --cache -i $1`basename $file` \
	--format vcf \
	-o ../vep-vcf/gs-vep/`basename $file` \
	--vcf --symbol --terms SO \
	--plugin Downstream --plugin Wildtype \
	--pick --no_stats --fork 2
   fi
  done
}

#函数定义结束，这里用来运行函数
folder="../vcf/gs-vcf/not/"
vep $folder 
