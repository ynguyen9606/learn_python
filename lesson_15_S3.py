#ham vo danh (anonymous function): dùng lambda
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
square = list(map(lambda x : x ** 2, number))
print(square)

even_number = list(filter(lambda x : x % 2 == 0, number))
print(f'so chan la: {even_number}')

names = ["hoang", "tuan", "tam", "vu", "y", "van"]
sort_names = sorted(names,key = lambda x : len(x), reverse= True) #neu muon sap xep nguoc lai thì bỏ reverse = True
print(sort_names)