from random import randrange
s = randrange(1,10) # xuat ngau nhien tu 1 den 199
doan = int(input("nhap so ban doan vao day : "))
while doan != s :
    if doan > s :
        print(doan,"lon hon ket qua roi ")
    if doan < s :
        print(doan,"nho hon ket qua roi ")
    doan = int(input("doan lai di : "))
print(f"ban da doan dung so {doan}")