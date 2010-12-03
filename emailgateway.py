from smtplib import SMTP, SMTP_SSL

class EmailGateway:
	def __init__(self, from_addr, smtp_host, smtp_port, smtp_tls, smtp_user, smtp_pass):
		self.from_addr = from_addr
		self.smtp_host = smtp_host
		self.smtp_port = smtp_port
		self.smtp_tls = smtp_tls
		self.smtp_user = smtp_user
		self.smtp_pass = smtp_pass

		if self.smtp_tls:
			self.conn = SMTP_SSL(self.smtp_host, self.smtp_port)
		else:
			self.conn = SMTP(self.smtp_host, self.smtp_port)

		self.conn.login(self.smtp_user, self.smtp_pass)

	def send(self, recip, subj, msg_text):
		msg = "From: %s\nTo: %s\nSubject: %s\n\n%s" % (self.from_addr, recip, subj, msg_text)

		self.conn.sendmail(self.from_addr, recip, msg)

	def quit(self):
		self.conn.quit()

