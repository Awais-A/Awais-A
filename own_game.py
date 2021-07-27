# This is ym independant attempt at creating the War game 
# First I will import any useful modules here
import random
# Here is a set for the suits in a deck: Hearts, Spades, Diamonds, Clubs

suits = ('clubs','diamonds','hearts','spades')

# Here is a set for the ranks in a deck

ranks = ('Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Jack','Queen','King','Ace')

# Here is a dictionary to give values to the ranks 

nums = [int for int in range(2,15)]
values = {ranks[i]:nums[i] for i in range(len(nums))}

# Here is a class to create a card

class Card:
    
    def __init__(self,suit,rank) -> None:
        self.suit = suit
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self) -> str:
        return f'{self.rank} of {self.suit}'

# Here is a class to create the whole deck

class Deck:
    
    def __init__(self) -> None:
        
        self.all_cards = []
        
        for suit in suits:
            for rank in ranks:
                created_card = Card(suit,rank)
                self.all_cards.append(created_card)
    
    def shuffle(self):
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        return self.all_cards.pop()

# Here is a class for the Player

class Player:
    
    def __init__(self, name):
      self.name = name
      self.all_cards = []
      
    def remove_one(self):
        return self.all_cards.pop(0)
    
    def add_cards(self,new_cards):
        if type(new_cards) == type([]):
            self.all_cards.extend(new_cards)
        else:
            self.all_cards.append(new_cards)
            
    def __str__(self) -> str:
        return f'Player {self.name} has {len(self.all_cards)} cards remaining.'

# Game logic

player_one = Player('One')
player_two = Player('Two')

new_deck = Deck()
new_deck.shuffle()

for i in range(26):
    player_one.add_cards(new_deck.deal_one())
    player_two.add_cards(new_deck.deal_one())

round_num = 0
game_on = True

while game_on:
    round_num +=1
    print(f'Round {round_num}!')
    
    if len(player_one.all_cards) == 0:
        print('Player One is all out of cards!')
        print('Congratulations Player Two! You have won!')
        game_on = False
        break
    
    if len(player_two.all_cards) == 0:
        print('Player Two is all out of cards!')
        print('Congratulations Player One! You have won!')
        game_on = False
        break
    
    player_one_cards = []
    player_one_cards.append(player_one.remove_one())
    
    player_two_cards = []
    player_two_cards.append(player_two.remove_one())
    
    if player_one_cards[-1].value > player_two_cards[-1].value:
        player_one.add_cards(player_one_cards)
        player_one.add_cards(player_two_cards)
    elif player_one_cards[-1].value < player_two_cards[-1].value:
        player_two.add_cards(player_two_cards)
        player_two.add_cards(player_one_cards)
    else:
        at_war =  True
        
        while at_war:
            print('WAR!')
            if len(player_one.all_cards) < 5:
                print('Player One unable to declare war!')
                print('Congratulations Player Two! You win!')
                game_on = False
                break
            elif len(player_two.all_cards) < 5:
                print('Player Two unable to declare war!')
                print('Congratulations! Player One wins!')
                game_on = False
                break
            else:
                for i in range(5):
                    player_one_cards.append(player_one.remove_one())
                    player_two_cards.append(player_two.remove_one())
                     