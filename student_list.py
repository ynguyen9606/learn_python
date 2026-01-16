students = input("nhap danh sach cac sinh vien: ").split(',')

print("\ndanh sach sinh vien ban nhap la: ")
for s in students:
    print(s)

delete_name = input("\nNhập tên sinh viên cần xóa (chỉ phần tên): ").strip()

for s in students[:]:  
    name = s.split()[-1]  # lấy phần tên (cuối cùng trong họ tên)
    if name == delete_name:
        students.remove(s)

print("\nDanh sách sinh viên sau khi xóa:")
for s in students:
    print(s)