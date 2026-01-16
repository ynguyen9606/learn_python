list1 = ["Huy", "Tuấn", "Vũ"]
for i, name in enumerate(list1): #tạo stt list
    print(i, name)

list2 = [n for n in range(10)] # list onl
print(list2)

ho = ["Nguyen", "Ho", "Le"]
ten = ["Tuan", "Tu", "Bao"]
for h, t in zip(ho, ten): #ghep long cac ky tu trong list
    print(h, t)

list3 = [1, 3, 5, 2, 2, 5, 8, 0]
list3_copy = list3
print(list3_copy)

list3_copy[0] = "hihihi"
print(list3_copy)

list3.clear()# neu có thay doi o goc hay nhanh thi phan con lại cung doi theo
print(list3_copy)