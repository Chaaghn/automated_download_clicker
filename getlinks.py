#! usr/bin env python
''' This script requires:
        sudo -H pip install requests
        sudo -H apt-get install build-essential libssl-dev libffi-dev python-dev
        sudo -H pip install --upgrade ndg-httpsclient
        sudo -H pip install bs4

    Potential links ot use:
        http://www.ebi.ac.uk/ena/data/search?query=human+gut+fastq
        ftp://ftp.sra.ebi.ac.uk/vol1/fastq/SRR294/

    Warning! The following link will change based on search.html location
        file:///D:/Dropbox/linux/search.html

    Note that all files used for this scrip should also be in the same directory
    as the script itself. Otherwise their file paths will not be definable

    The aim of this scrip is:
        To create a list of accession numbers for samples returned from an
        EMBL-EBI search, and then create a list of download links from them
'''
# Part 1: Download list creation
def getlinks():
	import os.path
	__location__= os.path.realpath(os.path.join(\
	os.getcwd(), os.path.dirname(__file__)))

	# Lets begin by defining a html object
	# TO find download links, we will need to make requests and have some beautiful soup
	import requests,bs4

	# EMBL-EBI is nice enough to create XML files out of search results
	# This should give us a list of accession numbers for all samples
	# I can then use this list to create links to each of these samples
	emblSearch = open(os.path.join(__location__,'ena.xml'))
	sampleNames = bs4.BeautifulSoup(emblSearch.read(),'xml')
	emblSearch.close()
	# Now we can use CSS selectors and
	nameNo= len(sampleNames.select('PRIMARY_ID'))
	print '<Number of samples found>\n',nameNo,'\n'
	ID=list((sampleNames.select('PRIMARY_ID')))

	# Now we can just use the extensions of our list objects to get desired text
	rangeNo=range(0,nameNo,1)
	IDlist=[]
	for i in rangeNo:
		grab=ID[i].text
		IDlist.append(grab)
	# print IDlist,'\n'

	# Looking at the html link, we see that the coding used is utf-8 (unicode)
	# Therefore, to get a normal string(wihtout u's), we use a decoder in a loop
	names=[]
	for i in rangeNo:
		names.append(str(IDlist[i].decode('utf-8')))
	# print names,'\n'
	# Finally, a list of html links to use can be obtained through string formats
	HTMLS=open((os.path.join(__location__,'secondary_accession.txt')),'w')
	for n in rangeNo:
		path='http://www.ebi.ac.uk/ena/data/view/%s' % (names[n])
		HTMLS.write(path)
		HTMLS.write('\n')
	HTMLS.close()
	# At this point, a file called 'links.txt' should be create with links inside
getlinks()