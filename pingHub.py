import scapy, argparse
# import pings.icmp_ping as icmp
import pings.arp_ping as arp
# import pings.syn_ping as syn
import pings.xmas_ping as xmas

'''
quelqu'un pour faire le CLI (loïc)

quel types de ping :
- echo ICMP (bapt)
- ARP (ben)
- SYN (arthur)

def mon_ping(address:string) -> boolean
'''

parser = argparse.ArgumentParser(
    prog= "Ping HUB",
    description= "Simple tool for using different pinging type",
)
parser.add_argument(
    "ip_address",
    help= "The ip address the programme will try to ping"
)
parser.add_argument(
    "-t",
    "--type",
    choices= ["ICMP", "ARP", "SYN", "XMAS"],
    help= "The ping type for this ping (ICMP ping by default)",
    default= "ICMP",
)
parser.add_argument(
    "-n",
    "--number_request",
    help= "The number of ping request launched to the ip address",
    default= 4
)

def ping_range(ips:list[str], nb_ping:int):
    ping_result:bool
    for ip in ips:
        match args.type:
            case "ICMP":
                for i in range(nb_ping):
                    ping_result = icmp.icmp_ping(ip)
                    print("Pinging successful !") if ping_result else print("No reply :(")
            case "ARP":
                for i in range(nb_ping):
                    ping_result = arp.arp_ping(ip)
                    print("Pinging successful !") if ping_result else print("No reply :(")
            case "SYN":
                for i in range(nb_ping):
                    ping_result = syn.syn_ping(ip)
                    print("Pinging successful !") if ping_result else print("No reply :(")
            case "XMAS":
                for i in range(nb_ping):
                    ping_result = xmas.xmas_ping(ip)
                    print("Pinging successful !") if ping_result else print("No reply :(")
            case _ :
                raise NotImplementedError

args = parser.parse_args()
splited:str
second_part:str
ip_part:str
if '/' in args.ip_address:
    print('/')
    splited = args.ip_address.split('/')
    ip_part = splited[0]
    second_part = splited[1]
elif '-' in args.ip_address:
    print('-')
    splited = args.ip_address.split('-')
    ip_part = splited[0]
    second_part = splited[1]
    addresses:list[str] = []
    if int(second_part) < 256 and int(second_part) >= 0:
        for end_addr in range(int(second_part)):
            split_addr = ip_part.split(".")[0:3]
            split_addr.append(str(end_addr))
            new_addr:str = ""
            for part in split_addr:
                new_addr += part + "."
            addresses.append(new_addr)
        ping_range(addresses, int(args.number_request))
else:
    ping_range([args.ip_address], args.number_request)
