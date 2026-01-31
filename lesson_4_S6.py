class Ong:
    def showong(self):
        print("ong")
    
    def demo(self):
        print("demo ong")
    

class cha(Ong):
    def showcha(self):
        print("cha")
    
    def demo(self):
        print("demo cha")
    

class con(cha):
    def show1(self):
        super().showcha()
    
co = con()
co.showong()
co.showcha()
co.show1()
co.demo() # lấy phương thức mới nhất  (gần nhất or nhận cuối cùng)
print("*" * 5)

# đa thừa kế : 1 lớp cso thể thừa kế cùng lúc nhiều lớp
class con2(Ong, cha): # cách thể hiện của đa thừa kế (k nên keess thừa lại lớp cha nếu lớp cha đã kế từ lớp ong)
    def showCon2(self):
        print("con")
# nếu có 2 phương thức giống nhau thì lớp con sẽ nhận phương thức mà lớp thừa kế đầu tiên


co2 = con2()
co2.showong()
co2.showcha()
co2.showCon2()
