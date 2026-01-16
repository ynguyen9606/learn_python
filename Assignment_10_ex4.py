import re

pattern = r"^(?!.*ab)(?=.*[ab])[a-z]*$"

tests = ["a", "bbb", "ba", "ab", "cabd", "xyz"]

for s in tests:
    print(s, bool(re.search(pattern, s)))
