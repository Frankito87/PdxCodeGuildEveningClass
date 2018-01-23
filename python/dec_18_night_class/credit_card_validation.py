string = "Welcome to the Pseudo Credit Card Validation program.!! "
print(string.center(100, " "))


card = list(input("Enter a valid credit card number, remember this need to have 16 digits: "))

print(card)


def check_digit():
    save_digit = card[-1]
    print(save_digit)

    return check_digit()


def reverse_digits():
    card.pop(-1)
    reverse = card[::-1]
    # print(reverse)
    return reverse


def double_each_element():
    double = reverse_digits()
    print(double)
    double_final = []
    for number in range(len(double)):
        if number % 2 == 0:
            double_final.append(int(double[number]) * 2)
        else:
            double_final.append(int(double[number]))

    return double_final


def subtract():
    s = double_each_element()
    print(s)
    subtract1 = []
    for i in s:
        if i > 9:
            # print(i)
            subtract1.append(int(i) - 9)
            i += 1
        else:
            subtract1.append(i)

    return subtract1


def sum_element():
    add = subtract()
    print(add)
    sum_list = add[0] + add[1] + add[2] + add[3] + add[4] + add[5] + add[6] + add[7] + add[8] + add[9] + add[10]

    return sum_list



