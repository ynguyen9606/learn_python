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

def sohoanhao(n):
    sum = 0 
    for i in range(1, n):
        if n % i == 0:
            sum += i

    return sum == n
    
def main():
    n = input_num()
    print(sohoanhao(n))

main()