def input_num(name, min_num = 1, max_num = 10000):
    while True:
        try:
            num = int(input(f'nhap so {name} = '))

            if num < min_num:
                print(f"{name} phải >= {min_num}")
            elif max_num is not None and num > max_num:
                print(f"{name} phải <= {max_num}")
            else:
                return num

        except ValueError:
            print("Sai dinh dang, nhap lai: ")

def square_sums(N):
    sum = 0
    for i in range(N + 1):
        sum += i
    sum **= 2
    return sum

def sum_each_square(N):
    sum = 0
    for i in range(N + 1):
        i **= 2
        sum += i
    return sum

def subtraction(N):
    result = square_sums(N) - sum_each_square(N)
    print(result)
    return result


T = input_num("T", 1, 10000)

N_list = []
for i in range(1, T + 1):
    N = input_num(f"N[{i}]", 1, 10000)
    N_list.append(N)

for N in N_list:
    subtraction(N)