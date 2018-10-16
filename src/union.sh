#!/bin/bash


function union ()
{
  file_array=()
  let i=0
#这里`为esc下面的按键符号
  for file in `ls $1`
  do
#这里的-d表示是一个directory，即目录/子文件夹
#否则就能够读取该文件的地址
    #echo $1"/"$file
#读取该文件的文件名，basename是提取文件名的关键字
    #echo `basename $file`
    file_array[i]=`basename $file`
    let i=$i+1
  done
  #echo ${file_array[3]}

  for i in {0..4}
  do
    #echo ${file_array[i]}
    if [ $i -eq 0 ]
    then
      #echo ${file_array[i]}
      #echo ${file_array[`expr $i + 1`]}
      cat $1"/"${file_array[i]} $1"/"${file_array[`expr $i + 1`]}|sort|uniq > $1"/tmp-"`expr $i + 1`.csv
    else
      #echo $1"/tmp-"$i
      #echo $1"/"${file_array[i+1]}
      cat $1"/tmp-"$i.csv $1"/"${file_array[i+1]}|sort|uniq > $1"/tmp-"`expr $i + 1`.csv
    fi
  done
  
  for j in {1..4}
  do
    rm $1"/tmp-"$j.csv
  done
  mv $1"/tmp-5.csv" "$3/union-$2.csv"
}

cin_folder="../mid/cin/"
cin_out_dir="../extract/cin"
for tumor_id in `ls $cin_folder`
do
  mid_dir=${cin_folder}${tumor_id}"/"
  cin_dir=${cin_out_dir}/${tumor_id}
  mkdir -pv $cin_dir
  for k in {1..1000}
  do
    dest_dir=${mid_dir}$k
    union $dest_dir $k $cin_dir
    #echo $dest_dir
  done
  echo $tumor_id" finish!!!"
done

msi_folder="../mid/msi/"
msi_out_dir="../extract/msi"
for tumor_id in `ls $msi_folder`
do
  mid_dir=${msi_folder}${tumor_id}"/"
  msi_dir=${msi_out_dir}/${tumor_id}
  mkdir -pv $msi_dir
  for k in {1..1000}
  do
    dest_dir=${mid_dir}$k
    union $dest_dir $k $msi_dir
    #echo $dest_dir
  done
  echo $tumor_id" finish!!!"
done

ebv_folder="../mid/ebv/"
ebv_out_dir="../extract/ebv"
for tumor_id in `ls $ebv_folder`
do
  mid_dir=${ebv_folder}${tumor_id}"/"
  ebv_dir=${ebv_out_dir}/${tumor_id}
  mkdir -pv $ebv_dir
  for k in {1..1000}
  do
    dest_dir=${mid_dir}$k
    union $dest_dir $k $ebv_dir
    #echo $dest_dir
  done
  echo $tumor_id" finish!!!"
done

gs_folder="../mid/gs/"
gs_out_dir="../extract/gs"
for tumor_id in `ls $gs_folder`
do
  mid_dir=${gs_folder}${tumor_id}"/"
  gs_dir=${gs_out_dir}/${tumor_id}
  mkdir -pv $gs_dir
  for k in {1..1000}
  do
    dest_dir=${mid_dir}$k
    union $dest_dir $k $gs_dir
    #echo $dest_dir
  done
  echo $tumor_id" finish!!!"
done