#!/bin/bash

function hla_union()
{
	file_array=()
	let i=0
	for file in `ls $1`
	do
		file_array[i]=`basename $file`
		let i=$i+1
	done
	#echo ${file_array[1]}
	let len=$3
	tcga_file=()
	let i=0
	for item in ${file_array[@]}
	do
		dir="$1/$item/$2"
		for file in `ls $dir`
		do
			tcga_file[i]=`basename $file`
			let i=$i+1
			#echo ${tcga_file[i]}
		done
		#echo ${tcga_file[1]}
		for(( j=0; j<=$3; j++))
		do
			if [ $j -eq 0 ]
			then
				cat "$dir/${tcga_file[j]}" "$dir/${tcga_file[`expr $j + 1`]}" |sort|uniq > "$dir/tmp-`expr $j + 1`.csv"
			else
				cat "$dir/tmp-$j.csv" "$dir/${tcga_file[`expr $j + 1`]}" |sort|uniq > "$dir/tmp-`expr $j + 1`.csv"
			fi
		done

		for (( k=1; k<=$3; k++))
		do
			rm "$dir/tmp-$k.csv"
		done
		mkdir -pv "../hla-union/$item/"
		mv "$dir/tmp-`expr $3 + 1`.csv" "../hla-union/$item/$2.csv"
	done
}

folder="../hla"
#type1="cin"
#len1=136
#hla_union $folder $type1 $len1
type2="ebv"
len2=20
hla_union $folder $type2 $len2
type3="gs"
len3=48
hla_union $folder $type3 $len3
type4="msi"
len4=60
hla_union $folder $type4 $len4




