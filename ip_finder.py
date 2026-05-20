import socket

print("🌐 Sayt IP Manzilini Topuvchi Dastur\n")
sayt = input("Sayt nomini kiriting (masalan: google.com yoki instagram.com): ")

# Link boshidagi ortiqcha narsalarni tozalash
sayt_toza = sayt.replace("https://", "").replace("http://", "").replace("www.", "").split("/")[0]

try:
    print(f"⏳ {sayt_toza} tekshirilmoqda...")
    ip_manzil = socket.gethostbyname(sayt_toza)
    print("-" * 40)
    print(f"🚀 Sayt nomi: {sayt_toza}")
    print(f"📍 IP Manzili: {ip_manzil}")
    print("-" * 40)
except socket.gaierror:
    print("❌ Sayt topilmadi yoki internetga ulanmagansiz! Nomini tekshirib qaytadan yozing.")