def asal(n):
    count = 2
    for i in range(2, n):
        if n % i != 0:
            count += 1
    if count == n:
        return True
    elif n == 2:
        return True
    else:
        return False

while True:
    n = input("n:")
    if n == "q":
        print("çıkış yapıldı")
        break
    else:
        n = int(n)
    if asal(n):
        print("{} bir asal sayıdır".format(n))
    else:
        print("{} bir asal sayı değildir.".format(n))
