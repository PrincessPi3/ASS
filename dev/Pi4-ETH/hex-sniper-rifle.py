import datetime
import subprocess
import time

host = "http://10.0.0.80"
# host = "http://192.168.4.1"
charlen = 1489
char = "%00"
prepend = ""
append = ""

currenttime = datetime.datetime.now()
datestamp = currenttime.strftime("%d%m%Y-%H.%M.%S")

outfile = f"fuzzing-results/hex-sniper-rifle-{datestamp}.txt"

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

chars = char*charlen
payload = f"{prepend}{chars}{append}"
uri = f"{host}/get.php?email={payload}&password=holdstill"
command = f"{curl_cmd} '{uri}' >> {outfile}"
print(f"\n\nRunning {char}*{charlen} on email\nPrepend: {prepend}\nAppend: {append}\nOutfile: {outfile}")
with open(outfile, "a") as log:
	log.write(f"\n\nChars: {char}*{charlen} - Prepend: {prepend} - Append: {append}\n")
p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()

print(f"\n\nlog written to {outfile}")
