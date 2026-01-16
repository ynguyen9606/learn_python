#1
list_input = input("nhap vao chuoi : ")
while not (0 < len(list_input) <= 50):
    list_input = input("do dai chuoi phai nho hon 50! nhap lai: ")
print(list_input)

#2
check_num = []
for i in list_input:
    try:
        num = float(i)
        check_num.append(num)
    except ValueError:
        continue
if check_num:
    print("co cac ky tu so la :",check_num)
else:
    print("khong tim thay")

#3
alpha = [i for i in list_input if i.isalpha()and i.isupper()]
                                    #check chu cai
if alpha:
    print(f'cac ky tu in hoa trong list la: {alpha}')
else:
    print("khong tim thay! ")

#4
find = input("nhap ky tu muon tim: ")
if find in list_input:
    print(f'ky tu {find} co trong list')
else:
    print("khong tim thay! ")

#5
list_new_input = input("nhap vao chuoi moi : ")
print(list_new_input)

if list_new_input in list_input:
    print("chuoi b nam trong chuoi a ")
else:
    print("chuoi b khong nam  trong chuoi a ")

if len(list_new_input) > len(list_input):
    print("chuoi b lon hon chuoi a")
elif len(list_new_input) < len(list_input):
    print("chuoi b be hon chuoi a")
else:
    print("chuoi b bang chuoi a")

#6
if list_input == list_input[::-1]:
    print("list tren co tinh doi xung ")
else:
    print("list tren khong co tinh doi xung ")

#7
count =  0
for i in list_input:
    i.split()
    if i.isalpha():
        count +=1
if count > 0:
    print(f"so tu trong chuoi la: {count}")
else:
    print("khong tim thay! ")

#8+9
list_cut_end = list_input.rstrip()
list_cut_head = list_input.lstrip()
print("list sau khi cat space o dau: ", list_cut_head)
print("list sau khi cat space o cuoi: ", list_cut_end)

#10
list_single_space = ' '.join(list_input.split())
                        #ghep cac ky tu voi nhau bang dau cach
print("list chi co space o giua: ", list_single_space)

#12
print("so lan xuat hien cau cac ky tu la:")
for character in list_input:
    if list_input.index(character) == list_input.find(character):
        print(f"'{character}': {list_input.count(character)} lần")

#13
if len(list_input) >= 5:
    list_inserted_newline = list_input[:4] + '\n' + list_input[4:]
    print("hcuoi sau khi chen '\\n' giua vi tri 4 va 5 la:", repr(list_inserted_newline))
else:
    print("Chuoi qua ngan de chen '\\n' ggiua vi tri 4 va 5.")

#14
list_tab = ""
i = 0

while i < len(list_input) - 1:
    list_tab += list_input[i]

    if list_input[i].isupper() and list_input[i+1].isupper():
        list_tab += '\t'
    i += 1

if list_input:
    list_tab += list_input[-1] #ky tu cuoi cung

print("chuoi sau khi chen '\\t' giua 2 ky tu in HOA:")
print(list_tab)