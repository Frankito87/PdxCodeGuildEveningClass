# class Bankaccount():

#    def account(self, balance):
#        self.balance = balance

#    def check_balance(self):
#        return self.balance

# acc1 = Bankaccount(500)

# b =


# import string

word_count = {}

text = 'I like to pet puppies I also like to pet kittens'

text = text.lower()

text_list = text.split()

for word in text_list:
    if word not in word_count:
        word_count[word] = 1
    else:
        # word_count[word] = word_count[word] + 1
        word_count[word] += 1

for word, times in word_count.items():
    print('"{}" seen {} times.'.format(word, times))
#
# alpha = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
# rot_13 = list(string.ascii_lowercase[13:] + string.ascii_lowercase[:13])
#
# word = 'Hat'.lower()
# new_word = ''
# for letter in word:
#     i = alpha.index(letter)
#     # new_word = new_word + rot_13[i]
#     new_word += rot_13[i]
#     # print(rot_13[i])
#
# print(new_word)
import random
# list_o_nums = [2, 3, 7, 3, 5, 756, 2345, 554, 7]
# list_o_nums_copy = list_o_nums.copy()
#
# for n in list_o_nums:
#     list_o_nums_copy.append(n)
# print(list_o_nums_copy)


# num = 0
# while num < 1000:
#     num += 1
#     print(num)
#     print()

# while True:
#     q = input('Enter 1 to yell, 2 to whisper or 3 to quit...: ')
#     if q == '1':
#         print('HELLO')
#     elif q == '2':
#         print('**hello**')
#     elif q == '3':
#         quit()
#         # break
#
# print('With break we will see this.')


for i in range(20):
    num = random.randrange(1, 7)
    if num % 2 == 0:
        # continue
        break
    print(num)
