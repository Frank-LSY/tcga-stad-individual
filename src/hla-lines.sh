#!/bin/bash

function hla-lines()
{
	file_array=()
	let i=0
	for file in `ls $1`
	do
		file_array[i]=`basename $file`
		let i=$i+1
	done
	#echo ${file_array[1]}

	for item in ${file_array[@]}
	do
		mkdir -pv "../hla-lines/"
		wc -l "$1/$item/$2.csv">>"../hla-lines/$item.csv"
	done
}

folder="../hla-union"
type1="cin"
type2="ebv"
type3="gs"
type4="msi"
hla-lines $folder $type1
hla-lines $folder $type2
hla-lines $folder $type3
hla-lines $folder $type4