#! usr/bin/env python
# Set up a path to current directory
import os,bs4,requests,time
__location__=os.path.realpath(os.path.join(os.getcwd(),os.path.dirname(__file__)))
# Create a file to store downloads
myfolder= (os.path.join(__location__,'getloads_output'))
if not os.path.exists(myfolder):
    os.makedirs(myfolder)
# A list of HTMLS will need to be used 
textfile=open(os.path.join(__location__,'secondary_accession.txt'),'r')
lines= textfile.readlines()
textfile.close()
# By adding a single parameter to the function, making small changes to the upper code, 
# and creating a loop at the end, inheritance kicks in and we can download multiple files. 
def gimmi(n):
	# We only want link strings, so new lines must be removed with regex
	import re
	link=str(lines[n].replace('\n',''))
	print link
	
	# Now its time to make beautiful soup requests
	import os,bs4,requests
	emblSearch = requests.get(link,'lxml')
	# First we create a temporary FIREFOX profile to bypass the pop-up prompt
	from selenium import webdriver
	from selenium.webdriver.firefox.firefox_profile import FirefoxProfile

	# Now we start to define a temporary FIREFOS profile to allow auto downloads
	profile = FirefoxProfile()
	# Stop files from being downloaded in downloads folder
	profile.set_preference("browser.download.folderList", 2)
	# Stop showing download progress
	profile.set_preference("browser.download.manager.showWhenStarting", False)
	# Set new folder download path
	profile.set_preference("browser.download.dir",myfolder)
	# Finally, allow auto download of GZIP files(fastq files)
	profile.set_preference("browser.helperApps.neverAsk.saveToDisk", 'application/gzip')
	
	
	driver =webdriver.Firefox(firefox_profile=profile)
	driver.get(link)
	# Desired link is names File 1
	downlink = driver.find_element_by_partial_link_text('File 1')
	import time
	try:
		downlink.click()
		# Six seconds of download allowance
		time.sleep(6)
		# There is probably a better way to do this but I couldn't find it
	except:
		os._exit(0)	
	driver.quit()
for n in range(0,len(lines),1):
	gimmi(n)