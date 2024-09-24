import subprocess
import os
# from requests.utils import requote_uri
import urllib.parse
from random import randbytes

host = "http://192.168.4.1"
# host = "http://10.0.0.80"
rangei = 10000
# charlen = 4*400
charlen = 128
curl_cmd = "curl --include --silent --show-error"

for x in range(rangei+1):
	payload = urllib.parse.quote(randbytes(charlen))	
	uri = f"{host}/get?email={payload}&password={payload}"
	command = f"{curl_cmd} '{uri}'"

	print(f"{x} of {rangei} sets of {charlen} random bytes")
	p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()
	p_status = p.wait()

print(f"\n\nThe End")
