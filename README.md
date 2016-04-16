# Automated download clicker
Combining virtual mouse clicker with multiple ENA dataset downloads

I want to use python's virtual mouse-clicker package to programmatically download multiple datasets from EMBL-EBI's ENA website. 
The script named 'extractor.py' will be the initiator which must be run to do this.

The script will use:

-python2.7

-packages: bs4, requests,selenium

-XML file generated after launching a specific ENA query

-getlinks.py and getloads.py, both in the same directory as extractort.py

# Usage steps

Note: To see a simple example, skip steps 1-4 and just use the given "ena.xml" file

1- Make a query on EMBL-EBI's ENA website, i.e "human gut"

2- On the left, under "Read", select Experiment

3- Under "Genome assembly contig set ( _ results found)", select and download XML

4- Make sure that this file is named "ena.xml" or make necessary changes in "getlinks.py"


5- Check that package requirements are met for each script (5-10 minutes of download time at worst)

6- Enter your email in line 14 of "extractor.py" for safely (may be unnecessary)

7- Launch the entire program by simply running "extractor.py". Any error should create a log file telling the reason of failure.
