from scapy.all import *

def xmas_ping(ip_address:str) -> bool:
    packet = IP(dst= ip_address)/TCP(dport= 23, flags=63)
    ans = sr1(packet, timeout=1)
    print(packet)
    if ans != None:
        return True
    else:
        return False

# print(xmas_ping("192.168.1.1/24"))
