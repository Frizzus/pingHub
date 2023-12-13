import sys;
from scapy.all import *;
import logging
logging.getLogger("scapy").setLevel(logging.ERROR)

'''
- ICMP: protocole que les périphériques d'un réseau utilisent pour communiquer les problèmes de transmission de données
- TTL: time to live, correspond à la durée de vie d'un paquet avant qu'il ne soit détruit (nombre de sauts)
'''
TIME_TO_LIVE = 20

def icmp_ping(ip_address: str, ping_number: int = 1) -> bool:
    packet = IP(dst = ip_address)/ICMP()
    print(f"Envoi d'une requête 'Ping' {packet['IP'].dst} :")
    for _ in range(int(ping_number)):
        start_time = time.time()
        response = sr1(packet, timeout=TIME_TO_LIVE)
        end_time = time.time()
        if response:
            response_time = round(end_time - start_time) * 1000
            # response.show()
            print(f"Réponse de {response['IP'].dst}  octets: {response['IP'].len}  temps={response_time} ms  TTL={response['IP'].ttl}\n")
            return True

    return False

def print_usage():
    print("Usage: python script.py <IP_address> <ping_number>")

if len(sys.argv) < 2 or len(sys.argv) > 3:
    print_usage()
else:
    icmp_ping(sys.argv[1]) if len(sys.argv) == 2 else icmp_ping(sys.argv[1], sys.argv[2])
