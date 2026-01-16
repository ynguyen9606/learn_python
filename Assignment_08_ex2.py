#1
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

#2
def sum_n(n):
    sum = 0
    single_number = n
    while n > 0:
        sum += n % 10
        n //= 10
    print(f'tong cac so trong {n} la {sum}')

#3
def prime_factorization(n):
    i = 2
    ket_qua = []  
    so = n
    while i * i <= so:
        while n % i == 0:
            ket_qua.append(i)   
            n //= i
        i += 1
    if n > 1:
        ket_qua.append(n)     
    print(f"cac thua so nguyen to cua {so} là:", ket_qua)
    return ket_qua

#4
def divisor(n, i=1):
    if i > n:
        return []
    if n % i == 0:
        return [i] + divisor(n, i + 1)
    else:
        return divisor(n, i + 1)

#5
def prime_divisors(n):
    num_of_divisor = divisor(n)  
    num_of_prime = [] 
    
    for i in num_of_divisor:
        if i > 1:
            for j in range(2, int(i**0.5) + 1):
                if i % j == 0:
                    break
            else:
                num_of_prime.append(i)
    
    print(f'cac uoc so nguyen to cua {n} la: {num_of_prime}')
    return num_of_prime


n = input_num()
sum_n(n)
prime_factorization(n)
print(f'cac uoc so cua {n} la: ',divisor(n))
prime_divisors(n)