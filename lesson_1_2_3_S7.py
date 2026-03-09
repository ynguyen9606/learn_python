def input_num():
    while True:
        try:
            num = int(input("nhap so nguyen duong x = "))
            if num > 0 :
                print(f'so ban vua nhap la: {num}')
                return num
            else:
                print("nhap so duong x = ")
        except ValueError as e:# as e ở đây chỉ ra lỗi ở đâu
            print(f"{e} sai dinh dang, nhap lai: ")

number = input_num()

while True:
    try:
        # Code có thể gây lỗi
        n = int(input("nhap so nguyen: "))
        print(100 / n)
        break
    except ZeroDivisionError as e:  # check có phải là 0 hay k

        print(f"{e} khong the chia cho 0")
    except:
        print("phai nhap so nguyen ")
    
    # except (ZeroDivisionError, ValueError) as e: ta có thể gộp nhiều lỗi vào 1 except
    #     print("nhap cho đúng", e)

    finally: # ít cần dùng
        print("finally luon chay")
        # Luôn chạy nếu trc nó sai hay đúng

#kích hoạt ngoại lệ bằng từ kháo raise
def tinh_giai_thua(n):
    if n % 1 != 0 or n < 1:
        raise ValueError("so phai la so nguyen duong ")
    gt = 1
    for i in range(1, n+1):
        gt *= i
    print(gt)
try:
    tinh_giai_thua(5)
except ValueError as e:
    print(e)