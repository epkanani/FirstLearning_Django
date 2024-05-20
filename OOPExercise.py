# OOP exercise project

# -------Libraries-----------
from random import shuffle


# --------Code begins here-----

# Two variables for creating cards
SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

# Deck class 
class Deck:
    def __init__(self):
        print('created deck class')
        # create deck of cards
        self.allcards = [(s,r) for s in SUITE for r in RANKS]
        # print(self.allcards)
        
    # shufle cards
    def shuffle(self):
        shuffle(self.allcards)
            
    # split the cards into two 
    def split_into_two(self):
        # #Print out an array
        # print('first deck: {}'.format(str(self.allcards[:26])))
        return (self.allcards[:26],self.allcards[26:])
                
# hand class 
class Hand:
    def __init__(self,cards):
        self.cards = cards
        
    # print the hand 
    def __str__(self):
        return 'contains {} cards'.format(len(self.cards))
    
    # new mehtod add to cards
    def Add(self,added_cards):
        self.cards.extend(added_cards)
          
    # remove cards 
    def remove_card(self):
        return self.cards.pop()

# player class 
class Player:
    def __init__(self,name,hand):
        self.name = name
        self.hand = hand
        
    # play card function
    def play_card(self):
        drawn_card = self.hand.remove_card()
        print('\n')
        print('{} has placed: {}'.format(self.name,drawn_card))
        
    def remove_war_cards(self):
        war_cards = []
        # if player has less than two cards left
        if len(self.hand.cards) < 3:
            return self.hand.cards
        else:
            for x in range(3):
                war_cards.append(self.hand.remove_card())
            return war_cards
        
    # check to see if play still has cards
    def still_has_cards(self):
        """
        Return True if player still has cards left
        """
        return len(self.hand.cards) != 0
    
# -------Code test------- 
# mytest = Deck()

# create a new deck and split in half 
D = Deck()
D.shuffle()
# tuple half 
half1,half2 = D.split_into_two()

# create computer play and user 
comp = Player('computer',Hand(half1))
name = input('your name?')
user =Player(name,Hand(half2))

# set round counts
total_rounds = 0
war_count = 0

while user.still_has_cards() and comp.still_has_cards():
    total_rounds += 1
    print('here are the current standings of the round')
    print(user.name+'has the coun:'+str(len(user.hand.cards)))
    print(comp.name+'has the coun:'+str(len(comp.hand.cards)))
    print('play a card')
    print('\n')
    
    # cards on the table
    table_cards = []
    
    # play cards
    c_card = comp.play_card()
    p_card = user.play_card()

    
    # add to table of cards
    table_cards.append(c_card)
    table_cards.append(p_card)
    
    # check war use matching rankings
     # Check for War!
    if c_card[1] == p_card[1]:
        war_count +=1
        print("We have a match, time for war!")
        print("Each player removes 3 cards 'face down' and then one card face up")
        table_cards.extend(user.remove_war_cards())
        table_cards.extend(comp.remove_war_cards())

        # Play cards
        c_card = comp.play_card()
        p_card = user.play_card()

        # Add to table_cards
        table_cards.append(c_card)
        table_cards.append(p_card)

        # Check to see who had higher rank
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(user.name+" has the higher card, adding to hand.")
            user.hand.add(table_cards)
        else:
            print(comp.name+" has the higher card, adding to hand.")
            comp.hand.add(table_cards)

    else:
        # Check to see who had higher rank
        if RANKS.index(c_card[1]) < RANKS.index(p_card[1]):
            print(user.name+" has the higher card, adding to hand.")
            user.hand.add(table_cards)
        else:
            print(comp.name+" has the higher card, adding to hand.")
            comp.hand.add(table_cards)
            
print('game over, number of rounds'+str(total_rounds))
print('a war happend'+str(war_count)+'times')