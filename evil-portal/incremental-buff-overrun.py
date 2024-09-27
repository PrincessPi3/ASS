import datetime
import subprocess
import time

# host = "http://10.0.0.80"
# host = "http://192.168.4.1"
host = "http://172.0.0.1"
rangei = 10000
char = "%00%FF"
# char = "%00"
prepend = ""
append = ""
#append = "%0a%00%0a"

currenttime = datetime.datetime.now()
datestamp = currenttime.strftime("%d%m%Y-%H.%M.%S")

outfile = f"fuzzing-results/chars-{rangei}-{datestamp}.txt"

# -i, --include - include header in output
# -I, --head - HEAD http method
# -s, --silent - supresses progress and errors
# -S, --show-error - when used with -s/--silent, displays errors
# -D <file>, --dump-header <file> - saves response headers to <file>
# -f, --fail - fail silently on HTTP error
# -X, --request - request method, defaults to GET
# -H <header:value>, --header <header:value> - sets header, multiple are allowed 
# -v, --verbose - show request headers
# -o <file>, --output <file> - write output to file

# curl_cmd = "curl -i -s -S -v"
curl_cmd = "curl --include --silent --show-error"

for x in range(rangei+1):
	chars = char*x
	payload = f"{prepend}{chars}{append}"
	uri = f"{host}/get?email={payload}&password={payload}"
	command = f"{curl_cmd} '{uri}' >> {outfile}"
	print(f"Running {x}/{rangei} chars ({char})\n\tPrepend: {prepend}\n\tAppend: {append}\nOutfile: {outfile}\n")
	with open(outfile, "a") as log:
		log.write(f"\n\n{x}/{rangei} - Char: {char} - Prepend: {prepend} - Append: {append}\n")
	p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
	(output, err) = p.communicate()
	p_status = p.wait()

print(f"\n\nlog written to {outfile}")
