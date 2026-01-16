def input_number ():
    #a, b, c = map(float,input("Nhap do dai 3 canh : ").split)
    a = float(input("Nhap do dai canh thu nhat : "))
    b = float(input("Nhap do dai canh thu hai : "))
    c = float(input("Nhap do dai canh thu b : "))
    return a, b, c

def is_triangle(a, b, c):
    return a + b > c and a + c > b and b + c > a

def is_isosceles(a, b, c):
    return a == b or b ==c or c == a 

def is_equilateral(a, b, c):
    return a == b == c

def is_right_triangle(a, b, c):
    #num = storted([a, b, c])
    #return round(num[0] ** 2 + num[1] ** 2, 2) == round(num[3] ** 2)
    return round(a ** 2 + b ** 2, 2) == round(c ** 2, 2) or round(a ** 2 + c ** 2, 2) == round(b ** 2, 2)  or round(c ** 2 + b ** 2, 2) == round(a ** 2, 2) \
    
def is_right_isosceles(a, b, c):
    return is_right_triangle(a, b, c) and is_isosceles(a, b, c)

def main():
    a, b, c = input_number()
    if is_triangle(a, b, c):
        print("day la mot tam giac")        
        if is_isosceles(a, b, c):
            print("day la mot tam giac can")
        if is_equilateral(a, b, c):
            print("day la mot tam giac deu")
        if is_right_isosceles(a, b, c):
            print("day la mot tam giac vuong")
            if is_right_isosceles(a, b, c):
                print("day la mot tam giac vuong can")
    else:
        print("a, b, c không phải là 3 cạnh của một tam giác.")

if __name__=="__main__":
    main()