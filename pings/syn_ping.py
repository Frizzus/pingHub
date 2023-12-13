import logging
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.all import *

def reset_half_open(ip_address, ports):
    sr(IP(dst=ip_address)/TCP(dport=ports, flags='AR'), timeout=1)


def syn_ping(ip_address:str, ports, timeout=0.2):

    results = {port:None for port in ports}
    to_reset = []
    syn_packet = IP(dst=ip_address)/TCP(dport=ports,flags='S')
    answers, un_answered = sr(syn_packet, timeout=timeout)
    for req, resp in answers:
        if not resp.hashlayer(TCP):
            continue
        tcp_layer = resp.getlayer(TCP)
        if tcp_layer.flags == 0x12:
            to_reset.append(tcp_layer.sport)
            results[tcp_layer.sport] = True
        elif tcp_layer.flags == 0x14:
            results[tcp_layer.sport] = False

    reset_half_open(ip_address, to_reset)
    return results


def chunks(l, n):
    for i in range(0, len(l), n):
        yield l[i:i + n]


if __name__ == '__main__':

    ip_address = "127.0.0.1" #TEMPORAIRE POUR TEST

    conf.verb = 0
    print("Start scanning Host %s" % ip_address)
    for ports in chunks(range(1, 1024), 100):
        for port in ports:
            results = syn_ping(ip_address, ports)
            for syn_packet, r in results.items():
                print(syn_packet, ':', r)
    print("%s Scan completed" % ip_address)