# 1. Computer ke dimaag mein Router ka ASLI permanent pata pehle se safe hai
router_asli_mac = "AA-BB-CC-DD-EE-FF"

# 2. Hamari live network diary (ARP Table) jisme abhi sab sahi chal raha hai
current_arp_table = {"192.168.1.1": "AA-BB-CC-DD-EE-FF"}
print("📁 Network Status: Sab kuch normal chal raha hai.")

# -------------------------------------------------------------
# 🚨 STEP 1: HACKER NE ATTACK KIYA (Jhoota Address Bheja)
# -------------------------------------------------------------
hacker_fake_mac = "99-99-99-99-99-99"

# Hacker ne diary mein router ke samne apna jhoota pata daal diya
current_arp_table["192.168.1.1"] = hacker_fake_mac
print("\n💥 Hacker ne network par jhoota address inject kar diya!")

# -------------------------------------------------------------
# 🛡️ STEP 2: AUTOMATIC DETECTION (Computer Apne Aap Check Karega)
# -------------------------------------------------------------
# Computer live diary se pata nikalega aur asli pate se match karega
current_mac_in_diary = current_arp_table["192.168.1.1"]

if current_mac_in_diary != router_asli_mac:
  # Agar match nahi hua, toh computer APNE AAP alert dega! 🛑
    print("\n🚨 REAL-TIME ALERT: Dushman ne jhoot bola! ARP Table spoofing pakdi gayi!")
    print(f"⚠️ Kharaab Address Jo Diary Mein Mila: {current_mac_in_diary}")
else:
    print("\n✅ Verification Success: No attack detected.")

OUTPUT:
📁 Network Status: Sab kuch normal chal raha hai.

💥 Hacker ne network par jhoota address inject kar diya!

🚨 REAL-TIME ALERT: Dushman ne jhoot bola! ARP Table spoofing pakdi gayi!
⚠️ Kharaab Address Jo Diary Mein Mila: 99-99-99-99-99-99
Use code with caution.
