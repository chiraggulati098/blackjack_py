import random   #imported random to use the shuffle function

'''
Setup a few global variables
Ranks and value for the cards
Playing for the game continuing till True
Credit for making the chips won/lost effect the next round if the person plays another round
'''
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two': 2, 'Three': 3, 'Four': 4, 'Five': 5, 'Six': 6, 'Seven': 7, 'Eight': 8, 'Nine': 9, 'Ten': 10, 'Jack': 10, 'Queen': 10, 'King': 10, 'Ace': 11}
playing = True
credit = 100

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

    def __init__(self,chips = 100):
        
        self.chips = chips
        self.bet = 0
        self.hand = []
        self.value = 0
        self.aces = 0

    def add_card(self,card):
        self.hand.append(card)
        self.value += values[card]
        if card == 'Ace':
            self.aces += 1

    def adjust_for_ace(self):
        while self.value > 21 and self.aces:
            self.value -= 10
            self.aces -= 1

    def win_bet(self):
        self.chips += self.bet

    def lose_bet(self):
        self.chips -= self.bet

def take_bet(player):
    while True:
        try:
            player.bet = int(input("How many chips would you like to bet? "))
        except:
            print("Please provide an Integer Value!")
        else:
            if player.bet > player.chips:
                print(f'Sorry, you do know have enough chips! You have: {player.chips}')
            else:
                break

def show_some(player,dealer):
    print(f"\nDealer's Hand:\n {dealer.hand[0]} Other Card Hidden\n")
    print("Player's Hand: ")
    for card in player.hand:
        print(card)
    print(f"Value of Player's Hand = {player.value}")

def show_all(player,dealer):
    print("\nDealer's Hand: ")
    for card in dealer.hand:
        print(card)
    print(f"Value of Dealer's Hand = {dealer.value}")
    print("\nPlayer's Hand: ")
    for card in player.hand:
        print(card)
    print(f"Value of Player's Hand = {player.value}")

def hit(deck,player):
    single_card = deck.deal()
    player.add_card(single_card)
    player.adjust_for_ace()

def hit_or_stand(deck,player):
    
    global playing 

    while True:
        x = input('Hit or Stand? Enter h or s:')
        if x[0].lower() == 'h':
            hit(deck,player)
        elif x[0].lower() == 's':
            print("Player Stands Dealer's Turn")
            playing = False
        else:
            print("Sorry, I did not understand that, Please enter h or s only")
            continue
        break

def player_busts(player,dealer):
    print("BUST PLAYER!")
    player.lose_bet()

def player_wins(player,dealer):
    print("PLAYER WINS!")
    player.win_bet()

def dealer_busts(player,dealer):
    print("PLAYER WINS! DEALER BUSTED!")
    player.win_bet()

def dealer_wins(player,dealer):
    print("DEALER WINS!")
    player.lose_bet()

def push(player,dealer):
    print("Dealer and Player tie! PUSH")

while True:

    print("WELCOME TO BLACKJACK!")

    deck = Deck()
    deck.shuffle_deck()

    player = Player(credit)
    player.add_card(deck.deal())
    player.add_card(deck.deal())

    dealer = Player()
    dealer.add_card(deck.deal())
    dealer.add_card(deck.deal())

    take_bet(player)

    show_some(player,dealer)

    while playing:
        
        hit_or_stand(deck,player)
        show_some(player,dealer)

        if player.value > 21:
            player_busts(player,dealer)
            break
    
    if player.value <= 21:

        while dealer.value < 17:
            hit(deck,dealer)

        show_all(player,dealer)

        if dealer.value > 21:
            dealer_busts(player,dealer)
        elif dealer.value < player.value:
            player_wins(player,dealer)
        elif dealer.value > player.value:
            dealer_wins(player,dealer)
        else:
            push(player,dealer)
        
    print(f"\nPlayer total chips are at: {player.chips}")
    credit = player.chips

    if credit == 0:
        print("You have lost all your money.\nThanks for Playing!")
        break

    new_game = input("Would you like to play another hand? ")

    if new_game[0].lower() == 'y':
        playing = True
        continue
    else:
        print("Thank You for playing!")
        break