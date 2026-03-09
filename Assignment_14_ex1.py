class MyException(Exception):
    def __init__(self, mes):
        self.mes = mes
        super().__init__(self.mes)

def InputNum():
    while True:
        try:
            N = int(input("N = "))
            if not (N > 0 and N <= 10000 and N % 2 == 0):
                raise MyException("N phai la so chan duong <= 10000")
            return N
        
        except ValueError :
            print("nhap sai dinh dang, nhap lai N !")
            
        except MyException as e:
            print(e)
        
N = InputNum()
print(N)