import math

n = int(input("nhap n can test: "))

def prime(n):
    
    if(n < 2):
        print("day khong phai la so nguyen to")
        return
    
    else:
        
        for i in range(2, int(math.sqrt(n)) + 1 ):#vif amth.sqrt(n) se tra ve so thuc nen can ep kieu int cungf kieu voi for
            
            if n % i == 0:
                print("day khong phai la so nguyen to ")
                return
        
        print(f'n = {n} la so nguyen to ')

prime(n)