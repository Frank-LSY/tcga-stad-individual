#!/bin/bash

function count_lines ()
{
#这里`为esc下面的按键符号
  for file in `ls $1`
  do
#这里的-d表示是一个directory，即目录/子文件夹
    if [ -d $1"/"$file ]
    then
#如果子文件夹则递归
      count_lines $1"/"$file $out
    else
#否则就能够读取该文件的地址
      #echo $1"/"$file
#读取该文件的文件名，basename是提取文件名的关键字
  	echo `basename $file`
    echo $1
    echo $2
    cat $1"/"`basename $file`|wc -l>>$2
    fi
  done
}

cin_folder="../extract/cin/"
ebv_folder="../extract/ebv/"
gs_folder="../extract/gs/"
msi_folder="../extract/msi/"

cin_out_folder="../qualified_lines/cin/"
ebv_out_folder="../qualified_lines/ebv/"
gs_out_folder="../qualified_lines/gs/"
msi_out_folder="../qualified_lines/msi/"

for tumor_id in `ls $cin_folder`
do
	dest_dir="${cin_folder}${tumor_id}"
	mkdir -pv ${cin_out_folder}
	cin_out="${cin_out_folder}${tumor_id}.csv"
	count_lines $dest_dir $cin_out
done

for tumor_id in `ls $ebv_folder`
do
	dest_dir="${ebv_folder}${tumor_id}"
	mkdir -pv ${ebv_out_folder}
	ebv_out="${ebv_out_folder}${tumor_id}.csv"
	count_lines $dest_dir $ebv_out
done

for tumor_id in `ls $gs_folder`
do
	dest_dir="${gs_folder}${tumor_id}"
	mkdir -pv ${gs_out_folder}
	gs_out="${gs_out_folder}${tumor_id}.csv"
	count_lines $dest_dir $gs_out
done

for tumor_id in `ls $msi_folder`
do
	dest_dir="${msi_folder}${tumor_id}"
	mkdir -pv ${msi_out_folder}
	msi_out="${msi_out_folder}${tumor_id}.csv"
	count_lines $dest_dir $msi_out
done

