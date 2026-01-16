#dtb = float(input("nhap diem trung binh: "))
#while (10 < dtb or dtb < 0 ):
#    dtb = float(input("nhap lai [0-10]: "))
while True:
    try:
        average_score = float(input("nhap diem trung binh cua ban: "))
        if 0 <= average_score <= 10:
            print(f"diem trung binh cau ban la : {round(average_score,2)}")
            break
        else:
            print("diem trung binh phai nam trong [0-10] ")
    except ValueError :
        print("diem trung binh phai la so; ")
#in tu 0-100
#i = 0
#while (0 <= i <= 100):
#    print(i)
#    i += 1
#else:
#    print("finish ! ")
