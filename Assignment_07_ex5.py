import random  

N = int(input("nhap so phan tu N (0 < N < 50): "))


a = [random.randint(0, 99) for _ in range(N)]
print("list cua ban la:", a)

a.sort()
print("list sau khi sap xep tang dan la:", a)

b = []
for x in a:
    if x not in b:
        b.append(x)

print("list sau khi bo trung la:", b)
