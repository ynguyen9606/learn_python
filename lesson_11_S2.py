dictionary = {"name":"Tuan", "age":"eighteen", "gender":"Male"}
dictionary_1 = {"ten":"Tuan", "tuoi":"18", "gioi_tinh":"nam"}
# luu tru cac cap key:value,cac cap cach nhau dau phay

print(dictionary)

print(dictionary["name"]) # dung key de goi value

dictionary["Address"] = "Danang" #them gia tri
print(dictionary)

del dictionary["Address"] #, dictionary["gender"]       xoa gia tri 
# dictionary.pop("gender")
print(dictionary)

for i, information in enumerate(dictionary):
    print(i, information)

for d , d1 in zip(dictionary, dictionary_1): #nối cac key: value cua 2 dictionary  
    print(d, dictionary[d],"---" ,d1, dictionary_1[d1])

for v in dictionary.values():
    print(v)

for k in dictionary.keys():
    print(k)

for i in dictionary.items():
    print(i)
for i, k in dictionary.items():
    print(i,":", k)




dictionary_3 = dictionary.copy()
dictionary.clear()
print(dictionary_3)
print(dictionary)

dictionary_4 = dict.fromkeys(dictionary_1,"ahihi")# sao chep cac key va cac value se la none
print(dictionary_4)

d = dictionary_1.get("tenm",123) #tro den key trong dictionary ,neu dung key se tra ve value cua no ,
#   neu sai key se tra none or 1 value moi sau dau phay,get không tac dong den key or value mà chi truy suat value
print(dictionary_1)

dictionary_1.setdefault("nghe",567) # tim neu co key thi giu nguyen value,neu key la thi them vao dictionary va them value sau dau phay or none
print(dictionary_1)