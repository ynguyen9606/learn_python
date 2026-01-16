# một số hàm trong module re.
import re
#search().
#findall(): tìm và trả về 1 list các kết quả phù hợp
str = "the AI in rain"
result = re.findall("i",str, re.IGNORECASE) # trả về list các kết quả của chuỗi siêu mẫu bên trong
print(result)

#split(): tìm và trả về 1 list các chuỗi con sau khi tìm thấy và tách chuỗi bởi chính chuỗi muốn tìm
result1 = re.split("\s",str) # trả về list các kết quả của chuỗi siêu mẫu bên trong
print(result1)
result2 = re.split("i",str, 0, re.IGNORECASE)
print(result2)              # nhập số bnh thì sẽ tách bấy nhiêu , nhập 0 thì tách hết, vượt quá số lượng thì vẫn tách như tối đa

#sub() : tìm và thay thế những kết quả phù hợp bằng chuỗi mới
result3 = re.sub(" ", "_", str) # tìm các khoảng space và thay vào là _
print(result3)                  # số lượng tác động cũng hoạt động tương tự như split

# finditer() : tìm và trả về 1 iterator các đối tượng Match phù hợp
result4 = re.finditer("i",str,2)
for match in result4:
    print(match.group(), match.start(), match.end(), match.span(), match.string)