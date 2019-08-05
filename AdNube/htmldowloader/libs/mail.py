# python imports
import logging
import datetime

# django level imports
from django.core.mail import EmailMessage

# project imports
from htmldowloader.settings import EMAIL_HOST_USER


logger = logging.getLogger(__name__)

def sendmail(message,subject,tolist):
	try:
		msg = EmailMessage(subject, message, EMAIL_HOST_USER, tolist) 
		msg.attach_file('folder.zip')
		msg.send()
		logger.info("Mail Sent ")
		return 1
	except:
		logger.error("Sending mail is failed", exc_info=True)
		return 0


