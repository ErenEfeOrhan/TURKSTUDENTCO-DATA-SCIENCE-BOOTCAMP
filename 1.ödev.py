#1.soru  Kullanıcıdan iki sayı alarak bu sayıları toplayan bir programın kodunu yazın
# Kullanıcıdan iki sayı al
sayi1 = float(input("Birinci sayıyı girin: "))
sayi2 = float(input("İkinci sayıyı girin: "))

# Sayıları topla
toplam = sayi1 + sayi2

# Sonucu ekrana yazdır
print("Toplam:", toplam)

#2.soru 1'den 100'e kadar olan sayıları toplayan bir programın kodunu yazın
# 1'den 100'e kadar olan sayıları topla
toplam = 0
for sayi in range(1, 101):
    toplam += sayi

# Sonucu ekrana yazdır
print("1'den 100'e kadar olan sayıların toplamı:", toplam)

#3.soru Kullanıcıdan alınan bir sayının asal olup olmadığını bulan bir programın kodunu yazın.
# Kullanıcıdan bir sayı al
sayi = int(input("Bir sayı girin: "))

# Sayının asal olup olmadığını kontrol et
if sayi > 1:
    for i in range(2,sayi):
        if sayi % i == 0:
            print(f"{sayi} asal bir sayı değildir.")
            break
    else:
        print(f"{sayi} asal bir sayıdır.")
else:
    print(f"{sayi} asal bir sayı değildir.")

#4.soru : Bir dizideki (array) elemanların tekrar edip etmediğini kontrol eden bir programın kodunu yazın.
def tekrar_var_mi(dizi):
    for i in range(len(dizi)):
        for j in range(i + 1, len(dizi)):
            if dizi[i] == dizi[j]:
                return True
    return False

# Kullanıcıdan dizi elemanlarını al
dizi = [int(x) for x in input("Dizi elemanlarını boşlukla ayırarak girin: ").split()]

# Tekrar eden eleman olup olmadığını kontrol et
if tekrar_var_mi(dizi):
    print("Dizide tekrar eden elemanlar var.")
else:
    print("Dizide tekrar eden elemanlar yok.")

