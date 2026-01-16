import re
test_String = "+84123456788"

#1
if re.search(r"^(0|\+84)", test_String):
    print(f'String {test_String} -> has 0 or +84')
else:
    print(f'String {test_String} -> hasn`t 0 or +84')

#2
if re.search(r"^(0|\+84)[0-9]{9}$", test_String):
    print(f'String {test_String} -> has 9 nums')
else:
    print(f'String {test_String} -> hasn`t 9 nums')