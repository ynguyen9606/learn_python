import re
 
test_string = "SScomcomcom%(@#$)(@#$)"
#pattern = r'^S{1,3}(com){3,}%?(@#\$){2}$'
#
#result = re.search(pattern, test_string)
#
#if result:
#    print("Chuỗi HỢP LỆ")
#else:
#    print("Chuỗi KHÔNG hợp lệ")
#1
if re.search(r"^S{1,3}", test_string):
    print(f'test: {test_string} -> has 1-3 characters "S"')
else:
    print(f'test: {test_string} -> hasn`t 1-3 characters "S"')

#2 
if re.search(r"(com){3,}", test_string):
    print(f'test: {test_string} -> There are at least 3 "com" characters')
else:
    print(f'test: {test_string} -> There aren`t at least 3 "com" characters')

#3
if re.search(r"(com){3,}%?", test_string):
    print(f'test: {test_string} -> has 0 or 1 characters "%" after "com"')
else:
    print(f'test: {test_string} -> hasn`t 0 or 1 characters "%" after "com"')

#4
if re.search(r"(\(@#\$\)){2}$", test_string):
    print(f'test: {test_string} -> has 2 characters "(@#$)"')
else:
    print(f'test: {test_string} -> hasn`t 2 characters "(@#$)"')