coursenotify
============

This script is intended to be run via cron and will send out email notifications when a course opens on a Banner-based course registration system.

To use it, you'll need a config.py file that looks something like this:

	url = "https://banweb.banner.vt.edu/ssb/prod/HZSKVTSC.P_ProcRequest"
	crns = []

	campus = 0
	termyear = 201101

	notify_addr = ""
	from_addr = ""

	smtp_host = "smtp.gmail.com"
	smtp_port = 465
	smtp_tls = True
	smtp_user = ""
	smtp_pass = ""

You'll want to fill in the blanks and modify the settings to get it working for your school, of course.

