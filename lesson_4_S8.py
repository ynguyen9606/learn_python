with open("test_4_S8.txt", "r+") as file:# file ban đầu đã cso nội dung, ta có thể đọc và còn có thể ghi thêm bằng cách dùng mode "r+"
    content = file.read()
    print(content)
    file.seek(1) # hàm này ddauw con trỏ về vị trí muốn đưa
    file.write("\nxin chao ban! ") 