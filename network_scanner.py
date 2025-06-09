from scapy.all import ARP, Ether, srp
from mac_vendor_lookup import MacLookup
import socket

def scan_network(ip_range):
    # Kirim paket ARP ke IP target
    arp = ARP(pdst=ip_range)
    ether = Ether(dst="ff:ff:ff:ff:ff:ff")
    packet = ether/arp

    print(f"\n[+] Scanning IP Range: {ip_range}\n")
    result = srp(packet, timeout=2, verbose=0)[0]

    mac_lookup = MacLookup()

    print(f"{'IP Address':<16} {'MAC Address':<20} {'Vendor':<25} {'Hostname'}")
    print("="*80)

    for sent, received in result:
        ip = received.psrc
        mac = received.hwsrc

        try:
            vendor = mac_lookup.lookup(mac)
        except:
            vendor = "Unknown"

        try:
            hostname = socket.gethostbyaddr(ip)[0]
        except:
            hostname = "-"

        print(f"{ip:<16} {mac:<20} {vendor:<25} {hostname}")

if __name__ == "__main__":
    # Ganti subnet sesuai jaringan lokal kamu
    subnet = "192.168.1.0/24"
    scan_network(subnet)
