li = [1, 134, 98, 77, 88.4, -197, 33, -89, -199.5, -978, 625, -121, 121, 121.01]

for i in li:
    if type(i) == int and i < 0 and i % 2 != 0:
        print(i)