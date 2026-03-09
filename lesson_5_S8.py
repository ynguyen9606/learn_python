with open("test_5_S8.txt", "w+") as file: # nếu dùng mode "w+" thì khi run thfi sẽ xóa hết file ban đầu 
    file.write("python")
    file.seek(0) # nếu k dùng seek thì con trỏ sau khi run sẽ ở cuối file txt -> không đọc đc gì cả 
    content = file.read()
    print(content)