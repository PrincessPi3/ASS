from scapy.all import *
import urllib.parse
#from random import randbytes
import random

iface = 'wlan1'
sender = 'ac:cb:12:ad:58:27'

def sendProbe(SSID, repeat=3, interval=0.100):
	dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff',
	addr2=sender, addr3=sender)
	beacon = Dot11Beacon()
	essid = Dot11Elt(ID='SSID',info=SSID, len=len(SSID))
	frame = RadioTap()/dot11/beacon/essid
	sendp(frame, iface=iface, inter=interval, count=repeat)

def sendProbeRaw(SSID, repeat=1, interval=0.200, listedLen=255):
        dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff',
        addr2=sender, addr3=sender)
        beacon = Dot11Beacon()
        essid = Dot11Elt(ID='SSID',info=RawVal(SSID), len=listedLen)
        frame = RadioTap()/dot11/beacon/essid
        sendp(frame, iface=iface, inter=interval, count=repeat)

def sendRandBytesBeacons(numOfBeacons=200, lenOfSSIDs=20, repeat=3, interval=0.100):
	for i in range(numOfBeacons):
		SSID = randbytes(lenOfSSIDs)
		urlEncoded = urllib.parse.quote(SSID)
		print(f"\n{i} of {numOfBeacons}\n\tRepeats: {repeat}\n\tLength: {lenOfSSIDs}\n\tSSID: {urlEncoded}\n")
		sendProbe(SSID, repeat, interval)

def sendProbeFuzz(repeat=1, interval=0.150):
	randMAC = '6e:07:9e:96:2b:4e'
	# randMAC = RandMAC()
	randLen = RandNum(0, 255)
	randSSIDLen = random.randint(0,255)
	randSSIDBytes = random.randbytes(randSSIDLen)
	urlEncoded = urllib.parse.quote(randSSIDBytes)

	dot11 = Dot11(type=0,
		subtype=8,
		addr1='ff:ff:ff:ff:ff:ff', # dst set to broadcast
		addr2=randMAC, # random source
		addr3=randMAC) # random bssid
	
	beacon = Dot11Beacon()
	
	essid = Dot11Elt(ID='SSID',
		info=RawVal(randSSIDBytes),
		len=RawVal(randLen))
	
	frame = RadioTap()/dot11/beacon/essid
	
	print(f"src={randMAC}, dst=ff:ff:ff:ff:ff:ff, BSSID={randMAC}\n\tSSID Set Length: {randLen}\n\tActual SSID Length: {randSSIDLen}\n\tSSID: {urlEncoded}")
	sendp(frame, iface=iface, inter=interval, count=repeat)

def sendFuzzBeacons(numOfBeacons=200,
	repeat=1,
	interval=0.150):
	
	for i in range(numOfBeacons):
		print(f"\n{i} of {numOfBeacons}")
		sendProbeFuzz()

def sendRandBytesBeaconsRaw(
	numOfBeacons=200,
	lenOfSSIDs=256,
	listedLen=255,
	repeat=1,
	interval=0.2):
	
	for i in range(numOfBeacons):
		SSID = random.randbytes(lenOfSSIDs)
		urlEncoded = urllib.parse.quote(SSID)
		print(f"\n{i} of {numOfBeacons}\n\tRepeats: {repeat}\n\tListed Length: {listedLen}\n\tReal Length: {lenOfSSIDs}\n\tInterval: {interval} Seconds\n\tSSID: {urlEncoded}")
		sendProbeRaw(SSID, repeat, interval, listedLen)



#sendRandBytesBeaconsRaw(numOfBeacons=100, lenOfSSIDs=1, listedLen=255, repeat=3, interval=0.15)
#sendRandBytesBeacons(100, 20, 5, 0.1)


def fullFuzz(
	numOfBeacons=200,
	repeat=3,
	interval=0.150):

	for i in range(numOfBeacons):
		realLenSSID = random.randint(0,255)
		SSID = random.randbytes(realLenSSID)
		urlEncoded = urllib.parse.quote(SSID)
		fakeLenSSID = random.randint(0,255)
		senderMAC = RandMAC()

		dot11 = Dot11(type=0, subtype=8,
				addr1='ff:ff:ff:ff:ff:ff',
				addr2=senderMAC,
				addr3=senderMAC)
		
		beacon = Dot11Beacon()

		essid = Dot11Elt(ID='SSID',
				   info=SSID,
				   len=fakeLenSSID)
					
		frame = RadioTap()/dot11/beacon/essid
		
		print(f"\n{i}/{numOfBeacons}\n\tEach Repeats: {repeat}\n\tReal Length: {realLenSSID}\n\tFake Length: {fakeLenSSID}\n\tSender MAC: {senderMAC}\n\tSSID: {urlEncoded}\n")

		sendp(frame, iface=iface, inter=interval, count=repeat)

fullFuzz()