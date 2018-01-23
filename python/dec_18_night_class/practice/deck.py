from card import Card
from random import shuffle


class Deck:
    suit = ['Clubs', 'Diamonds', 'Hearts', 'Spades']
    name_values = {'ACE': 11, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, 'J': 10,
                   'Q': 10, 'K': 10}

    def __init__(self, num_decks=6):
        self.deck = self.create_deck(num_decks)
        self.shuffle_deck()

    def create_deck(self, number_decks):
        temp_deck = []
        for n in range(number_decks):
            for s in self.suit:
                for r, v in self.name_values.items():
                    temp_deck.append(Card(s, r, v))

        return temp_deck

    def shuffle_deck(self):
        shuffle(self.deck)

    def deal_card(self):
        return self.deck.pop()


if __name__ == '__main__':
    d = Deck()
    print(d.deck)