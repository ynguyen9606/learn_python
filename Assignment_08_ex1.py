#1
def input_num():
    while True:
        try:
            num = float(input("Nhập số: "))
            return num
        except ValueError:
            print("Sai định dạng, nhập lại: ")

#2
def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

#3
def is_isosceles(a, b, c):
    return a == b or b ==c or c == a 

#4
def is_equilateral(a, b, c):
    return a == b == c
#5
def is_right_triangle(a, b, c):
    num = sorted([a, b, c])
    return round(num[0] ** 2 + num[1] ** 2, 2) == round(num[2] ** 2)
#6   
def is_right_isosceles(a, b, c):
    return is_right_triangle(a, b, c) and is_isosceles(a, b, c)

def main():
    print("nhap lan luoc 3 so: ")
    a = input_num()
    b = input_num()
    c = input_num()
    if is_triangle(a, b, c):
        print("day la mot tam giac")
    else:
        print("a, b, c không phải là 3 cạnh của một tam giác.")      
        
    if is_isosceles(a, b, c):
        print("day la mot tam giac can")
    else:
        print("day khong phai la tam giac can")

    if is_equilateral(a, b, c):
        print("day la mot tam giac deu")
    else:
        print("day khong phai la tam giac deu")

    if is_right_triangle(a, b, c):
        print("day la mot tam giac vuong")
    else:
        print("day khong phai la tam giac vuong")

    if is_right_isosceles(a, b, c):
        print("day la mot tam giac vuong can")
    else:
        print("day khong phai la tam giac vuong can")
    

if __name__=="__main__":
    main()