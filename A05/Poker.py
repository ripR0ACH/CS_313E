#  File: Poker.py
#  Description: 
#  Student's Name: zachary morrison
#  Student's UT EID: zim225
#  Course Name: CS 313E
#  Unique Number: 52590
#  Date Created:
#  Date Last Modified:

import sys, random

class Card(object):
    RANKS = (2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14)

    SUITS = ('C', 'D', 'H', 'S')

    # constructor
    def __init__(self, rank = 12, suit = 'S'):
        if rank in Card.RANKS:
            self.rank = rank
        else:
            self.rank = 12
        
        if suit in Card.SUITS:
            self.suit = suit
        else:
            self.suit = 'S'
    
    # string representation of a Card object
    def __str__(self):
        if self.rank == 14:
            rank = 'A'
        elif self.rank == 13:
            rank = 'K'
        elif self.rank == 12:
            rank = 'Q'
        elif self.rank == 11:
            rank = 'J'
        else:
            rank = str(self.rank)
        return rank + self.suit
    
    # equality tests
    def __eq__(self, other):
        return self.rank == other.rank
    def __ne__(self, other):
        return self.rank != other.rank
    def __lt__(self, other):
        return self.rank < other.rank
    def __le__(self, other):
        return self.rank <= other.rank
    def __gt__(self, other):
        return self.rank > other.rank
    def __ge__(self, other):
        return self.rank >= other.rank

class Deck(object):
    # constructor
    def __init__(self, num_decks = 1):
        self.deck = []
        for i in range(num_decks):
            for suit in Card.SUITS:
                for rank in Card.RANKS:
                    card = Card(rank, suit)
                    self.deck.append(card)
    
    # shuffle the deck
    def shuffle(self):
        random.shuffle(self.deck)
    
    # deal a card
    def deal(self):
        if len(self.deck) == 0:
            return None
        else:
            return self.deck.pop(0)

class Poker(object):
    # constructor
    def __init__(self, num_players=2, num_cards=5):
        self.deck = Deck()
        self.deck.shuffle()
        self.all_hands = []
        self.numCards_in_Hand = num_cards

        # deal the cards to the players
        for i in range(num_players):
            hand = []
            for j in range(self.numCards_in_Hand):
                hand.append(self.deck.deal())
            self.all_hands.append(hand)

    # simulate the play of poker

    # determine if a hand is a royal flush
    # takes as argument a list of 5 Card objects
    # returns a number (points) for that hand
    def is_royal(self, hand):
        same_suit = True
        for i in range(len(hand) - 1):
            same_suit = same_suit and (hand[i].suit == hand[i + 1].suit)

        if (not same_suit):
            return 0, ''

        rank_order = True
        for i in range(len(hand)):
            rank_order = rank_order and (hand[i].rank == 14 - i)

        if (not rank_order):
            return 0, ''

        points = 10 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Royal Flush'

    def is_straight_flush(self, hand):
        is_straight_flush = True
        suit = hand[0].suit
        rank_order = hand[0].rank
        for i in hand:
            if i.suit != suit or i.rank != rank_order - 1:
                is_straight_flush = False
                break
            rank_order -= 1
        if not is_straight_flush:
            return 0, ''
        
        points = 9 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Straight Flush'

    def is_four_kind(self, hand):
        is_four_kind = False
        ranks = [i.rank for i in hand]
        four = None
        one = None
        for i in ranks:
            if ranks.count(i) == 4:
                four = i
                is_four_kind = True
                break
        if not is_four_kind:
            return 0, ''
        for i in ranks:
            if i != four:
                one = i
        
        points = 8 * 15 ** 5 + (four.rank) * 15 ** 4 + (four.rank) * 15 ** 3
        points = points + (four.rank) * 15 ** 2 + (four.rank) * 15 ** 1
        points = points + (one.rank)

        return points, 'Four of a Kind'

    def is_full_house(self, hand):
        is_full_house = False
        ranks = [i.rank for i in hand]
        if ranks.count(ranks[0]) != 3 and ranks.count(ranks[1]) != 3 and ranks.count(ranks[2]) != 3:
            return 0, ''
        triple, pair = None
        for i in ranks:
            if ranks.count(i) == 2:
                pair = i
                is_full_house = True
            if ranks.count(i) == 3:
                triple = i
        
        if is_full_house == False:
            return 0, ''
        
        points = 7 * 15 ** 5 + (triple) * 15 ** 4 + (triple) * 15 ** 3
        points = points + (triple) * 15 ** 2 + (pair) * 15 ** 1
        points = points + (pair)

        return points, 'Full House'

    def is_flush(self, hand):
        suit = hand[0].suit
        for i in hand:
            if i.suit != suit:
                return 0, ''
        
        points = 6 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Flush'

    def is_straight(self, hand):
        straight = True
        start = hand[0].rank
        for i in hand[1:]:
            if i.rank != start - 1:
                straight = False
                break
            start -= 1

        if not straight:
            return 0, ''
        
        points = 5 * 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'Straight'

    def is_three_kind(self, hand):
        ranks = [i.rank for i in hand]
        if ranks.count(ranks[0]) != 3 and ranks.count(ranks[1]) != 3 and ranks.count(ranks[2]) != 3:
            return 0, ''
        triple = None
        for i in ranks:
            if ranks.count(i) == 3:
                triple = i
                break
        while ranks.count(triple) > 0:
            del ranks[ranks.index(triple)]
        ranks = sorted(ranks, reverse=True)

        points = 4 * 15 ** 5 + (triple) * 15 ** 4 + (triple) * 15 ** 3
        points = points + (triple) * 15 ** 2 + (ranks[0]) * 15 ** 1
        points = points + (ranks[1])

        return points, 'Three of a Kind'

    def is_two_pair(self, hand):
        ranks = [i.rank for i in hand]
        pair1 = None
        pair2 = None
        for i in ranks:
            if ranks.count(i) == 2:
                pair1 = i
        if pair1 == None:
            return 0, ''
        while ranks.count(pair1) > 0:
            del ranks[ranks.index(pair1)]
        for i in ranks:
            if ranks.count(i) == 2:
                pair2 = i
        if pair2 == None:
            return 0, ''
        if pair1 < pair2:
            temp = pair2
            pair2 = pair1
            pair1 = temp
        ranks = sorted(ranks, reverse=True)

        points = 3 * 15 ** 5 + (pair1) * 15 ** 4 + (pair1) * 15 ** 3
        points = points + (pair2) * 15 ** 2 + (pair2) * 15 ** 1
        points = points + (ranks[0])

        return points, 'Two Pair'

    # determine if a hand is one pair
    # takes as argument a list of 5 Card objects
    # returns the number of points for that hand
    def is_one_pair(self, hand):
        ranks = [i.rank for i in hand]
        pair = None
        for i in range(len(hand) - 1):
            if (hand[i].rank == hand[i + 1].rank):
                pair = hand[i].rank
                break
        if pair == None:
            return 0, ''
        
        while ranks.count(pair) > 0:
            del ranks[ranks.index(pair)]
        ranks = sorted(ranks, reverse=True)

        points = 2 * 15 ** 5 + (pair) * 15 ** 4 + (pair) * 15 ** 3
        points = points + (ranks[0]) * 15 ** 2 + (ranks[1]) * 15 ** 1
        points = points + (ranks[2])

        return points, 'One Pair'

    def is_high_card(self, hand):
        points = 15 ** 5 + (hand[0].rank) * 15 ** 4 + (hand[1].rank) * 15 ** 3
        points = points + (hand[2].rank) * 15 ** 2 + (hand[3].rank) * 15 ** 1
        points = points + (hand[4].rank)

        return points, 'High Card'
    
    def play(self):
        players = []
        # sort the hands of each player and print
        for i in range(len(self.all_hands)):
            sorted_hand = sorted(self.all_hands[i], reverse = True)
            players.append(sorted_hand)
            self.all_hands[i] = sorted_hand
            hand_str = ''
            for card in sorted_hand:
                hand_str = hand_str + str(card) + ' '
            print('Player ' + str(i + 1) + ' : ' + hand_str)
        print()
        # determine the type of each hand and print
        hand_type = []  # create a list to store type of hand
        hand_points = []  # create a list to store points for hand

        for player in range(len(players)):
            points, type = self.is_royal(players[player])
            if points != 0 and type != '':
                hand_type.append(type)
                hand_points.append(points)
                continue
            points, type = self.is_straight_flush(players[player])
            if points != 0 and type != '':
                hand_type.append(type)
                hand_points.append(points)
                continue
            points, type = self.is_four_kind(players[player])
            if points != 0 and type != '':
                hand_type.append(type)
                hand_points.append(points)
                continue
            points, type = self.is_full_house(players[player])
            if points != 0 and type != '':
                hand_type.append(type)
                hand_points.append(points)
                continue
            points, type = self.is_flush(players[player])
            if points != 0 and type != '':
                hand_type.append(type)
                hand_points.append(points)
                continue
            points, type = self.is_straight(players[player])
            if points != 0 and type != '':
                hand_type.append(type)
                hand_points.append(points)
                continue
            points, type = self.is_three_kind(players[player])
            if points != 0 and type != '':
                hand_type.append(type)
                hand_points.append(points)
                continue
            points, type = self.is_two_pair(players[player])
            if points != 0 and type != '':
                hand_type.append(type)
                hand_points.append(points)
                continue
            points, type = self.is_one_pair(players[player])
            if points != 0 and type != '':
                hand_type.append(type)
                hand_points.append(points)
                continue
            points, type = self.is_high_card(players[player])
            hand_type.append(type)
            hand_points.append(points)
        
        # determine winner and print
        max = hand_points[0]
        for player in range(len(players)):
            print("Player " + str(player + 1) + " : " + hand_type[player])
            if max < hand_points[player]:
                max = hand_points[player]
        print()
        print("Player " + str(hand_points.index(max) + 1) + " wins")

            
def main():
    # read number of players from stdin
    line = sys.stdin.readline()
    line = line.strip()
    num_players = int(line)
    if (num_players < 2) or (num_players > 6):
        return

    # create the Poker object
    game = Poker(num_players)

    # play the game
    game.play()

if __name__ == "__main__":
    main()
