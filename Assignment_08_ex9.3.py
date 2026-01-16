def input_num(name, min_num = 0, max_num = 1000):
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

def greatest_common_divisor(num1, num2):
    while num2 != 0:
        r = num1 % num2
        num1 = num2
        num2 = r
    return num1

def check_sum_fractions(num1, num2, num3):
    nums = [num1, num2, num3]
    fractions = []

    for i in range(3):
        for j in range(3):
            if i != j:
                fractions.append((nums[i], nums[j]))
    
    fraction_min = min(fractions,key = lambda x: x[0] / x[1])
    numerator, denominator = fraction_min


    num = greatest_common_divisor(numerator, denominator)
    min_numerator = numerator // num
    min_denominator = denominator // num

    sum = min_numerator + min_denominator
    print("tong = ",sum)


def main():
    A = input_num("A")
    B = input_num("B")
    C = input_num("C")
    check_sum_fractions(A, B, C)

main()