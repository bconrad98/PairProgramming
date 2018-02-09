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

  '''
  def __str__(self):
  	string_1=""
  	list1=[]
  	for i in range(len(self.players)):
  		list1=self.players.split()
  		string_1+= self.players[i].rank
  	return list1
'''
  def play (self):
    # sort the hands of each player and print
    for i in range (len(self.players)):
      sortedHand = sorted (self.players[i], reverse = True)
      self.players[i] = sortedHand
      hand = ''
      for card in sortedHand:
        hand = hand + str (card) + ' '
      print ('Player ' + str (i + 1) + " : " + hand)
    # Test Case
    c1=Card(9,"C")
    c2=Card(9,"H")
    c3=Card(6,"H")
    c4=Card(6,"C")
    c5=Card(4,"H")
    self.players[5]=[ c1,c2,c3,c4,c5 ]
    hand=''
    for card in self.players[5]:
        hand = hand + str (card) + ' '
    print ('Player ' + str (6) + " : " + hand)

    # determine the each type of hand and print
    print()
    points_hand = []  # create list to store points for each hand
    h=0
    str_result=''
    for j in range(0, len(self.players)):
      if (self.is_royal(self.players[j])):
        h=10
        str_result=("Player "+ str(j+1) + ': ' + 'Royal Flush')
      elif(self.is_straight_flush(self.players[j])):
        h=9
        str_result=("Player "+ str(j+1) + ': ' + 'Straight Flush')
      elif(self.is_four_kind(self.players[j])):
        h=8
        str_result=("Player "+ str(j+1) + ': ' + 'Four of a Kind')
      elif(self.is_full_house(self.players[j])):
        h=7
        str_result=("Player "+ str(j+1) + ': ' + 'Full House')
      elif(self.is_flush(self.players[j])):
        h=6
        str_result=("Player "+ str(j+1) + ': ' + 'Flush')
      elif(self.is_straight(self.players[j])):
        h=5
        str_result=("Player "+ str(j+1) + ': ' + 'Straight')
      elif(self.is_three_kind(self.players[j])):
        h=4
        str_result=("Player "+ str(j+1) + ': ' + 'Three of a Kind')
      elif(self.is_two_pair(self.players[j])):
        h=3
        str_result=("Player "+ str(j+1) + ': ' + 'Two Pair')
      elif(self.is_one_pair(self.players[j])):
        h=2
        str_result=("Player "+ str(j+1) + ': ' + 'One Pair')
      elif(self.is_high_card(self.players[j])):
        h=1
        str_result=("Player "+ str(j+1) + ': ' + 'High Card')
      print (str_result)



    # determine winner and print


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
      for i in range (j, j+3):
        same_rank = same_rank and (hand[i].rank == hand[i+1].rank)
      if same_rank:
        return same_rank
    return same_rank

  def is_two_pair (self, hand):
    for j in range(0, len(hand)-1):
      if (hand[j].rank == hand[j+1].rank):
        for i in range(j+1, len(hand)-1):
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
