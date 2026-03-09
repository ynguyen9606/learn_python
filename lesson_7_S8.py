class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def show(self):
        print(f'Name: {self.name}, age: {self.age}, color : {self.color}')

#CRUD với 1 đối tượng 

C = Cat("Mooon", "2", "black")
#create
import  pickle
with open("test_7_S8.txt", "wb") as file:
    pickle.dump(C, file)

#read
with open("test_7_S8.txt", "rb") as file:
    cats = pickle.load(file)
    cats.show()

#update
with open("test_7_S8.txt", "rb+") as file:
    cat = pickle.load(file)
    cat.color = "white"

    file.seek(0)
    pickle.dump(cat, file)

with open("test_7_S8.txt", "rb") as file:
    cats = pickle.load(file)
    cats.show()

#delete
with open("test_7_S8.txt", "wb") as file:
    pass

with open("test_7_S8.txt", "rb") as file:
    cats = pickle.load(file)
    cats.show()