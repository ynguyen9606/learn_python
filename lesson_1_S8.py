           # ĐỌC FILE
with open("test_1_S8.txt","r") as file:
    #content1 = file.read() # hàm read đọc toàn bộ file
    #print(content1)

    #content2 = file.readline()# hàm readline đọc TỪNG DÒNG 1   
    #print(content2) 
    #while content2:
    #    print(content2, end="")#them end để xóa bỏ line trắng
    #    content2 = file.readline()

    #content3 = file.readlines() # hàm readlines đọc HẾT lần lược tất cả các dòng 
    #for content in content3:
    #    print(content, end="")

    #for line in file:
    #    print(line, end="")
    
       # đọc từng từ trong file
    #content = file.read()
    #words = content.split()
    #for word in words:
    #    print(word)
    #
    #print(len(words))
    
    count = 1
    for line in file:
        words = line.split()
        
        #print(words) # lúc này words ở dạng list các từ
        
        print(f'in cac tu o dong {count}')
        for word in words:
            print(word)
        count += 1
    