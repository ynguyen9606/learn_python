import pickle
import os

filename = "Assignment_3_S8.pkl"  

default_contacts = [
    "Hoang Van Phuc 0987366452",
    "Truong Minh Duc 012456986",
    "Luong Cong Toan 0913433678",
    "Tran Quang Hung 01657899877",
    "Nguyen Thanh Tam 0945678900"
]

if not os.path.exists(filename) or os.path.getsize(filename) == 0:
    ListInput = default_contacts
else:
    with open(filename, "rb") as file:
        ListInput = pickle.load(file)

name = input("Nhap ho ten: ")
phone = input("Nhap so dien thoai: ")
ListInput.append(f"{name} {phone}")

with open(filename, "wb") as file:
    pickle.dump(ListInput, file)

print("Da them thong tin!\n")
print("Danh sach lien lac:")

for i, contact in enumerate(ListInput, 1):
    print(f"{i}. {contact}")

find = input("Nhap so dien thoai can tim: ")
found = False

for contact in ListInput:
    if find in contact:
        print("Tim thay:", contact)
        found = True
        break

if not found:
    print("Khong tim thay so dien thoai!")