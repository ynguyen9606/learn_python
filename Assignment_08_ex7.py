def input_num():
    while True:
        try:
            num = int(input("nhap so: "))

            if num > 0:
                return num
            
            else:
                print("phai nhap 1 so nguyen duong")

        except ValueError:
            print("Sai dinh dang, nhap lai: ")

def sum_of_squares(num):
    sum = 0
    while num > 0:
        single_num = num % 10
        sum += single_num ** 2
        num = num // 10
    return sum

def happy_num(num):
    list_num_seen = set()
    original_num = num
    while num != 1 and num != 0:
        if num in list_num_seen:
            print(f"So {original_num} khong phai la so hanh phuc hay so buon ba")
            return
        list_num_seen.add(num)
        num = sum_of_squares(num)
    
    if num == 1:
        print(f"So {original_num} la so hanh phuc")
    else:
        print(f"So {original_num} la so buon ba")

    

num = input_num()
happy_num(num)
