def multiply(numbers_list, number):

    print(numbers_list, number)



multiply(list(), 1)





subtract = s[0]
    if subtract > 9:
        result = subtract - 9
        print(result)
    else:
        print(subtract)
    subtract1 = s[1]
    if int(subtract1) > 9:
        result1 = subtract1 - 9
        print(result1)
    else:
        print(subtract1)
    subtract2 = s[2]
    if subtract2 > 9:
        result2 = subtract2 - 9
        print(result2)
    else:
        print(subtract2)
    subtract3 = s[3]
    if int(subtract3) > 9:
        result3 = subtract3 - 9
        print(result3)
    else:
        print(subtract3)
    subtract4 = s[4]
    if subtract4 > 9:
        result4 = subtract4 - 9
        print(result4)
    else:
        print(subtract4)
    subtract5 = s[5]
    if int(subtract5) > 9:
        result5 = subtract5 - 9
        print(result5)
    else:
        print(subtract5)
    subtract6 = s[6]
    if subtract6 > 9:
        result6 = subtract6 - 9
        print(result6)
    else:
        print(subtract6)
    subtract7 = s[7]
    if int(subtract7) > 9:
        result7 = subtract7 - 9
        print(result7)
    else:
        print(subtract7)
    subtract8 = s[8]
    if subtract8 > 9:
        result8 = subtract8 - 9
        print(result8)
    else:
        print(subtract8)
    subtract9 = s[9]
    if int(subtract9) > 9:
        result9 = subtract9 - 9
        print(result9)
    else:
        print(subtract9)
    subtract10 = s[10]
    if subtract10 > 9:
        result10 = subtract10 - 9
        print(result10)
    else:
        print(subtract10)
    subtract11 = s[11]
    if int(subtract11) > 9:
        result11 = subtract11 - 9
        print(result11)
    else:
        print(subtract11)
    subtract12 = s[12]
    if subtract12 > 9:
        result12 = subtract12 - 9
        print(result12)
    else:
        print(subtract12)
    subtract13 = s[13]
    if int(subtract13) > 9:
        result13 = subtract13 - 9
        print(result13)
    else:
        print(subtract13)
    subtract14 = s[14]
    if subtract14 > 9:
        result14 = subtract14 - 9
        print(result14)
    else:
        print(subtract14)
def double_each_element():
    a = reverse_digits()
    position = a[0]
    position_2 = a[2]
    position_4 = a[4]
    position_6 = a[6]
    position_8 = a[8]
    position_10 = a[10]
    position_12 = a[12]
    position_14 = a[14]
    double = int(position) * 2
    double1 = int(position_2) * 2
    double2 = int(position_4) * 2
    double3 = int(position_6) * 2
    double4 = int(position_8) * 2
    double5 = int(position_10) * 2
    double6 = int(position_12) * 2
    double7 = int(position_14) * 2

    double_list = [double, a[1], double1, a[3], double2, a[5], double3, a[7], double4, a[9], double5, a[11], double6,
                   a[13], double7]
    print(double_list)
    return double_list


def subtract_list():
    s = double_each_element()
    print(s)
    result = s[0], s[2], s[4], s[6], s[8], s[10], s[12], s[14]
    print(result)






subtract_list()



