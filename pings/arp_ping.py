from scapy.all import ARP, Ether, srp

def arp_ping(target_ip) -> bool:

    arp_request = Ether(dst="ff:ff:ff:ff:ff:ff") / ARP(pdst=target_ip)

    result = srp(arp_request, timeout=3, verbose=0)[0]

    has_results = False

    for sent, received in result:
        has_results = True  
        print("\nPaquet envoyé:")
        print(sent.summary())
        print("\nPaquet reçu:")
        print(received.summary())
        print("-----------------------------------------")

    if not has_results:
        print("Aucun résultat obtenu pour la requête ARP.")

    devices = []

    for sent, received in result:
        devices.append({'ip': received.psrc, 'mac': received.hwsrc})

    return has_results

# def main():
#     target_ip = input("Entrez l'adresse IP du réseau à scanner : ")
#     devices, has_results = arp_ping(target_ip)

#     if has_results:
#         print("\nRésultats du scan ARP :")
#         print("IP\t\t\tMAC Address")
#         print("-----------------------------------------")

#         for device in devices:
#             print(f"{device['ip']}\t\t{device['mac']}")
#     else:
#         print("Aucun résultat obtenu pour la requête ARP.")

# if __name__ == "__main__":
#     main()
