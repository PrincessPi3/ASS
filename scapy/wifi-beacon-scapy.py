from scapy.all import *

# https://yasoob.me/2018/09/08/sending-sniffing-wlan-beacon-frames-using-scapy/

iface = 'wlan1'
sender = 'c2:13:37:c2:13:37'

def beacon_raw(SSID, length=255):
	dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff', addr2=sender, addr3=sender)
	beacon = Dot11Beacon()
	essid = Dot11Elt(ID='SSID',info=RawVal(SSID), len=length)
	frame = RadioTap()/dot11/beacon/essid
	sendp(frame, iface=iface, inter=0.250, loop=1)
#	sendp(frame, iface=iface, inter=0.100, count=256)

def beacon_normie(SSID):
	dot11 = Dot11(type=0, subtype=8, addr1='ff:ff:ff:ff:ff:ff', addr2=sender, addr3=sender)
	beacon = Dot11Beacon()
	essid = Dot11Elt(ID='SSID',info=SSID, len=len(SSID))
	frame = RadioTap()/dot11/beacon/essid
	print(SSID)
	sendp(frame, iface=iface, inter=0.100, loop=1)
#       sendp(frame, iface=iface, inter=0.100, count=256)

#longgg = "\xFF"*800
#longggg = f"\x00{longgg}\x00"
#beacon_raw(longggg)
SSID = b"YOU-SEEM-FUNDAMETALLY-FUN\x0AI-THINK-ID-LIKE-TO-KNOW-YOU\x0AI-FEEL-LIKE-BEING-YOUR-FRIEND\x0AI-AM-YOUR-PONY-WAIFU"
beacon_raw(SSID)
