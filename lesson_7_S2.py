list1 = [1, 2.99, 'hihihi', 321 ]
        #0   1       2        3
        #-4 -3      -2       -1
list2 = [123, 456, 5653, 2, 21]

print(list1)

for i in list1:
    print(i)

print(list1[-4])

print(list1[0 : 3]) # lay tu 0 den can 3

print(list1[0 :: 3]) #lay 0  va 3

list1.append("hello") #them phan tu vao cuoi list
print(list1)
list1.append(int(input("nhap n can them ")))
print(list1)

list1.insert(0,12102005) #them phan tu vao vi tri trc dau , trong insert cua list
print(list1)

list1.remove(321) #xoa gia tri trong ngoac
print(list1)

list1.pop(0) #xoa gia tri cua phan tu trong ngoac.Neu k them vi tri thi xoa gia tri cuoi cung
print(list1)

list2.sort() # sap xep tanwg dan
print(list2)

list2.reverse() # dao nguoc list
print(list2)

#list2.sort(key=lambda x : x, reverse=False) # sap xep giam dan
#print(list2)

length = len(list1) #kich thuoc list
print(length)

count_2 = list2.count(456) # dem gia tri trong ngoac
print(count_2)

print(list2.index(456)) #tim vi tri cua gia tri trong ngoac

print(min(list2))
print(max(list2))