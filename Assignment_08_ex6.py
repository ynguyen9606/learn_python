def input_num(num, min_num = 1, max_num = 10000):
    while True:
        try:
            num = int(input(f'nhap so {num} = '))

            if num < min_num:
                print(f"{num} phải >= {min_num}")
            elif max_num is not None and num > max_num:
                print(f"{num} phải <= {max_num}")
            else:
                return num

        except ValueError:
            print("Sai dinh dang, nhap lai: ")

def is_prime(x):
    if x < 2:
        return False
    for i in range(2, int(x**0.5) + 1):
        if x % i == 0:
            return False
    return True

T = input_num("T", 1, 1000)

N_list = []
for i in range(1, T + 1):
    N = input_num(f"N[{i}]", 1, 10000)
    N_list.append(N)

max_N = max(N_list)

primes = []
num = 2
while len(primes) < max_N:
    if is_prime(num):
        primes.append(num)
    num += 1

for N in N_list:
    print(primes[N-1])