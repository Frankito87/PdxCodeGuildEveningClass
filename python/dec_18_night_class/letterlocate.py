
def letterlocate(string, letter):

    #string = list(input("Enter a phrase or word: "))
    #print(string)

    #letter = input("Enter a letter: ")

    #letter.split()

    new_list = []

    while letter in string:

        ind = string.index(letter)

        new_list.append(ind)

        string[ind] = '-'

    print(new_list)


letterlocate(list('apple'), 'p')

