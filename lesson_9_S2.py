#tuple giong list nhung chi chua du lieu khong doi,k them ,k xoa , k sua 
 
tu = (1, 4, 5, 6, 22, 432, 123)
tu1 = ("Hai", "Tu", "Lan")
tu2 = tu + tu1

print(tu2)

for i, t in enumerate(tu2):
    print(i, t)