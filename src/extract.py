#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 22 11:14:57 2018

@author: frank-lsy
"""
import time
import re
import pandas as pd 
import csv
import os

f = '../一条龙/mutect.maf'
f1 = '../gender/male.maf'
f2 = '../gender/female.maf'
g1 = '../gender/cin-male.maf'
g2 = '../gender/gs-male.maf'
g3 = '../gender/ebv-male.maf'
g4 = '../gender/msi-male.maf'
g5 = '../gender/male.maf'
g6 = '../gender/female.maf'
g7 = '../gender/cin-female.maf'
g8 = '../gender/gs-female.maf'
g9 = '../gender/ebv-female.maf'
g10 = '../gender/msi-female.maf'

dir1 = '../individual/cin/'
dir2 = '../individual/gs/'
dir3 = '../individual/ebv/'
dir4 = '../individual/msi/'

cin = open('../tcga-stad/new/1-new.csv','r')
gs = open('../tcga-stad/new/2-new.csv','r')
ebv = open('../tcga-stad/new/3-new.csv','r')
msi = open('../tcga-stad/new/4-new.csv','r')
male = open('../tcga-stad/gender/male.csv','r')
female = open('../tcga-stad/gender/female.csv','r')



cin_arr = cin.readlines()
gs_arr = gs.readlines()
ebv_arr = ebv.readlines()
msi_arr = msi.readlines()
male_arr = male.readlines()
female_arr = female.readlines()
#print (cin_arr)




def strip(arr):
    p=re.compile('\n')
    for i in range(len(arr)):
        arr[i]=re.sub(p,'',arr[i])
    #print(arr)
    return arr

def extract(input_file,source_arr,output_dir):
    head = 'Hugo_Symbol	Entrez_Gene_Id	Center	NCBI_Build	Chromosome	Start_Position	End_Position	Strand	Variant_Classification	Variant_Type	Reference_Allele	Tumor_Seq_Allele1	Tumor_Seq_Allele2	dbSNP_RS	dbSNP_Val_Status	Tumor_Sample_Barcode	Matched_Norm_Sample_Barcode	Match_Norm_Seq_Allele1	Match_Norm_Seq_Allele2	Tumor_Validation_Allele1	Tumor_Validation_Allele2	Match_Norm_Validation_Allele1	Match_Norm_Validation_Allele2	Verification_Status	Validation_Status	Mutation_Status	Sequencing_Phase	Sequence_Source	Validation_Method	Score	BAM_File	Sequencer	Tumor_Sample_UUID	Matched_Norm_Sample_UUID	HGVSc	HGVSp	HGVSp_Short	Transcript_ID	Exon_Number	t_depth	t_ref_count	t_alt_count	n_depth	n_ref_count	n_alt_count	all_effects	Allele	Gene	Feature	Feature_type	One_Consequence	Consequence	cDNA_position	CDS_position	Protein_position	Amino_acids	Codons	Existing_variation	ALLELE_NUM	DISTANCE	TRANSCRIPT_STRAND	SYMBOL	SYMBOL_SOURCE	HGNC_ID	BIOTYPE	CANONICAL	CCDS	ENSP	SWISSPROT	TREMBL	UNIPARC	RefSeq	SIFT	PolyPhen	EXON	INTRON	DOMAINS	GMAF	AFR_MAF	AMR_MAF	ASN_MAF	EAS_MAF	EUR_MAF	SAS_MAF	AA_MAF	EA_MAF	CLIN_SIG	SOMATIC	PUBMED	MOTIF_NAME	MOTIF_POS	HIGH_INF_POS	MOTIF_SCORE_CHANGE	IMPACT	PICK	VARIANT_CLASS	TSL	HGVS_OFFSET	PHENO	MINIMISED	ExAC_AF	ExAC_AF_Adj	ExAC_AF_AFR	ExAC_AF_AMR	ExAC_AF_EAS	ExAC_AF_FIN	ExAC_AF_NFE	ExAC_AF_OTH	ExAC_AF_SAS	GENE_PHENO	FILTER	CONTEXT	src_vcf_id	tumor_bam_uuid	normal_bam_uuid	case_id	GDC_FILTER	COSMIC	MC3_Overlap	GDC_Validation_Status\n'
    for item in source_arr:
        f = open(input_file,'r')
        line_num = 0
        g = open(output_dir+item+'.maf','w')
        g.writelines(head)
        print("writing the "+item+" file.")
        while 1:
            line_num += 1
            line = f.readline()
            #print(line)
            match = item+'-[0-9][0-9][A-Z]-[0-9][0-9][A-Z]-[A-Z0-9][A-Z0-9][A-Z0-9][A-Z0-9]-08'
            #print (item)
            t = re.findall(r''+match,line)
            if (t):
                #print(item)
                #print(line_num)
                g.writelines(line)
            if not line:
                break
        f.close()
    g.close()


new_cin = strip(cin_arr)
new_gs = strip(gs_arr)
new_ebv = strip(ebv_arr)
new_msi = strip(msi_arr)
#new_male = strip(male_arr)
#new_female = strip(female_arr)

#cin_result = extract(f1,new_cin,g1)
cin_result = extract(f,new_cin,dir1)
print ('finish!!!')
gs_result = extract(f,new_gs,dir2)
#gs_result = extract(f2,new_gs,g8)
print ('finish!!!')
ebv_result = extract(f,new_ebv,dir3)
#ebv_result = extract(f2,new_ebv,g9)
print ('finish!!!')
msi_result = extract(f,new_msi,dir4)
#msi_result = extract(f2,new_msi,g10)
print ('finish!!!')
#male_result = extract(f,new_male,g5)
print('finish!!!')
#female_result = extract(f,new_female,g6)
print('finish!!!')


