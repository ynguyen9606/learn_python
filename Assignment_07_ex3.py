text = "X-DSPAM-Confidence: 0.8475"

find_the_colon = text.find(':')

number_str = text[find_the_colon+1:].strip()

number = float(number_str)

print(number)
def test():
  a = range(5)
  print(a)
test()