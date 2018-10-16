#!/bin/bash

function pre ()
{
#这里`为esc下面的按键符号
  for file in `ls $1`
  do
#这里的-d表示是一个directory，即目录/子文件夹
    if [ -d $1"/"$file ]
    then
#如果子文件夹则递归
      pre $1"/"$file
    else
#否则就能够读取该文件的地址
      #echo $1"/"$file
#读取该文件的文件名，basename是提取文件名的关键字
  	#echo `basename $file`
  	cd ../pre/
  	mkdir -pv $3/`basename $file`/$4
  	for line in `cat $2`
  	do
  		echo $line
  		python3.6 ../ref/mhcnuggets-2.0/mhcnuggets/src/predict.py \
  		-c I \
  		-p $1`basename $file` \
  		-a $line \
  		-o "$3/`basename $file`/$4/$line.csv"
  	done
   fi
  done
}

folder="../pep/ebv/"
hla="../dataset/HLA-A.csv"
stad="ebv"
type="A"
pre $folder $hla $stad $type
folder="../pep/ebv/"
hla="../dataset/HLA-B.csv"
stad="ebv"
type="B" 
pre $folder $hla $stad $type
folder="../pep/ebv/"
hla="../dataset/HLA-C.csv" 
stad="ebv"
type="C"
pre $folder $hla $stad $type

folder="../pep/msi/"
hla="../dataset/HLA-A.csv"
stad="msi"
type="A"
pre $folder $hla $stad $type
folder="../pep/msi/"
hla="../dataset/HLA-B.csv"
stad="msi"
type="B" 
pre $folder $hla $stad $type
folder="../pep/msi/"
hla="../dataset/HLA-C.csv" 
stad="msi"
type="C"
pre $folder $hla $stad $type

folder="../pep/gs/"
hla="../dataset/HLA-A.csv"
stad="gs"
type="A"
pre $folder $hla $stad $type
folder="../pep/gs/"
hla="../dataset/HLA-B.csv"
stad="gs"
type="B" 
pre $folder $hla $stad $type
folder="../pep/gs/"
hla="../dataset/HLA-C.csv" 
stad="gs"
type="C"
pre $folder $hla $stad $type