def input_num():
    while True:
        try:
            num = int(input("nhap so nguyen duong n = "))
            if num > 0:
                print("so vua nhap la n = ",num)
                return  num
            else:
                print("so can nhap phai la so nguyen duong, nhap lai !")
        except ValueError:
            print("nhap  sai dinh dang, nhap lai !")

def chusoxuathiennhieunhat(n):
    list_num = []
    count_max = 0
    num_max = 0

    while n > 0:
        single_num = n % 10
        list_num.append(single_num)
        n = n // 10

    for i in list_num:
        count_num = list_num.count(i)
        if count_max < count_num or (count_num == count_max and i > num_max):
            count_max = count_num
            num_max = i
    print(f'{num_max} co {count_max} lan')

def main():
    n = input_num()
    chusoxuathiennhieunhat(n)

main()