def input_num(num, min_num = 10, max_num = 10**15):
    while True:
        try:
            num = int(input(f'nhap so {num} = '))

            if num < min_num:
                print(f"{num} phải >= {min_num}")
            elif max_num is not None and num > max_num:
                print(f"{num} phải <= {max_num}")
            else:
                return num

        except ValueError:
            print("Sai dinh dang, nhap lai: ")
        

def  generate_num_divisible_4(N):
    N = str(N)
    count_num = len(N)

    pairs_num_divisible_4 = [f"{i:02d}" for i in range(0, 100, 4)]

    num_find = None

    for last_2_num in pairs_num_divisible_4:
        count_num_changes = (N[-2] != last_2_num[0]) + (N[-1] != last_2_num[1])

        if count_num_changes > 2:
            continue

        previous_num_part = list(N[:-2])
        num_can_change = 2 - count_num_changes

        for i in range(count_num - 2):
            if num_can_change <= 0:
                break
            if i == 0:
                final_num_change = "1"
            else:
                final_num_change = "0"
            if previous_num_part[i] != final_num_change:
                previous_num_part[i] = final_num_change
                num_can_change -= 1
            
        new_num = "".join(previous_num_part) + last_2_num

        if new_num[0] == "0":
                continue

        if num_find is None or int(new_num) < int(num_find):
                num_find = new_num
            
    print("so moi nho nhat sau khi thay doi 2 chu so co the chia het cho 4 la: ",num_find)


N = input_num("N")
print(f'so N ban dau la: {N}')
generate_num_divisible_4(N)