import math

def toplama(x, y):
    return x + y

def cikarma(x, y):
    return x - y

def carpma(x, y):
    return x * y

def bolme(x, y):
    return x / y

def us_alma(x, y):
    return x ** y

def mod_alma(x, y):
    return x % y

def kok_alma(x):
    return math.sqrt(x)

def log_alma(x):
    return math.log10(x)

def faktoriyel(x):
    if x == 0:
        return 1
    elif x < 0:
        print("Negatif sayıların faktoriyeli bulunamaz!")
        return None
    else:
        return math.factorial(x)

print("Aşırı Gelişmiş Hesap Makinesi")

while True:
    print("\nLütfen yapmak istediğiniz işlem kategorisini seçin:")
    print("1 - Basit İşlemler (Toplama, Çıkarma, Çarpma, Bölme)")
    print("2 - Gelişmiş İşlemler (Üs Alma, Mod Alma, Kök Alma, Log Alma, Faktöriyel)")
    print("3 - Çıkış")

    kategori_secim = int(input("Seçiminizi yapın: "))

    if kategori_secim == 3:
        print("Çıkış yapılıyor...")
        break

    if kategori_secim < 1 or kategori_secim > 3:
        print("Geçersiz seçim! Lütfen tekrar deneyin.")
        continue

    if kategori_secim == 1:
        print("\nBasit İşlemler Kategorisi:")
        print("1 - Toplama")
        print("2 - Çıkarma")
        print("3 - Çarpma")
        print("4 - Bölme")

        secim = int(input("Seçiminizi yapın: "))

        if secim < 1 or secim > 4:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")
            continue

        num1 = float(input("Birinci sayıyı girin: "))
        num2 = float(input("İkinci sayıyı girin: "))

        if secim == 1:
            print("Sonuç: ", toplama(num1, num2))
        elif secim == 2:
            print("Sonuç: ", cikarma(num1, num2))
        elif secim == 3:
            print("Sonuç: ", carpma(num1, num2))
        elif secim == 4:
            if num2 != 0:
                print("Sonuç: ", bolme(num1, num2))
            else:
                print("Sıfıra bölme hatası!")

    elif kategori_secim == 2:
        print("\nGelişmiş İşlemler Kategorisi:")
        print("1 - Üs Alma")
        print("2 - Mod Alma")
        print("3 - Kök Alma")
        print("4 - Log Alma")
        print("5 - Faktoriyel Hesaplama")

        secim = int(input("Seçiminizi yapın: "))

        if secim < 1 or secim > 5:
            print("Geçersiz seçim! Lütfen tekrar deneyin.")
            continue

        if secim == 1 or secim == 2:
            num1 = float(input("Birinci sayıyı girin: "))
            num2 = float(input("İkinci sayıyı girin: "))

            if secim == 1:
                print("Sonuç: ", us_alma(num1, num2))
            elif secim == 2:
                print("Sonuç: ", mod_alma(num1, num2))
        else:
            num = float(input("Bir sayı girin: "))

            if secim == 3:
                print("Sonuç: ", kok_alma(num))
            elif secim == 4:
                print("Sonuç: ", log_alma(num))
            elif secim == 5:
                print("Sonuç: ", faktoriyel(num))
