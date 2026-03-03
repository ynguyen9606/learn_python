from abc import ABC, abstractmethod
class INews(ABC):
    @abstractmethod
    def display(self):
        pass

class News(INews):
    def __init__(self, id, title, publishdate, author, content):
        self.id = id
        self.title = title
        self.publishdate = publishdate
        self.author = author
        self.content = content
        self.__averagerate = 0
        self.RateList = []

    def getAverageRate(self):
        return self.__averagerate

    def setAverageRate(self, value):
        self.__averagerate = value

    def calculate(self):
        if len(self.RateList) == 3:
            avg = sum(self.RateList) / 3
            self.setAverageRate(avg)
        else:
            print("RateList pphai co 3 phan tu !")
    
    def display(self):
        print("Title:", self.title)
        print("Publish Date:", self.publishdate)
        print("Author:", self.author)
        print("Content:", self.content)
        print("Average Rate:", self.getAverageRate())
        print("----------------------")
        
news_list = []  
id_counter = 1

while True:
    print("\n===== MENU =====")
    print("1. Insert news")
    print("2. View list news")
    print("3. Average rate")
    print("4. Exit")

    choice = input("Chọn: ")

    if choice == "1":
        title = input("Nhap title: ")
        publishdate = input("Nhap publish date: ")
        author = input("Nhap author: ")
        content = input("Nhap content: ")

        news = News(id_counter, title, publishdate, author, content)

        for i in range(3):
            rate = float(input(f"Nhap rate {i+1}: "))
            news.RateList.append(rate)

        news_list.append(news)
        id_counter += 1

        print("Them tin tuc thanh cong!")

    elif choice == "2":
        if not news_list:
            print("Danh sach rong!")
        else:
            for n in news_list:
                n.display()

    elif choice == "3":
        if not news_list:
            print("Danh sach rong!")
        else:
            for n in news_list:
                n.calculate()   
                n.display()     

    elif choice == "4":
        print("Thoat chuong trinh...")
        break

    else:
        print("Lua chon khong hop le!")