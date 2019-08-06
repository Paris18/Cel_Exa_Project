# python imports
import logging
import urllib.request,shutil,os
from celery import shared_task

# Project level import
from .mail import sendmail


urlstr = ["https://","www.",".com",".co","in","/","."]
logger = logging.getLogger(__name__)

def namestr(url):
	for i in urlstr:
		url = url.replace(i,"")
	return url

def dowloadhtml(url):
	htmlfile = urllib.request.urlopen(url)
	htmltext = htmlfile.read()
	nameu = namestr(url)
	f = open('folder/'+nameu+'.html', 'wb')
	f.write(htmltext)
	f.close()
	return 1

@shared_task
def runtask(data):
	try:
		if not os.path.exists('folder'):
			os.mkdir('folder')
		for i in data["urls"]:
			dowloadhtml(i)
		shutil.make_archive('folder', 'zip', 'folder')
		sendmail('PFA for zipped file of html',"html downloader",[data["email"]])
		shutil.rmtree('folder')
		os.remove('folder.zip')
	except:
		logger.error("Sending mail is failed", exc_info=True)







	