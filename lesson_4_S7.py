class MyException(Exception):
    def __init__(self, mes):
        self.mes = mes
        super().__init__(self.mes)

def chia(n):
    if type(n).__name__ not in ["int", "float"]:
        raise MyException("phai la so!")
    
    print(n/10)

try:
    chia(10)
    print(10/0) # tu động kích hoạt ngoại lệ
except MyException as e:
    print(e)

print("finished")
