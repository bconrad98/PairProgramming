#  File: Poker.py
#  Description: Plays Poker with OOP
#  Student Name: Matthew Frangos
#  Student UT EID: msf955
#  Partner Name: Braeden Conrad
#  Partner UT EID: bsc875
#  Course Name: CS 313E
#  Unique Number: 51335
#  Date Created: 2/5/2018
#  Date Last Modified: 2/10/2018
import random

class Card (object):
  RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

  SUITS = ('C', 'D', 'H', 'S')

  def __init__ (self, rank = 12, suit = 'S'):
    if (rank in Card.RANKS):
      self.rank = rank
    else:
      self.rank = 12

    if (suit in Card.SUITS):
      self.suit = suit
    else:
      self.suit = 'S'

  def __str__ (self):
    if (self.rank == 14):
      rank = 'A'
    elif (self.rank == 13):
      rank = 'K'
    elif (self.rank == 12):
      rank = 'Q'
    elif (self.rank == 11):
      rank = 'J'
    else:
      rank = str (self.rank)
    return rank + self.suit

  def __eq__ (self, other):
    return (self.rank == other.rank)

  def __ne__ (self, other):
    return (self.rank != other.rank)

  def __lt__ (self, other):
    return (self.rank < other.rank)

  def __le__ (self, other):
    return (self.rank <= other.rank)

  def __gt__ (self, other):
    return (self.rank > other.rank)

  def __ge__ (self, other):
    return (self.rank >= other.rank)

class Deck (object):
  def __init__ (self):
    self.deck = []
    for suit in Card.SUITS:
      for rank in Card.RANKS:
        card = Card (rank, suit)
        self.deck.append (card)

  def shuffle (self):
    random.shuffle (self.deck)

  def deal (self):
    if (len(self.deck) == 0):
      return None
    else:
      return self.deck.pop(0)

class Poker (object):
  def __init__ (self, num_players):
    self.deck = Deck()
    self.deck.shuffle()
    self.players = []
    numcards_in_hand = 5

    for i in range (num_players):
      hand = []
      for j in range (numcards_in_hand):
        hand.append (self.deck.deal())
      self.players.append (hand)

  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.players)):
      sortedHand = sorted (self.players[i], reverse = True)
      self.players[i] = sortedHand
      hand = ''
      for card in sortedHand:
        hand = hand + str (card) + ' '
      print ('Player ' + str (i + 1) + " : " + hand)
    ''' TEST CASE IF 6 PLAYERS
    c1=Card(14,"S")
    c2=Card(14,"H")
    c3=Card(11,"S")
    c4=Card(11,"S")
    c5=Card(10,"S")
    self.players[5]=[ c1,c2,c3,c4,c5 ]
    
    hand=''
    for card in self.players[5]:
        hand = hand + str (card) + ' '
    print ('Player ' + str (6) + " : " + hand)
	'''
    # determine the each type of hand and print
    print()
    points_hand = []  # create list to store points for each hand
    h_hand = [] # create a list for h's
    h=0
    str_result=''
    # search through all players
    for j in range(0, len(self.players)):
      # Determine if Royal Flush
      if (self.is_royal(self.players[j])):
        h=10
        str_result=("Player "+ str(j+1) + ': ' + 'Royal Flush')
      
      # Determine if Straight Flush  
      elif(self.is_straight_flush(self.players[j])):
        h=9
        str_result=("Player "+ str(j+1) + ': ' + 'Straight Flush')
      
      # Determine if 4 of a kind, and reverse cards for points algorithm
      elif(self.is_four_kind(self.players[j])):
        h=8
        str_result=("Player "+ str(j+1) + ': ' + 'Four of a Kind')
        temp_hand = self.players[j]
        if (temp_hand[0] != temp_hand[1]):
            temp_hand.reverse()
        self.players[j] = temp_hand
      
      # Determine if full house, and re-order cards for points algorithm  
      elif(self.is_full_house(self.players[j])):
        h=7
        str_result=("Player "+ str(j+1) + ': ' + 'Full House')
        temp_hand = self.players[j]
        if (temp_hand[2]!=temp_hand[3]):
            temp_hand.reverse()
        self.players[j] = temp_hand
      
      # Determine if hand is a flush
      elif(self.is_flush(self.players[j])):
        h=6
        str_result=("Player "+ str(j+1) + ': ' + 'Flush')
      
      # Determine if hand is a straight
      elif(self.is_straight(self.players[j])):
        h=5
        str_result=("Player "+ str(j+1) + ': ' + 'Straight')
      
      # Determine if hand is 3 of a kind, and re-order cards for points algorithm 
      elif(self.is_three_kind(self.players[j])):
        h=4
        str_result=("Player "+ str(j+1) + ': ' + 'Three of a Kind')
        temp_hand = []
        for i in range(len(self.players[j])-2):
            if (self.players[j][i]==self.players[j][i+1]):
                temp_hand = self.players[j][i:i+3]
                if (i==1):
                    temp_hand.append(self.players[j][0])
                    temp_hand.append(self.players[j][4])
                elif (i==2):
                    temp_hand.append(self.players[j][0])
                    temp_hand.append(self.players[j][1])
                elif (i==0):
                    temp_hand = self.players[j]
        self.players[j] = temp_hand
      
      # Determine if two pair, and re-order cards for points algorithm 
      elif(self.is_two_pair(self.players[j])):
        h=3
        str_result=("Player "+ str(j+1) + ': ' + 'Two Pair')
        temp_hand = []
        i=0
        # Search for index location of the non- paired value
        while(i < 4 and self.players[j][i]==self.players[j][i+1]):
            i+=2
        if (i==0):
            temp_hand=self.players[j][1:5]
        elif (i==2):
            temp_hand=self.players[j][0:2]
            temp_hand.append(self.players[j][3])
            temp_hand.append(self.players[j][4])
        elif (i==4):
            temp_hand=self.players[j][0:4]
        temp_hand.append(self.players[j][i])
        self.players[j] = temp_hand
      
      # Determine if one pair, and re-order cards for points algorithm 
      elif(self.is_one_pair(self.players[j])):
        h=2
        str_result=("Player "+ str(j+1) + ': ' + 'One Pair')
        temp_hand = []
        i=0
        # Search for index location of the paired value
        while(i < 4 and self.players[j][i]!=self.players[j][i+1]):
            i+=1
        if (i==0):
            temp_hand = self.players[j][0:2]
            temp_hand.append(self.players[j][2])
            temp_hand.append(self.players[j][3])
            temp_hand.append(self.players[j][4])
        elif (i==1):
            temp_hand = self.players[j][1:3]
            temp_hand.append(self.players[j][0])
            temp_hand.append(self.players[j][3])
            temp_hand.append(self.players[j][4])
        elif (i==2):
            temp_hand = self.players[j][2:4]
            temp_hand.append(self.players[j][0])
            temp_hand.append(self.players[j][1])
            temp_hand.append(self.players[j][2])
            temp_hand.append(self.players[j][4])
        elif (i==3):
            temp_hand = self.players[j][3:5]
            temp_hand.append(self.players[j][0])
            temp_hand.append(self.players[j][1])
            temp_hand.append(self.players[j][2]) 
        self.players[j] = temp_hand

      elif(self.is_high_card(self.players[j])):
        h=1
        str_result=("Player "+ str(j+1) + ': ' + 'High Card')
      print (str_result)
      points = h * 13**5 + (self.players[j][0]).rank * 13**4 + (self.players[j][1]).rank * 13**3 + (self.players[j][2]).rank * 13**2 + (self.players[j][3]).rank * 13 + (self.players[j][4]).rank
      # print (points) # for verification
      points_hand.append(points) # Index of total points value
      h_hand.append(h)  # Index of h values

    # determine winner and print
    print()
    Max = max(h_hand)
    tie_list = []
    count_max = 0
    # Finds max based on h value
    for i in range(len(h_hand)):
        if (h_hand[i] == Max):
            count_max +=1
            tie_list.append(i)
    # Finds winner if max h values are tied
    if (len(tie_list) > 1):
        for i in range (1,count_max+1):
            max_val = max(points_hand)
            win1= points_hand.index(max_val)
            print("Player",win1+1,"ties.")
            points_hand[win1]=0 # Ensures duplicate winner doesn't exist
    else:
        print("Player",h_hand.index(Max)+1,"wins.")

  # determine if a hand is a royal flush
  def is_royal (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return False

    rank_order = True
    for i in range (len(hand)):
      rank_order = rank_order and (hand[i].rank == 14 - i)

    return (same_suit and rank_order)


  def is_straight_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

    if (not same_suit):
      return False

    rank_order = True
    for i in range (len(hand)-1):
      rank_order = rank_order and (hand[i].rank == (hand[i+1].rank)+1)

    return (same_suit and rank_order)


  def is_four_kind (self, hand):
    same_rank = True
    for i in range (len(hand)-2):
      same_rank = same_rank and (hand[i].rank == hand[i+1].rank)
    if same_rank:
      return same_rank
    else:
      same_rank= True
      for j in range (1, len(hand)-1):
        same_rank = same_rank and (hand[j].rank == hand[j+1].rank)
      return same_rank

  def is_full_house (self, hand):
    full_house1 = True
    full_house2 = True
    for i in range (len(hand)-1):
        if (hand[i].rank != hand[i+1].rank and i!=1):
            full_house1 = False
        if (hand[i].rank != hand[i+1].rank and i!=2):
            full_house2 = False
    return full_house1 or full_house2

  def is_flush (self, hand):
    same_suit = True
    for i in range (len(hand) - 1):
      same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)
    return same_suit

  def is_straight (self, hand):
    rank_order = True
    for i in range (len(hand)-1):
      rank_order = rank_order and (hand[i].rank == (hand[i+1].rank)+1)
    return rank_order

  def is_three_kind (self, hand):
    same_rank = True
    for j in range(0, len(hand)-2):
      same_rank= True
      for i in range (j, j+2):
        same_rank = same_rank and (hand[i].rank == hand[i+1].rank)
      if same_rank:
        return same_rank
    return same_rank

  def is_two_pair (self, hand):
    for j in range(0, len(hand)-1):
      if (hand[j].rank == hand[j+1].rank):
        for i in range(j+2, len(hand)-1):
          if(hand[i].rank==hand[i+1].rank):
            return True
    return False

  # determine if a hand is one pair
  def is_one_pair (self, hand):
    for i in range (len(hand) - 1):
      if (hand[i].rank == hand[i + 1].rank):
        return True
    return False


  def is_high_card (self, hand):
    return True


def main():
  # prompt user to enter the number of players
  num_players = int (input ('Enter number of players: '))
  while ((num_players < 2) or (num_players > 6)):
    num_players = int (input ('Enter number of players: '))

  # create the Poker object
  game = Poker (num_players)

  # play the game (poker)
  game.play()


main()
