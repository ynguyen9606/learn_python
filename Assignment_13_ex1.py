from abc import ABC, abstractmethod
class Phone(ABC):
    @abstractmethod
    def insertphone(self, name, phone):
        pass
    
    @abstractmethod
    def removephone(self, name):
        pass

    @abstractmethod
    def updatephone(self, name, newphone):
        pass

    @abstractmethod
    def searchphone(self, name):
        pass

    @abstractmethod
    def sort(self):
        pass

class PhoneBook(Phone):
    def __init__(self):
        self.PhoneList = []
    
    def insertphone(self, name, phone):
        for i in range(len(self.PhoneList)):
            if self.PhoneList[i].startswith(name + " :"):
                data = self.PhoneList[i].split(" : ")
                numbers = data[1].split(" - ")

                if phone not in numbers:
                    numbers.append(phone)
                    self.PhoneList[i] = name + " : " + " - ".join(numbers)
                    print("Them so moi thanh cong!")
                else:
                    print("So da ton tai!")
                return

        self.PhoneList.append(name + " : " + phone)
        print("Them moi thanh cong!")

    def removephone(self, name):
        for i in self.PhoneList:
            if i.startswith(name + " :"):
                self.PhoneList.remove(i)
                print("Xoa thanh cong!")
                return
        print("Khong tim thay!")

    def updatephone(self, name, newphone):
        for i in range(len(self.PhoneList)):
            if self.PhoneList[i].startswith(name + " :"):
                self.PhoneList[i] = name + " : " + newphone
                print("Cap nhat thanh cong!")
                return
        print("Khong tim thay!")

    def searchphone(self, name):
        for i in self.PhoneList:
            if i.startswith(name + " :"):
                print(i)
                return
        print("Khong tim thay!")

    def sort(self):
        self.PhoneList.sort()
        for item in self.PhoneList:
            print(item)

class ManagePhoneBook:

    @staticmethod
    def main():
        pb = PhoneBook()

        while True:
            print("\n= PHONEBOOK MANAGEMENT SYSTEM =")
            print("1. Insert Phone")
            print("2. Remove Phone")
            print("3. Update Phone")
            print("4. Search Phone")
            print("5. Sort")
            print("6. Exit")

            choice = input("Chon chuc nang (1-6): ")

            if choice == "1":
                name = input("Nhap ten: ")
                phone = input("Nhap so dien thoai: ")
                pb.insertphone(name, phone)

            elif choice == "2":
                name = input("Nhap ten can xoa: ")
                pb.removephone(name)

            elif choice == "3":
                name = input("Nhap ten can cap nhat: ")
                newphone = input("Nhap so dien thoai moi: ")
                pb.updatephone(name, newphone)

            elif choice == "4":
                name = input("Nhap ten can tim: ")
                pb.searchphone(name)

            elif choice == "5":
                pb.sort()

            elif choice == "6":
                print("Thoat chuong trinh...")
                break

            else:
                print("Lua chon khong hop le!")

if __name__ == "__main__":
    ManagePhoneBook.main()