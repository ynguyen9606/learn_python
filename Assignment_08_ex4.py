#1
def input_num():
    while True:
        try:
            num = int(input("nhap so: "))

            if num > 0 and num < 50:
                return num
            
            else:
                print("phai nhap 1 so nguyen (0 < N < 50)")

        except ValueError:
            print("Sai dinh dang, nhap lai: ")

#2
def input_list(num):
    list_num = []

    print(f'nhap {num} so thuc: ')

    for i in range(num):
        while True :
            try:
                number = float(input(f'nhap so thu {i} la: '))
                list_num.append(number)
                break

            except ValueError:
                print("cac so trong list phai la so thuc, nhap lai! ")

    print(f'list gom N so thuc cua ban la : {list_num}')
    return list_num

#3
def max_in_list(list_num):
    print(f'max in list: {max(list_num)}')

#4
def min_in_list(list_num):
    print(f'min in list: {min(list_num)}')

#5
def max_int_positive(list_num):
    max_value = 0
    found = False

    for i in list_num:
        if i.is_integer() and i > 0 and i % 2 == 0:
            if i > max_value:
                max_value = i
                found = True

    if found:
        print("max so nguyen duong chan:", max_value)
    else:
        print("Khong co so nguyen duong chan")


#6
def min_int_negative(list_num):
    min_value = 0
    found = False

    for i in list_num:
        if i.is_integer() and i < 0 and i % 2 != 0:
            if (not found) or i < min_value:
                min_value = i
                found = True

    if found:
        print("min so nguyen am le:", min_value)
    else:
        print("Khong co so nguyen am le")

#7
def square_num(list_num):
    print("cac so chinh phuong trong list cua ban la ")

    for number in list_num:

        if number >=0 and number.is_integer():
            i = 0

            while i**2 <= number:
                if i**2 == number:
                    print(number)
                    break

                i += 1 

#8
def sum_list(list_num):
    sum = 0
    for num in list_num:
        sum += num
    
    return sum

#9
def average_list(list_num):
    N = len(list_num)
    sum = sum_list(list_num)
    average = round(sum / N, 2)
    return average

#10
def larger_than_average(list_num):
    average = average_list(list_num)
    larger_number = [i for i in list_num if i > average]

    if larger_number:
        print(f'cac gia tri lon hon trung binnh cong cua list la: {larger_number}')
        return larger_number
    else:
        print("khong co gia tri nao lon hon trung binnh cong cua list ")

#11
def list_sort(list_num):   #quick sort
    if len(list_num) <= 1:
        return list_num
    
    pivot = list_num[-1]
    
    left = [x for x in list_num[:-1] if x <= pivot]
    right = [x for x in list_num[:-1] if x > pivot]
    
    new_list = list_sort(left) + [pivot] + list_sort(right)

    return new_list

#12
def decrease(list_num):
    list_num.sort(reverse=True)
    print("sap xep list giam dan la: ",list_num)

num = input_num()
list_num = input_list(num)
max_in_list(list_num)
min_in_list(list_num)
max_int_positive(list_num)
min_int_negative(list_num)
square_num(list_num)
sum = sum_list(list_num)
print(f'tong list la: {sum}')

average = average_list(list_num)
print(f'trung binh cong cua list la: {average}')

larger_than_average(list_num)
list_num = list_sort(list_num)
print("sap xep list tang dan la: ",list_num)

decrease(list_num)