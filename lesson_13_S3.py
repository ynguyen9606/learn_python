def main():
    N = N_input()

    if check_integer(N) == True:
        print(f"{N} la so nguyen! ")
    else:
        print("day khong phai la so nguyen! ")
    
    if check_integer(N) == True:
        if check_odd_even(N) == True:
            print("day la so chan! ")
        else:
            print("day la so le!")
    else:
        print("khong xac dinh duoc tinh chan le!")

    if check_odd_even(N) == True:
        if check_even_positive_or_odd_negative(N) == True:
            print(f'{N} la so chan duong!')
    else:
        if check_even_positive_or_odd_negative(N) == False:
            print(f'{N} la so le am!')

    check_square_num(N)

    check_Amstrong(N)

def N_input():
    while True:
        try:
            N = float(input("nhap N = "))
            print(f"gia tri N cua ban la: {N}")
            return N
        except ValueError:
            print("gia tri N phai la so, hay nhap lai: ")

def check_integer(N):
    if N == int(N):
        return True
    return False

def check_odd_even(N):
    if N % 2 == 0:
        return True
    return False
    
def check_even_positive_or_odd_negative(N):
    if N > 0:
        return True
    return False

def check_square_num(N):
    if check_integer(N) and N > 0 and check_integer(N**0.5):
        print(F'{N} la so chinh phuong!')
    else:
        print(f'{N} khong phai la so chinh phuong!')
    
def check_Amstrong(N):
    if check_integer(N) and N > 0:
        sum = 0
        original_num = N

        while N != 0:
            sum += (N % 10) ** 3
            N //= 10
        if sum == original_num:
            print(f'{original_num} la so Amstrong!')
        else:
            print(f'{original_num} khong phai la so Amstrong!')
    else:
            print(f'{original_num} khong phai la so Amstrong!')

main()