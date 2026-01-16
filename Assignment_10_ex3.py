import re
local_number = "(0123)1234567"

if re.search(r"^\(0[0-9]{1,3}\)[0-9]{5,7}$",local_number):
    print(f"{local_number} -> True")
else:
    print(f"{local_number} -> False")