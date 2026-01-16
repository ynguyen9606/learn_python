import re

str = "rain the rain in Viet Nam"

#-----search-----
result1 = re.search("rain", str)
print(result1)

# meta character:
#  ^ : đặt ở đầu chuỗi mẫu=> ký tự hoặc cụm ký tự ngây sau nios pahir xuất hiện ở đầu tiên trong chuỗi
result2 = re.search("^rain", str)
print(result2)

#  $ : đặt ở cuối chuỗi mẫu=> ký tự /cụm ký tự ngay trước nó phải xuất hiện ở cuối chuỗi
result3 = re.search("Nam$", str)
print(result3)

#  * : ký tự hoặc cụm ký tụ ngay trc nó xuất hiên 0  hoặc nhiều lần 
str1 = ""
result4 = re.search("^r*$",str1)
print(result4)

#  + : ký tự hoặc cụm ký tụ ngay trc nó xuất hiên 1  hoặc nhiều lần 
str2 = "rrrrrrxrrr"
result5 = re.search("^r+$",str)
print(result5)

#  . : tương đương với 1 ký tự bất kỳ  a.b giữa a và b là có ký tự khác
str3 = "acxcxcxcxb"
result6 = re.search("^a.*b$",str3)
print(result6)

# () : tạo cymj kysy tự trong nó (absdc)
result7 = re.search("^a(cx)*",str3)
print(result7)

#  ? : ký tự hoặc cụm ký tự ngay trước nó xuất hiện 0 hoặc chỉ 1 lần
str4 = "acx"
result8 = re.search("^a(cx)?$",str4)
print(result8)

#  {n} : ký tự hoặc cụm ký tự ngay trước nó xuất hiện đúng n lần
str5 = "acxcxcxcx"
result8 = re.search("^a(cx){4}$",str5)
print(result8)

#  {n,} : ký tự hoặc cụm ký tự ngay trước nó xuất hiện ít nhất n lần
result9 = re.search("^a(cx){3,}$",str5)
print(result9)

#  {,m} : ký tự hoặc cụm ký tự ngay trước nó xuất hiện nhiều nhất m lần
result10 = re.search("^a(cx){,5}$",str5)
print(result10)

#  {n,m} : ký tự hoặc cụm ký tự ngay trước nó xuất hiện từ m đến n lần
result11 = re.search("^a(cx){3,5}$",str5)
print(result11)

#  | : a|b => a hoặc b , (abc)|(cdg)=> abc hoặc cdg
str6 = "hjhhjhjhhjahjhjhkj$h"
result12 = re.search("a|b",str6)
print(result12)
result13 = re.search("(hk)|(ah)",str6)
print(result13)

#  \ : đặt trước ký tự đặc biệt => ký tự thường
str7 = "k.h5     "
result14 = re.search("k\.h",str7)
print(result14)

#  \ : kết hợp với một số ký tự khác => ký tự đặc biệt
# \d : là 1 chữ số bất kỳ từ 0 -9
result15 = re.search("\d",str7)
print(result15)

#  \D : la 1 ký tự bất kỳ nhưng không phải là chữ số
result16 = re.search("\D",str7)
print(result16)

#  \s : là ký tự cách(space) hoặc là tab hoặc là xuống dòng 
result17 = re.search("\s",str7)
print(result17)

#  \S : là ký tự baasrt kỳ nhưng không phải là space , tab, xuống dòng
result18 = re.search("\S",str6)
print(result18)

#  \w : là ký tự in thường a-z, hoặc in hoa A-Z, hoặc số từ 0-9, hoặc _

str8 = "\t\n Â_"
result18 = re.search("\w", str8)
print(result18)

#  \W : là ký tự bất kỳ nhưng không phải là a-z, A-Z, 0-9, hoặc _
result19 = re.search("\W",str8)
print(result19)

#  \A : tương đương với ^
result20 = re.search("\A\W",str8)
print(result20)

#  \Z : tương đương với $
result21 = re.search("Nam\Z", str)
print(result21)

#  \b : ký tự sau nó thì phải có ở đầu cụm trong chuỗi và ngược lại, không tìm cùng 1 lúc 2 vị trí
str9 = "aPythona h_ahah1"
result22 = re.search(r"\ba",str9)
print(result22)

#  #B : tìm ký tự đặt trước và sau nó
result23 = re.search("_\B",str9)
print(result23)

#  [] : là 1 ký tự trong các ký tự nằm trong nó ,[abc] tương đương với a hoặc b hoặc c
result24 = re.search("[yo]",str9)
print(result24)
 
#  [a-z] : tương đương với Ký tự in thường 
#  [A-Z] : tương đương với Ký tự in hoa
#  [0-9] : tương đương với Ký số
#  [1-5] :
#  [a-zA-Z0-9_] : <=> |w
#  [^] : tương đương với 1 ký tự bất kỳ nhưng không nằm trong nó [^abc]
result25 = re.search("^[^ayo]",str9)
print(result25)