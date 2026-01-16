for i in range(0, 50, 2):
    print(i)

a = "hihih0i"
for i in a:
    if i == "0":
        break
    print(i)
result = []
for i in range(-10, 51, 1):
    if i % 5 == 0:
        result.append(i)
print(f'chuoi chia het cho 5 trong [-10-50] la {result}')