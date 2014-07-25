#!/bin/python

import ConfigParser
import subprocess
from flask import Flask
from datetime import datetime
from time import sleep
import os

app = Flask(__name__)

@app.route("/snap")
def snap():
	dateFormat = "%Y%m%d-%H%M%S"
	dateString = datetime.now().strftime(dateFormat)
	fileName = config.get('Directories', 'photos') + os.sep + "img-" + dateString + ".jpg"

	subprocess.call(["gphoto2", "--capture-image-and-download", "--filename=%s" % (fileName)])

	sleep(10)

def setupNetwork():
	extConfig = ConfigParser.ConfigParser()
	extConfig.readfp(open(config.get('ExternalConfig', 'path')))
	networkMode = extConfig.get('Network', 'mode')

	if networkMode == 'static':
		networkIp = extConfig.get('Network', 'ip')
		subprocess.call(['ifconfig', 'en4', networkIp])

def setupDirectories():
	try:
		os.mkdir(config.get('Directories', 'photos'))
	except:
		pass

if __name__ == "__main__":
	config = ConfigParser.ConfigParser()
	config.readfp(open('settings.config'))
	setupNetwork()
	setupDirectories()
	# app.debug = True
	app.run(host='0.0.0.0')