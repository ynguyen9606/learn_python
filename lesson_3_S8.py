            #  GHI ĐÈ FILE 
data  ="1.nguyen van a \n2.nguyen ho c\n"   ### phần nội dung muốn viết thêm vào file mới \
list_word = [
    "1/hat\n",
    "2/dan\n",
    "3/mua\n"
]
with open("test_3_S8.txt", "a") as file: # mode "a" co nghia la append
    #file.write(data) # dung ham write de viet them 1 chuoi vao file
    file.writelines(list_word) # dung ham writelines de viet them nhieu chuoi (vd: dang list) vao file

with open("test_3_S8.txt","r") as file:
    content = file.read() # hàm read đọc toàn bộ file
    print(content)
