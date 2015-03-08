import re 
import os
import urllib
import urllib2

######################################
#Change these settings
######################################
name='OpenHAB' # Whatever you want your device name to be
localip='YOUR_LOCAL_IP' #Put your local static IP here
key='YOUR_AUTOREMOTE_KEY' #Found by going to your custom Autoremote URL and then copying it out of the URL box

#######################################
#Do not modify below this line
#######################################

name = urllib.quote_plus(name)
ipreq=urllib2.Request("http://ipecho.net/plain")
ipres=urllib2.urlopen(ipreq)
ipdata = ipres.read()
publicip=ipdata

def autoremote_reg():
	req=urllib2.Request('http://autoremotejoaomgcd.appspot.com/registerpc?key={0}&name={1}&id=homepi&type=linux&publicip={2}&localip={3}&id={4}'.format(key,name,publicip,localip,name))
	res=urllib2.urlopen(req)
	data=res.read()

def autoremote_send(message):
	message = urllib.quote_plus(message)
	req=urllib2.Request('https://autoremotejoaomgcd.appspot.com/sendmessage?key={0}&message={1}&sender={3}'.format(key,message,name))
	res=urllib2.urlopen(req)
	data=res.read()

if __name__ == "__main__":
	import sys
	#If there were no arguments supplied, we want to register the PC with Autoremote
	if len(sys.argv) == 1:
		autoremote_reg()
		exit()
		
	#otherwise we want to send a message!
	else:
		message = sys.argv[1]
		autoremote_send(message)
		exit()
