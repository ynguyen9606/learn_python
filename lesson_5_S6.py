from abc import ABC,abstractmethod
class Ca(ABC):
    @abstractmethod
    def __init__(self, khoiluong, chieudai):
        self.khoiluong = khoiluong
        self.chieudai = chieudai

    @abstractmethod
    def boi(self):
        pass

class CaChep (Ca):
    def __init__(self, khoiluong, chieudai):
        super().__init__(khoiluong, chieudai)

    def boi(self):
        print("boi vong vong")

ca = CaChep(40, 30)
print(ca.khoiluong)
ca.boi()