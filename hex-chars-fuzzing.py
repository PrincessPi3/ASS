import datetime
import subprocess
import time

# host = "10.0.0.80"
host = "192.168.4.1"

rangei = 65536 # FFFF+1

currenttime = datetime.datetime.now()
datestamp = currenttime.strftime("%d%m%Y-%H.%M.%S")

for x in range(rangei):
	hexcode = hex(x)[2:]
	if x > 255:
		urlformatted_raw = "%{:04x}".format(x)
		hexformatted_raw = "0x{:04x}".format(x)
		urlformatted = f"{urlformatted_raw[:3]}%{urlformatted_raw[3:]}"
	else:
		urlformatted_raw = "%{:04x}".format(x)
		urlformatted = "%{:02x}".format(x)
		hexformatted = "0x{:02x}".format(x)
	unicode_formatted = "%u{:04x}".format(x)
	printformatted = f"\\x{hexcode}"

	print(f"Running {urlformatted} and {urlformatted_raw} and {unicode_formatted}")
	p = subprocess.Popen(f"curl -i -s -S 'http://{host}/get?email=email{urlformatted}email&password=password{urlformatted}password' >> fuzzing-results/urlformatted-{rangei}-{datestamp}.txt", stdout=subprocess.PIPE, shell=True)
	p1 = subprocess.Popen(f"curl -i -s -S 'http://{host}/get?email=email{urlformatted_raw}email&password=password{urlformatted_raw}password' >> fuzzing-results/urlformatted_raw-{rangei}-{datestamp}.txt", stdout=subprocess.PIPE, shell=True)
	p2 = subprocess.Popen(f"curl -i -s -S 'http://{host}/get?email=email{unicode_formatted}email&password=password{unicode_formatted}password' >> fuzzing-results/unicode_formatted-{rangei}-{datestamp}.txt", stdout=subprocess.PIPE, shell=True)

	(output, err) = p.communicate()
	(output, err) = p1.communicate()
	(output, err) = p2.communicate()

	p_status = p.wait()
	p_status1 = p1.wait()
	p_status2 = p2.wait()

	time.sleep(0.225)
print(f"\n\nlog written to fuzzing-results/X-{rangei}-{datestamp}.txt")
