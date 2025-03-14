# Kullanıcıdan metin almak ve dosyaya yazmak
def yaz_dosya():
    # Kullanıcıdan metin girişi almak
    metin = input("Metninizi girin: ")

    # Dosyaya yazma işlemi
    with open('metin_dosyasi.txt', 'w') as dosya:
        dosya.write(metin)

# Dosyayı okuyarak içeriğini yazdırmak
def oku_dosya():
    # Dosyayı okuma işlemi
    with open('metin_dosyasi.txt', 'r') as dosya:
        icerik = dosya.read()
        print("Dosya içeriği:")
        print(icerik)

# Kullanıcıdan 5 farklı satır verisini almak ve dosyaya yazmak
def yaz_satislar():
    with open('satislar.txt', 'w') as dosya:
        for i in range(5):
            satir = input(f"{i+1}. satırı girin: ")
            dosya.write(satir + "\n")

# Dosyadaki verileri satır satır okuyarak yazdırmak
def oku_satislar():
    with open('satislar.txt', 'r') as dosya:
        print("Dosyadaki veriler:")
        for satir in dosya:
            print(satir.strip())

# Ana fonksiyon
def main():
    # İlk olarak metin dosyasını yazıp oku
    yaz_dosya()
    oku_dosya()

    # Şimdi 5 satır verisini alıp dosyaya yaz
    yaz_satislar()
    
    # Son olarak bu verileri satır satır oku ve yazdır
    oku_satislar()

# Programı çalıştırma
if __name__ == "__main__":
    main()
