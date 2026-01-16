#1
while True:

    try:
        N = int(input("nhap N = "))
        if 0 < N < 50:
            break
        else:
            print("so N phai nam trong [0-50] ")

    except ValueError :
        print("N pahi la so nguyen duong ! ")

#2
list_N = []
print(f'nhap {N} so thuc ! ')

for i in range(N):

    while True :

        try:
            number = float(input(f'nhap so thu {i} la: '))
            list_N.append(number)
            break

        except ValueError:
            print("cac so trong list phai la so thuc, nhap lai! ")

print(f'list gom N so thuc cua ban la : {list_N}')

#3
print(f'max in list: {max(list_N)}')

#4
print(f'min in list: {min(list_N)}')

#5
so_duong_chan = [i for i in list_N if i > 0 and i.is_integer() and int(i) % 2 == 0]

if so_duong_chan:
    print(f'so duong chan lon nhat la: {max(so_duong_chan)}')

else:
    print("khong tim thay so do! ")

#6
so_am_le = [i for i in list_N if i < 0 and i.is_integer() and int(i) % 2 != 0]

if so_am_le:
    print(f'so am le nho nhat la: {min(so_am_le)}')

else:
    print("khong tim thay so do! ")

#7
print("cac so chinh phuong trong list cua ban la ")

for number in list_N:

    if number >=0 and number.is_integer():
        i = 0

        while i**2 <= number:
            if i**2 == number:
                print(number)
                break

            i += 1        

#8
sum = 0

for number in list_N:
    sum += number

print(f'tong list la: {round(sum, 2)}')

#9
average = round(sum / N, 2)
print(f'trung binh cong cua list la; {average}')

#10
numbers = [number for number in list_N if number.is_integer() and number > average]

if numbers:
    print(f'cac so lon hon so trung binh cong cua list la: {numbers}')

else:
    print("khong tim thay cac so do! ")

#11
list_N.sort()

print(f'list tang dan la: {list_N}')

#12
list_N.reverse()

print(f'list giam dan la: {list_N}')