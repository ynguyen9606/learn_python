import re

str = """Phuong is 5 years old, and her sister Lan is 2 years old.

Thuy and Long, their parents, have 3 kids."""

names = re.findall(r"\b[A-Z][a-z]+\b",str)# nếu dùng search thì chỉ trả về 1 tên, k tạo list names được
print(names)