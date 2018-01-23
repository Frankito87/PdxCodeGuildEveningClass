# f = open('scratch.txt', 'r')
#
# # print(type(f.read()))
# lines = f.readlines()
# f.close()
#
# for line in lines:
#     print(line, end='')
#
# # f = open('scratch.txt', 'w')
# # new_lines = ['I took your milkshake!\n', '\n', 'I DRANK IT UP!\n']
# # for line in new_lines:
# #     f.write(line)
# # f.close()
#
# f = open('scratch.txt', 'a')
# new_lines = ['\nI took your milkshake!\n', '\n', 'I DRANK IT UP!\n']
# for line in new_lines:
#     f.write(line)
# f.close()
from random import randrange as a


with open('test.txt', 'r') as f:
    lines = f.readlines()

for line in lines:
    print(line, end='')

# with open('scratch.txt', 'w') as file:
#     new_lines = ['I took your milkshake!\n', '\n', 'I DRANK IT UP!\n']
#
# for line in new_lines:
#     file.write(line)

with open('test.txt', 'a') as a_file:
    new_lines = lines

    for line in new_lines:
        a_file.write(line)
