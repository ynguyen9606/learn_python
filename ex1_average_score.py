max_dtb = 0
name_max = "noname"
def dtb(t,v,a):
    return round ((t + v + a) / 3,2)

while True :
    hoten = input("nhap ho va ten hs : ")
    try:
        t = float(input("nhap diem toan : "))
        v = float(input("nhap diem van : "))
        a = float(input("nhap diem tieng anh : "))
    except ValueError :
        print("ban phai nhap diem la so ! ")
        continue
    diem_tb = dtb(t, v, a)
    print(f"{hoten} co diem toan là: {t},van la : {v},tieng anh la : {a},diem trung binh cac mon la : {diem_tb}")

    if diem_tb > max_dtb:
        max_dtb = diem_tb
        name_max = hoten

    hoi = input("nhap S or s de ngung nhap : ")
    if hoi == "S" or hoi == "s" :
        break
print(f"{name_max} co diem trung binh cao nhat lop la : {max_dtb}")