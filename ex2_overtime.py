import time
while True :
    t1 = input("nhap gio vao lam (HH:MM) : ")
    try :
        read_strtimein = time.strptime(t1,"%H:%M")
        print("thoi gian ban vao lam la : ",time.strftime("%H:%M",read_strtimein))
        break
    except ValueError  :
        print("dinh dang sai ,nhap lai : ")

while True :
    t2 = input("nhap gio nghi lam (HH:MM) : ")
    try :
        read_strtimeout = time.strptime(t2,"%H:%M")
        print("thoi gian ban nghi lam la : ",time.strftime("%H:%M",read_strtimeout))
        break
    except ValueError  :
        print("dinh dang sai ,nhap lai : ")

time_in = time.strptime(t1,"%H:%M")
time_out = time.strptime(t2,"%H:%M")
if time_out <time_in :
    time_out += timedelta(days=1)
OT = time_out - time_in
print(f"so gio OT la : {OT}")