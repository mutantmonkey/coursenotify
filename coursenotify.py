#!/usr/bin/python3
###############################################################################
# coursenotify.py - Course Notify
# Receive email notifications when a course opens up on a Banner-based course
# registration system.
# Licensed under the ISC License.
#
# https://github.com/mutantmonkey/coursenotify
# author: mutantmonkey <mutantmonkey@mutantmonkey.in>
###############################################################################

import urllib.error
import urllib.parse
import urllib.request
import re

import config
import actions.email
from time import sleep

__author__ = "mutantmonkey <mutantmonkey@mutantmonkey.in>"
__license__ = "ISC"

nosectex = b"NO SECTIONS FOUND FOR THIS INQUIRY."
coursenrex = b"<TD class=deleft style=background-color:WHITE>\n<FONT "\
        b"SIZE=\"1\">(.+?)<\/FONT>\n<\/TD>"
coursetitex = b"<TD class=deleft style=background-color:WHITE>(.+?)<\/TD>"

postdata = {
    'CAMPUS': config.campus,
    'TERMYEAR': config.termyear,
    'CORE_CODE': "AR%",
    'SUBJ_CODE': "%",
    'SCHDTYPE': "%",

    'BTN_PRESSED': "FIND class sections",
    'inst_name': "",
}

action = actions.email.Email(config.from_addr, config.notify_addr,
        config.smtp_host, config.smtp_port, config.smtp_tls, config.smtp_user,
        config.smtp_pass)


def check_sections():
    for crn in config.crns:
        postdata['crn'] = crn
        postdata['open_only'] = ""

        # check to see if there are open seats
        postdata['open_only'] = "on"
        encoded = urllib.parse.urlencode(postdata).encode('ascii')
        page = urllib.request.urlopen(config.url, data=encoded)
        result = page.read()

        if re.search(nosectex, result) is None:
            try:
                coursenr = re.search(coursenrex, result).group(1).decode(
                        'ascii')
                coursetitle = re.search(coursetitex, result).group(1).\
                        decode('ascii')
            except AttributeError:
                # skip broken CRNS
                print("Warning: CRN {0} does not exist, skipping...".format(
                    crn))
                continue

            action.course_open(coursenr, coursetitle, crn)

check_sections()
