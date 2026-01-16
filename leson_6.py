# find number
n = int(input("nahp so ky tu can xem: "))
s = ""
i = 1

while len(s) < n:
    s += str(i)
    i += 1

print(s)

#Đếm số lượng số một số nhỏ hơn hoặc bằng N cho trước
N = int(input("nhap N = "))  

count = 0
str_N = str(N)
len_N = len(str_N)

count += (len_N - 1) * 9

for d in range(1, 10):
    one_digit_number = int(str(d) * len_N)
    if one_digit_number <= N:
        count += 1

print(count)

#Số hạnh phúc, số buồn bã
n = int(input("nhap so can test N = "))
m = n
count = 0
while True:
    sum = 0

    while m != 0:
        sum += (m % 10) ** 2
        m //= 10

    count += 1
    print(sum)

    if count == 100:
        break

    if sum != 1 and sum != 0:
        m = sum
        continue

    else:
        break

if sum == 1:
    print(f"{n} là số hạnh phúc")

elif sum == 0:
    print(f"{n} là số buồn bã")

else:
    print(f"{n} không là số hạnh phúc hay buồn bã")

#Tính tích các chữ số và tìm chữ số lớn nhất của một số nguyên dương
while True:
    try:
        N = int(input("nhap so can test N = "))       
        if N < 1:              
            continue
        break                  
    except:
        continue             

m = list(str(N))          
s = 1

for i in range(len(m)):
    s *= int(m[i])    
    
print(s, max(m))              