# 🕵️‍♂️ Network Scanner dengan Python + Scapy

Skrip ini digunakan untuk melakukan pemindaian jaringan lokal menggunakan protokol ARP. Hasil pemindaian mencakup:

- IP Address  
- MAC Address  
- Vendor (berdasarkan MAC)  
- Hostname (jika tersedia)

Cocok digunakan untuk memantau perangkat aktif di jaringan lokal, atau sebagai bagian dari pembelajaran dasar ethical hacking dan networking.

---

## 📋 Fitur

✅ Pemindaian jaringan lokal via ARP  
✅ Resolusi hostname secara otomatis  
✅ Identifikasi vendor perangkat menggunakan MAC address  
✅ Output rapi dan mudah dibaca  

---

## 📦 Dependencies

Sebelum menjalankan skrip, pastikan kamu sudah menginstall pustaka berikut:

```bash
pip install scapy mac-vendor-lookup

subnet = "192.168.1.0/24"  # Ganti dengan subnet jaringan lokalmu

jalankan
sudo python network_scanner.py


contoh output
[+] Scanning IP Range: 192.168.1.0/24

IP Address       MAC Address          Vendor                   Hostname
================================================================================
192.168.1.1      84:0d:8e:ab:cd:ef    TP-Link Technologies     router.local
192.168.1.12     58:ef:68:12:34:56    Xiaomi Communications    android-8f1a2b3c
192.168.1.15     44:65:0d:de:ad:be    Unknown                  -
