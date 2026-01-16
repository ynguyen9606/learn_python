def input_num(name, min_num = 1, max_num = 10**9):
    while True:
        try:
            num = int(input(f'nhap so {name} = '))

            if num < min_num:
                print(f"{name} phải > {min_num}")
            elif max_num is not None and num > max_num:
                print(f"{name} phải < {max_num}")
            else:
                return num

        except ValueError:
            print("Sai dinh dang, nhap lai: ")

def sum(N,M):
    list_num = []
    for i in range(1, N//2 + 1):
        list_num.append(i)
        num = N - i + 1
        list_num.append(num)
    
    sum_M = 0
    for i in range(M):
        sum_M += list_num[i]

    print(f'tong {M} so dau tien trong day {list_num} voi N = {N} la: {sum_M}')

def main():
    N = input_num("N", 1, 10**9)
    M = input_num("M", 1, N)


    sum (N, M)

main()