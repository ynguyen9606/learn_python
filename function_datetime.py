from datetime import *

t1 = input("nhap thoi gian vao lam (HH:MM): ")
t2 = input("nhap thoi gian nghi (HH:MM): ")

dt1 = datetime.strptime(t1, "%H:%M")
dt2 = datetime.strptime(t2, "%H:%M")
if dt2 < dt1 :
    dt2 += timedelta(days=1)
OT = dt2 - dt1
lunch_start = datetime.strptime("12:00","%H:%M")
lunch_end = datetime.strptime("13:00","%H:%M")
night_end = datetime.strptime("21:00","%H:%M")
if dt1 >= lunch_start and dt1 <= lunch_end and OT > timedelta(hours=4):
    OT -= timedelta(hours=1)
    lunch = "Y"
else:
    lunch = "N"
if dt2 > night_end and OT > timedelta(hours=3) :
    night = "Y"
else:
    night = "N"
total_minutes = OT.total_seconds() // 60
hours = float(total_minutes / 60)

print(f"OT = {round(hours,2)},Lunch = {lunch},Night = {night}")
