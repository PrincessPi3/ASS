from boofuzz import *
import datetime
import time

def main():
	port = 80
	# host = '10.0.0.80'
	host = '192.168.4.1'
	file_tag = 'Marauder-CYD'
	# web_interface_listen='0.0.0.0'
	web_interface_listen='10.0.0.79'
	web_interface_listen_port=26000
	currenttime = datetime.datetime.now()
	ct = currenttime.strftime("%d%m%Y-%H.%M.%S")
	output_filename=f"./boofuzz-results/{file_tag}-{ct}.db"
	session_persistsant_filename=f"./boofuzz-results/session-save-{file_tag}-{ct}.dat"
	
	session = Session(
		target=Target(connection=TCPSocketConnection(host, port)),
		receive_data_after_fuzz=True,
		web_address=web_interface_listen,
		web_port=web_interface_listen_port,
		db_filename=output_filename,
		session_filename=session_persistsant_filename,
		sleep_time=0.225
		)
	
	s_initialize(name="Request")
	with s_block("Request-Line"):
		s_group("http-method", ["GET", "HEAD", "POST"])
		s_static(" ", "space-0")
		s_static("/get?email=", name="uri-start")
		s_string("email", name="emailvar")
		s_static("&password=", name="password")
		s_string("password", name="passwordvar")
		s_static(" ", "space-1")
		s_static("HTTP/1.1", "http-version")
		s_static("\r\n\r\n", "Request-CRLF")

	session.connect(s_get("Request"))
	session.fuzz()


if __name__ == "__main__":
    main()
