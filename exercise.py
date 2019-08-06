def write_dictionary():
    new_dictionary = {}

    for num in range(1,51):
        if (num % 2 == 0) and (num % 7 == 0):
            # print(f'A - {num}: {num * 2}')
            new_dictionary[num] = num * 2
        elif (num % 7 == 0):
            # print(f'B - {num}: {num - 1}')
            new_dictionary[num] = num - 1
        elif (num % 2 == 0):
            # print(f'C - {num}: {num + 1}')
            new_dictionary[num] = num + 1
        else:
            # print(f'D - {num}: {num}')
            new_dictionary[num] = num

    return new_dictionary

print(write_dictionary())