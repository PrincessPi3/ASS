from scapy.all import *
import urllib.parse
from random import randbytes

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

def sendRandBytesBeaconsRaw(
	numOfBeacons=200,
	lenOfSSIDs=256,
	listedLen=255,
	repeat=1,
	interval=0.2):
	
	for i in range(numOfBeacons):
		SSID = randbytes(lenOfSSIDs)
		urlEncoded = urllib.parse.quote(SSID)
		print(f"\n{i} of {numOfBeacons}\n\tRepeats: {repeat}\n\tListed Length: {listedLen}\n\tReal Length: {lenOfSSIDs}\n\tInterval: {interval} Seconds\n\tSSID: {urlEncoded}")
		sendProbeRaw(SSID, repeat, interval, listedLen)

sendRandBytesBeaconsRaw(numOfBeacons=100, lenOfSSIDs=1, listedLen=255, repeat=3, interval=0.15)
#sendRandBytesBeacons(100, 20, 5, 0.1)
