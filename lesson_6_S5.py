# đối tượng match : chứa thông tin về kết quả tìm kiếm ,nếu k tìm thấy sẽ trả về none

import re
str = "0399-254139"
result = re.search("^(\d{4})-(\d{6})$",str)
print(result.span()) # cho biết tọa độ cảu result trên(đếm từ 0)
print(result.start()) # cho biết vị trí bắt đầu
print(result.end()) # cho biết vị trí kết thúc 
print(result.group(1)) # cho biết chuỗi mẫu àm ta muốn tìm ở result
print(result.group(2))
print(result.string) # cho biết chuỗi gốc mà ta muốn tìm
 