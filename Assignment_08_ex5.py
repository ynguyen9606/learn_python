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

def fibonacci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    
#2
def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

def demsonguyento(n, m):
    count = 0
    for num in range(n, m + 1):
        if is_prime(num):
            count += 1
    return count

#3
def kiemtradoixung(s):
    s = str(s)
    left = 0
    right = len(s) - 1

    while left < right:            
        if s[left] != s[right]:   
            return False
        left += 1
        right -= 1

    return True 

n = input_num()
print(f'fibonacci cua {n} la {fibonacci(n)}')

m = input_num()
print(f'so luong so nguyen to trong doan [{n}, {m}] la: {demsonguyento(n, m)}')

s = print(input('nhap vao 1 chuoi: '))
print(f"kiem tra tinh doi xung cua chuoi tren la: {kiemtradoixung(s)}")