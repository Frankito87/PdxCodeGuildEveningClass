
class String:

    def __init__(self, first_word, second_word):
        self.first = first_word
        self.second = second_word

    def str(self):
        self.first = input("Enter a first word: ")
        self.second = input("Enter a second word: ")

        lst = self.first.split(" ") + self.second.split(" ")
        print("-".join(lst))
        self.play_again()

    def play_again(self):
        a = input("Do you like to play again: ").lower()

        if a in 'yes':
            self.str()
        elif a in 'no':
            quit()
        else:
            print(" I did not understand that! ")


word = String('Frank', 'Ramos')
word.str()
