#! usr/bin env python
'''
	This will be my main script for multiple EMBL-EBI file downloads.
	I will need to call other scripts from within here. I will also
	have to make sure that there is a place for all records to go.
	I should also take all necessary safety precautions such as provide
	my contact details and using SSH encryption(optional for now). In the end,
	I should have a folder containing extracted fastq files.

'''
# safety_first.py
from Bio import Entrez
# Contact details for website. # No email = NCBI blocks Newcastle!!
Entrez.email = "C.A.Tuna2@newcastle.ac.uk" 

import os,subprocess,time
from subprocess import Popen, PIPE
__location__=os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))

try:
	# getlinks.py
	script_1=os.path.join(__location__,'getlinks.py')
	first=process = subprocess.Popen(["python",script_1],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	# Time has to be given to let the first script finish before starting the second
	time.sleep(3)
	# getloads.py
	script_2=os.path.join(__location__,'getloads.py')
	process = subprocess.Popen(["python",script_2],stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	
	# Standard error
	x = process.stderr.read()
	# Standard output
	y = process.stdout.read()
	
	# Keeping log
	outPATH=os.path.join(__location__,'log.txt')
	with open(outPATH,'wb') as put:
		put.write(x)
		put.write(y)
	
	
	
except Exception,e:
	print '\n',str(e)
	os.system("pause")

# With stdout=subprocess.PIPE, script show no output. Beware: raw_input == deadlock
# Extracting archive contents is too hard in python
# From this point onwards, I will just create and use pipes
