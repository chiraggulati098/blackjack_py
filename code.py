import random

ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}

class Deck():

    def __init__(self):
        self.deck = []
        for _ in range (0,4):
            for x in ranks:
                self.deck.append(x)
    
    def __str__(self):
        for card in self.deck:
            print(card+'\n')

    def shuffle_deck(self):
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()
        return single_card
    
class Player():

    def __init__(self,name,chips = 100):
        
        self.name = name
        self.chips = chips