n = input("n:")
sayininbasamagi = len(n)
b = list(n)
toplam = 0
for eleman in b:
    eleman = int(eleman)
    toplam += eleman ** sayininbasamagi
if toplam == (int(n)):
    print("bu sayı armstong sayısıdır.")
else:
    print("bu sayı armstong sayısı değildir.")




"""
sayı = input("Sayı:")
basamak_sayisi = len(sayı)
sayı = int(sayı)
basamak = 0
toplam = 0

gecici_sayı = sayı
while (gecici_sayı > 0):
    basamak = gecici_sayı % 10
    toplam += basamak ** basamak_sayisi
    gecici_sayı //= 10
if (toplam == sayı):
    print(sayı, "bir armstrong sayısıdır.")
else:
    print(sayı, "bir armstrong sayısı değildir.")
"""