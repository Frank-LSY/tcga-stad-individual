依赖环境安装：
===
A MHCnuggets
---
	pip(3/3.5/3.6/3.7) install mhcnuggets

B ensembl-vep
---
	需安装依赖软件

	B1 mysql
		sudo apt-get install mysql-server
		sudo apt install mysql-client
		sudo apt install libmysqlclient-dev
		检测：
		sudo netstat -tap | grep mysql

	B2 DBI
		cpan (install) DBI
	
	B3 DBD::mysql
		cpan (install) DBD::mysql

	安装完成依赖软件之后安装ensembl-vep
	git clone https://github.com/Ensembl/ensembl-vep.git
	(ps:没有安装git请自行安装。。。。。。)
	cd ensembl-vep
	perl INSTALL.pl
	
	ps:	
		安装时候基本一路选择yes，记得要安装plugins。
		不需要安装fasta，如果根目录剩余空间够大(>10G)可以安装cache，否则手动下载cache。		
		***安装所有的Plugins!!!*** (即选择0:all)
		手动下载cache方法：
			在ensembl-vep下
			mkdir cache
			cd cache
			curl -O ftp://ftp.ensembl.org/pub/release-94/variation/VEP/homo_sapiens_vep_94_GRCh38.tar.gz
			tar zxvf homo_sapiens_vep_94_GRCh38.tar.gz
		
		pps:安装过程中提示缺什么就直接cpan (install) *库名称*
			Module::Build
			Try::Tiny

C pvactools
---
	pip(3/3.5/3.6/3.7) install pvactools
	下载完成后，找到pvactools文件夹并打开， cd tools/pvacseq/VEP_lugins. 会看到一个Wildtype.pm 将其复制到/root/.vep/Plugins文件夹中。
		ps:pvactools文件夹通常在python3的默认安装文件夹中。(/usr/local/lib/python3.5/disk-packages/tools)

D samtools (maf2vcf会用到)
---	
	先安装依赖软件

	D1 autoconf
		sudo apt-get install autoconf

	D2 htslib	
		git clone https://github.com/samtools/htslib.git
		apt-get install libbz2-dev
		apt-get install liblzma-dev
		autoheader
		autoconf
		./configure
		make
		make install

	D3 curses
		apt-get install libncurses5-dev

	安装完成依赖软件之后安装samtools
	git clone https://github.com/samtools/samtools.git
	cd samtools
	autoheader
	autoconf -Wno-syntax
	./configure --with-htslib=/htslib/install/dir(/usr/local/include/htslib)
	make
	make install
	


整体运行流程
===
STEP①:利用gdc-scan从gdc-portal提取somatic mutation数据  TCGA.[type].[predict-method].maf
---
	1.	搜索指定癌症类型的突变注释格式文件(Mutation Annotation Format, MAF)
		18种癌症癌症类型数据来自 [gdc-portal](https://portal.gdc.cancer.gov/)
	
	2.	运行gdc_scan.py脚本，其中注意：
			python gdc_scan.py files download --format MAF --project TCGA-XXXX
			python gdc_scan.py files download --project TCGA-XXXX --type "Clinical Supplement"
			2.1. 第9行应改为：URL_BASE="https://api.gdc.cancer.gov/"
			2.2. 第10行应改为：LEGACY_BASE="https://api.gdc.cancer.gov/legacy/"

	3.	运行结束后得到压缩包，选择其中 TCGA.STAD.mutect.*.maf.gz 进行解压
		即 gzip -d TCGA.STAD.mutect.*.maf.gz
	4.	移动该maf文件至创建的工作目录中，并重命名为mutect.maf
	5.	mutect.maf文件的前五行需要删除，同时由于染色体表示方式与fasta文件不符，需要删除各条目对应的”chr“,故共有两步操作:
			sed -i '1,5d' mutect.maf //删去前5行
			vim mutect.maf 	//打开文件
			:%s/chr//g 		//正则匹配chr并替换为空字符串
			Enter 			//执行
			:wq				//保存




STEP②:利用爬虫从[网站](http://compbio-research.cs.brown.edu/public/stad/#!/)爬取胃癌四种分型分别包含的患者ID
---
	1.运行tcga-stad.py
		即 python(3/3.5/3.6/3.7) tcga-stad.py
		会新建tcga-stad文件夹，产生1(cin)/2(ebv)/3(gs)/4(msi).csv四个文件。
		ps:
			1.提示缺少什么python库直接 pip(3/3.5/3.6/3.7) install *库名称*
			2.利用模拟网页访问的方式进行数据爬取，故需提前安装chromedriver(谷歌浏览器)或geckodriver(火狐浏览器)，直接网页下载即可，windows环境下放在tcga-stad.py当前文件夹，linux环境放在/usr/bin/目录下。
				pps:可能会提示driver无法运行类似错误，尝试更新电脑本身浏览器至最新再重试。

	2.爬取数据会出现大量重复，调用duplicate.py进行去重
		即 python(3/3.5/3.6/3.7) duplicate.py
		会在tcga-stad中新建new文件夹，产生1-new/2-new/3-new/4-new.csv四个文件。为最终结果。

	最终得到抽取好的各分型对应患者ID。
	输出:../tcga-stad/new/type.csv(tcga-stad/new/cin.csv)

STEP③:从maf文件提取各ID对应的maf文件
---
	将从网页上提取的四组不同类型的胃癌从maf文件中分离。
	输入:mutect.maf
	输出:../data/type/sample.maf (data/cin/TCGA-BR-4183.maf)

STEP④:利用maf2vcf进行文件格式转换
---
	使用vcf2maf中的maf2vcf工具将MAF文件转换为VCF文件
	谷歌搜索[Homo_sapiens.GRCh38.dna_sm.primary_assembly.fa.gz]并下载解压到 ./dataset
	maf2vcf.pl脚本中第12行的 Homo_sapiens.GRCh*.fa.gz 路径更新为 ../dataset/Homo_sapiens.GRCh38.dna_sm.primary_assembly.fa.gz
	maf2vcf.pl脚本第105行，splice( @regions, 0, 50000 ),其中50000可根据电脑情况更改，一般Cent0S和Ubuntu不用改。

	调用脚本2vcf.sh进行文件批量文件格式转换
	输入：../data/type/sample.maf (data/cin/TCGA-BR-4183.maf)
	输出：../vcf/type-vcf/sample.vcf (vcf/cin-vcf/TCGA-BR-4183.vcf)

STEP⑤:利用ensembl-vep进行注释
---
	直接调用vep.sh脚本进行文件批量注释。
	输入:../vcf/type-vcf/sample.vcf (vcf/cin-vcf/TCGA-BR-4183.vcf)
	输出:../vep-vcf/type-vep/sample.vcf (vep-vcf/cin-vep/TCGA-BR-4183.vcf)
	
	注释命令
		./vep -i <input-vcf> -o <output-vcf> \
		--format vcf --vcf --symbol --terms SO --tsl \
		--hgvs --fasta <reference build fasta file location> \
		--cache --dir_cache <VEP cache directory> \
		--plugin Downstream --plugin Wildtype \
		[--dir_plugins <VEP_plugins directory>] --pick [--transcript_version] \
		--no_stats [--fork num]
	
	需要将注释后的vep中normal数据删掉，调用cut.py脚本

STEP⑥:利用filter_vep.pl脚本过滤vcf文件
---
	对于像TCGA-BR-4183-vep.vcf这样的文件，其中第220行H列蛋白质很长，需要额外进行过滤操作
	运行filter_vep.pl脚本
	
	输入：../vep-vcf/type-vep/sample.vcf (vep-vcf/cin-vep/TCGA-BR-4183.vcf)
	输出：../RP/to/filtered_file/sample.vcf ()

	过滤命令
		./filter_vep \
		-i <input_file> \
		-o <output_file> \
		-filter "Feature != ENST00000589042"


STEP⑦：运行pVACseq得到fasta文件
---
	
	移除正常样本数据并过滤之后的vcf文件与pVACseq兼容，运行pVACseq得到相应长度的多肽链
	
	输入：../RP/to/filtered/sample.vcf ()
	输出：../RP/to/output/fasta_file/sample.fa ()
	
	pVACseq命令
		pvacseq generate_protein_fasta [-h] [-d DOWNSTREAM_SEQUENCE_LENGTH]
						<input_file> <peptide_sequence_length>
						<output_file>
STEP⑧：运行pep.sh脚本抽取偶数行多肽
---
	对于得到的fasta文件，我们只需要偶数行的多肽
	
	输入：../RP/to/fasta_file/sample.fa ()
	输出：../RP/to/pep_file/sample.pep ()
	
	pep命令
		./pep.sh
		awk 'NR%2==O'
		
STEP⑨：利用mhcnuggets预测IC50值
---
	输入： ../RP/to/pep_file/sample.pep ()
	输出： ../RP/to/predict_file/sample.csv ()

	mhcnuggets-2.0/mhcnuggets/src/predict.py
	
	交互窗口命令[mhcnuggets] https://github.com/KarchinLab/mhcnuggets-2.0/blob/master/user_guide.ipynb
















