import random

string = "Welcome to a BlackJack game!!"
print(string.center(50, " "))


class Card:
    def __init__(self, suit, rank, value=0):
        self.suit = suit
        self.rank = rank
        self.value = value


class Deck:
    suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    name_values = {'A: 11', '2:2', '3:3', '4:4', '5:5', '6:6', '7:7', '8:8', '9:9', '10:10', 'J:10', 'Q:10', 'K:10'}

    def __init__(self, num_decks = 6):
        self.deck = self.create_deck(num_decks)
        self.shuffle_deck()

        def create_deck(self, number_decks):
            temp_deck = []
            for n in range(number_decks):
                for s in self.SUIT:
                    for r, v in self.NAME_VALUE.items():
                        temp_deck.append(Card(s, r, v))
            return temp_deck

        def shuffle_deck(self):
            shuffle(self.deck)

        def deal_card(self):
            return self.deck.pop()

    if __name__ == '__main__':
        d = Deck()
        print(d.deck)

    
class Hand:
    def __init__(self, collection_of_cards):
        self.collection = collection_of_cards
        self.card = Card

    def add_card(self):
        pass

    def user_type(self):
        pass


class Game:
    def __init__(self):
        pass

    def new_game(self):
        a = input("Do you want to start a new game (y/n): ")
        if a in 'yes':
            pass
        elif a in 'no':
            print("GoodBye!!")
            quit()

        else:
            print("I do not understand that.!!")

    def score(self):
        pass

    def bust(self):
        pass
