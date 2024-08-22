def findComplement(num: int) -> int:
    new_number = ''
    binary_number = bin(num)
    for i in binary_number[2:]:
        if i == '0':
            new_number += '1'
        if i == '1':
            new_number += '0'
    return int(new_number, 2)


print(findComplement(10))
