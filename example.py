from enum import Enum


class Card:
    hearts = 1
    diamonds = 2
    clubs = 3
    spades = 4
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14

    def __init__(self, suit, number):
        self.suit = suit
        self.number = number

    def __eq__(self, other):
        return self.number - other.number


suits = ["hearts", "diamonds", "clubs", "spades"]
rank = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

card1 = Card(suits[2], rank[11])
card2 = Card(suits[0], rank[3])
card3 = Card(suits[3], rank[6])
card4 = Card(suits[1], rank[10])
card5 = Card(suits[1], rank[11])
card6 = Card(suits[2], rank[3])
card7 = Card(suits[3], rank[12])
card8 = Card(suits[2], rank[9])

result = card1 == card2
if result == 0:
    print(card1.number, card1.suit, "=", card2.number, card2.suit)
if result > 0:
    print(card1.number, card1.suit, ">", card2.number, card2.suit)
if result < 0:
    print(card1.number, card1.suit, "<", card2.number, card2.suit)
