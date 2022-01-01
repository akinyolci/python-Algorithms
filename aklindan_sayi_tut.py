from random import shuffle

print("aklından bir sayı tut oyununa hoş geldin\nkaçtan kaça kadar sayılardan alalım yaz")

aralik1=int(input("başlangıç:"))
aralik2=int(input("bitiş:"))
print("{} ve {} sayı aralığın".format(aralik1,aralik2))
aralik=[i for i in range(aralik1,aralik2+1)]

shuffle(aralik)
print("sayıyı tuttuk bu aralıktan\nsence sayı kaç?")
count=3
while count>0:
    tahmin=int(input("Tahmin:"))
    if tahmin==aralik[0]:
        print("doğru bildiniz sayı: {}".format(tahmin))
        break
    else:
        print("yanlış bildiniz, tekrar deneyiniz")
        count-=1
