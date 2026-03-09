class Cat:
    def __init__(self, name, age, color):
        self.name = name
        self.age = age
        self.color = color

    def show(self):
        print(f'Name: {self.name}, age: {self.age}, color : {self.color}')

#CRUD với nhiều đối tượng 

C = Cat("Mooon", "2", "black")
C1 = Cat("Tieu Ho", "3", "gold")
#create
import  pickle
with open("test_8_S8.txt", "wb") as file:
    pickle.dump([C, C1], file)

#read
with open("test_8_S8.txt", "rb") as file:
    cats = pickle.load(file)
    for cat in cats:
        cat.show()

#update
with open("test_8_S8.txt", "rb+") as file:
    cats = pickle.load(file)
    file.seek(0)
    for cat in cats:
        if cat.color == "gold":
            cat.color = "yellow"
            break

    pickle.dump(cats, file)

#read again
with open("test_8_S8.txt", "rb") as file:
    cats = pickle.load(file)
    for cat in cats:
        cat.show()

#delete
with open("test_8_S8.txt", "rb+") as file:
    cats = pickle.load(file)
      
    file.seek(0)
    for cat in cats:
        if cat.name == "Mooon":
            cats.remove(cat)
            break
    
    pickle.dump(cats, file)

#read again
with open("test_8_S8.txt", "rb") as file:
    cats = pickle.load(file)
    for cat in cats:
        cat.show()