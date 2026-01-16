#danh sach chieu cao cua hs .tim chieu cao trung nhau nhieu nhat ,in so luong va so chieu cao ay

height = (123, 127, 123, 134, 127, 123, 156, 132, 123)
list = [123, 127, 134, 156, 132]

count_height = 0
height_max = 0

for i in list:
    if height.count(i) > count_height:
        count_height = height.count(i)
        height_max = i
print(count_height, height_max)