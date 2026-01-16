#2
def input_num():
    while True:
        try:
            num = float(input("nhap so: "))
            return num
        except ValueError:
            print("Sai dinh dang, nhap lai: ")

#3
def sum(num1, num2):
    return num1 + num2

#4
def subtraction(num1, num2):
    return num1 - num2

#5
def multiplication(num1, num2):
    return num1 * num2

#6
def division(num1, num2):
    return num1 / num2

#7
def greatest_common_divisor(num1, num2):
    if num2 == 0:
        return num1
    else:
        return greatest_common_divisor(num2, num1 % num2)

#8
def least_common_multiple(num1, num2):
    return abs(num1 * num2) / greatest_common_divisor(num1,num2)

def main():
    number1 = input_num()
    number2 = input_num()

    print(f'{number1} + {number2} = ', sum( number1, number2))
    print(f'{number1} - {number2} = ', subtraction( number1, number2))
    print(f'{number1} * {number2} = ', multiplication( number1, number2))
    print(f'{number1} / {number2} = ', round(division( number1, number2), 2))
    print(f'The greatest common divisor of {number1} and {number2} is:',greatest_common_divisor(number1, number2))
    print(f'The least common multiple of {number1} and {number2} is:',least_common_multiple(number1, number2))

main()