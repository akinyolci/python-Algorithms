birler={"1":"bir", "2":"iki", "3":"üç","4":"dört","5":"beş","6":"altı","7":"yedi","8":"sekiz","9":"dokuz"}
onlar={"1":"on","2":"yirmi","3":"otuz","4":"kırk","5":"elli","6":"altmış","7":"yetmiş","8":"seksen","9":"doksan"}

def okunus(sayi):
        if (len(sayi)==2):
            a=onlar[sayi[0]]
            b=birler[sayi[1]]
        else:
            print("lütfen girdiğiniz sayının 2 basamaklı olmasına dikkat edin.")
        return(a+' '+b)
while True:
    sayi = input("sayı:")
    if sayi == "q":
        print("sistemden çıkış yapıldı.")
        break
    else:
        print(okunus(sayi))

#2.yol
"""
birler =  ["","Bir","İki","Üç","Dört","Beş","Altı","Yedi","Sekiz","Dokuz"]
onlar = ["","On","Yirmi","Otuz","Kırk","Elli","Altmış","Yetmiş","Seksen","Doksan"]

def okunus(sayi):
    on=sayi//10
    bir=sayi%10
    return onlar[on]+" "+birler[bir]
sayi=int(input("sayi:"))
print(okunus(sayi))

"""