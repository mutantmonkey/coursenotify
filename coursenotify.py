#!/usr/bin/python
import urllib.parse, urllib.request, urllib.error
import re

import config
from emailgateway import EmailGateway
from time import sleep

nosectex = b"NO SECTIONS FOUND FOR THIS INQUIRY."

postdata = {
	'CAMPUS' : config.campus,
	'TERMYEAR': config.termyear,
	'CORE_CODE' : "AR%",
	'SUBJ_CODE' : "%",
	'SCHDTYPE' : "%",

	'BTN_PRESSED' : "FIND class sections",
	'inst_name' : "",
}

gateway = EmailGateway(config.from_addr, config.smtp_host, config.smtp_port, config.smtp_tls, config.smtp_user, config.smtp_pass)

def check_sections():
	for crn in config.crns:
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
		page = urllib.request.urlopen(config.url, data=encoded)
		result = page.read()

		if re.search(nosectex, result) is None:
			#print("CRN %d: Section open" % crn)
			gateway.send(config.notify_addr, "CRN %d Open" % crn, "The section with CRN %d is now open" % crn)
		#else:
		#	print("CRN %d: Section full" % crn)

check_sections()

