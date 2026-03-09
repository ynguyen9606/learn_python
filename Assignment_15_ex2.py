with open("Assignment_2_S8.txt", "w") as file:
    file.write("Xin chao ban. Hom nay troi dep. Ban co khoe khong?")

find = input("nhap tu muon check: ")

with open("Assignment_2_S8.txt", "r") as file:
    data = file.read()

data.split()

count = data.count(find)

print(f'tu :{find} xuat hien trong file {count} lan')