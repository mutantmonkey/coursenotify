from smtplib import SMTP, SMTP_SSL
from email.mime.text import MIMEText

class Email(object):
    def __init__(self, sender, recipient, smtp_host, smtp_port, smtp_tls,
            smtp_user, smtp_pass):
        self.sender = sender
        self.recipient = recipient

        self.smtp_host = smtp_host
        self.smtp_port = smtp_port
        self.smtp_tls = smtp_tls
        self.smtp_user = smtp_user
        self.smtp_pass = smtp_pass

    def _login(self):
        if self.smtp_tls:
            self.conn = SMTP_SSL(self.smtp_host, self.smtp_port)
        else:
            self.conn = SMTP(self.smtp_host, self.smtp_port)

        if len(self.smtp_user) > 0:
            self.conn.login(self.smtp_user, self.smtp_pass)

    def _send(self, msg):
        self._login()
        self.conn.sendmail(self.sender, self.recipient, msg.as_string())
        self.conn.quit()

    def course_open(self, coursenr, coursetitle, crn):
        text = """\
Hello,

This message is to inform you that at last run, coursenotify
found an open seat in {nr} {title}, CRN {crn}.

You will continue to receive notifications the next time coursenotify
runs unless you remove this CRN from your configuration.
"""

        msg = MIMEText(text.format(nr=coursenr, title=coursetitle, crn=crn))
        msg['Subject'] = "[coursenotify] {0} open".format(coursenr)
        msg['From'] = self.sender
        msg['To'] = self.recipient
        self._send(msg)
