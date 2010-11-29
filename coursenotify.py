#!/usr/bin/python
import urllib.parse, urllib.request, urllib.error
#import lxml.html
import re

url = "https://banweb.banner.vt.edu/ssb/prod/HZSKVTSC.P_ProcRequest"
crns = [12013, 11918]

nosectex = b"NO SECTIONS FOUND FOR THIS INQUIRY."

postdata = {
	'CAMPUS' : 0,
	'TERMYEAR': 201101,
	'CORE_CODE' : "AR%",
	'SUBJ_CODE' : "%",
	'SCHDTYPE' : "%",

	'BTN_PRESSED' : "FIND class sections",
	'inst_name' : "",
}

for crn in crns:
	postdata['crn'] = crn
	postdata['open_only'] = ""

	# ensure that section exists
	#encoded = urllib.parse.urlencode(postdata)
	#page = urllib.request.urlopen(url, data=encoded)
	#result = page.read()
	
	#if re.search(nosectex, result) is not None:
		#print("CRN %d: Section does not exist" % crn)

	# check to see if there are open seats
	postdata['open_only'] = "on"
	encoded = urllib.parse.urlencode(postdata)
	page = urllib.request.urlopen(url, data=encoded)
	result = page.read()

	if re.search(nosectex, result) is None:
		print("CRN %d: Section open" % crn)
	else:
		print("CRN %d: Section full" % crn)

