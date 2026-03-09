with open("Assignment_1_S8.txt", "w") as file:
    file.write("Xin chao ban. Hom nay troi dep. Ban co khoe khong?")

find = input("nhap ky tu muon check: ")

with open("Assignment_1_S8.txt", "r") as file:
    data = file.read()

count = data.count(find)

print(f'ky tu :{find} xuat hien trong file {count} lan')