with open("test_6_S8.txt", "a+") as file:
    file.write("ABC")
    file.seek(0)
    content = file.read()
    print(content)

