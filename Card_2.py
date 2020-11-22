from random import randint
from enum import Enum


class Card:

    def __init__(self, suit, number, name):
        self.suit = suit
        self.number = number
        self.name = name

    def compare(self, other):
        return self.number - other.number


class Suit(Enum):
    hearts = "hearts"
    diamonds = "diamonds"
    clubs = "clubs"
    spades = "spades"


class Rank(Enum):
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
    Ace = 14


class CardDesk:
    def __init__(self, arr):
        self.arr = arr

    def random_card(self, m):
        amount = set()
        if m > len(self.arr):
            return
        while len(amount) != m:
            j = randint(0, len(self.arr) - 1)
            amount.add(self.arr[j])
        for item in amount:
            print(item.name, item.suit)

    def max_card(self):
        x = 0
        top = 0
        for j in range(4):
            for k in range(len(self.arr)):
                if self.arr[k].suit == suits[j] and x == 0:
                    top = k
                    x = 1
                if self.arr[k].suit == suits[j] and x == 1:
                    res = self.arr[top].compare(self.arr[k])
                    if res < 0:
                        top = k
            if x == 0:
                print("No suit")
            else:
                print(self.arr[top].name, self.arr[top].suit)
            x = 0
            top = 0

    def min_card(self):
        x = 0
        bottom = 0
        for j in range(4):
            for k in range(len(self.arr)):
                if self.arr[k].suit == suits[j] and x == 0:
                    bottom = k
                    x = 1
                if self.arr[k].suit == suits[j] and x == 1:
                    res = self.arr[bottom].compare(self.arr[k])
                    if res > 0:
                        bottom = k
            if x == 0:
                print("No suit")
            else:
                print(self.arr[bottom].name, self.arr[bottom].suit)
            x = 0
            bottom = 0


card1 = Card(Suit.hearts.value, Rank.Two.value, Rank.Two.name)
card2 = Card(Suit.diamonds.value, Rank.King.value, Rank.King.name)
card3 = Card(Suit.clubs.value, Rank.Ace.value, Rank.Ace.name)
card4 = Card(Suit.spades.value, Rank.Seven.value, Rank.Seven.name)
card5 = Card(Suit.clubs.value, Rank.Five.value, Rank.Five.name)
card6 = Card(Suit.diamonds.value, Rank.Jack.value, Rank.Jack.name)
card7 = Card(Suit.hearts.value, Rank.Three.value, Rank.Three.name)
card8 = Card(Suit.spades.value, Rank.Ten.value, Rank.Ten.name)
suits = ["hearts", "diamonds", "clubs", "spades"]
array = [card1, card2, card3, card4, card5, card6, card7, card8]
n = 2
print("Random cards", "\n", "_________________")
CardResult = CardDesk(array)
CardResult.random_card(n)
result = card3.compare(card2)
print("_________________", "\n", "List of cards")
for i in range(len(array)):
    print(array[i].name, array[i].suit)
if result == 0:
    print("cards equal")
if result < 0:
    print("the first card < the second card")
if result > 0:
    print("the first card > the second card")
print("_________________", "\n", "Maxcard")
CardResult.max_card()
print("_________________", "\n", "Mincard")
CardResult.min_card()
