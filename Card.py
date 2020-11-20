from random import randint


class Card:
    def __init__(self, suit, range):
        self.suit = suit
        self.range = range

    def comparison(self, r):
        for i in range(len(rank)):
            if rank[i] == self.range and rank[i] == r:
                return 0
            if rank[i] == self.range:
                return -1
            if rank[i] == r:
                return 1


class CardDesk:
    def __init__(self, arr):
        self.arr = arr

    def RandomCard(self, m):
        amount = set()
        if m > len(self.arr):
            return
        while len(amount) != m:
            j = randint(0, len(self.arr) - 1)
            amount.add(self.arr[j])
        for item in amount:
            print(item.range, item.suit)

    def MaxCard(self):
        x = 0
        max = 0
        for j in range(4):
            for i in range(len(self.arr)):
                if self.arr[i].suit == suits[j] and x == 0:
                    max = i
                    x = 1
                if self.arr[i].suit == suits[j] and x == 1:
                    res = self.arr[max].comparison(self.arr[i].range)
                    if res == -1:
                        max = i
            if x == 0:
                print("No suit")
            else:
                print(self.arr[max].range, self.arr[max].suit)
            x = 0
            max = 0

    def MinCard(self):
        x = 0
        min = 0
        for j in range(4):
            for i in range(len(self.arr)):
                if self.arr[i].suit == suits[j] and x == 0:
                    min = i
                    x = 1
                if self.arr[i].suit == suits[j] and x == 1:
                    res = self.arr[min].comparison(self.arr[i].range)
                    if res == 1:
                        min = i
            if x == 0:
                print("No suit")
            else:
                print(self.arr[min].range, self.arr[min].suit)
            x = 0
            min = 0




suits = ["hearts", "diamonds", "clubs", "spades"]
rank = [2, 3, 4, 5, 6, 7, 8, 9, 10, "Jack", "Queen", "King", "Ace"]

card1 = Card(suits[2], rank[5])
card2 = Card(suits[1], rank[1])
card3 = Card(suits[3], rank[6])
card4 = Card(suits[1], rank[10])
card5 = Card(suits[1], rank[11])
card6 = Card(suits[2], rank[3])
card7 = Card(suits[3], rank[12])
card8 = Card(suits[2], rank[9])
result = card1.comparison(card2.range)
if result == 0:
    print("cards equal")
if result == -1:
    print("card 1 < card 2")
if result == 1:
    print("card 1 > card 2")


array = []
array.append(card1)
array.append(card2)
array.append(card3)
array.append(card4)
array.append(card5)
array.append(card6)
array.append(card7)
array.append(card8)
for i in range(len(array)):
    print(array[i].range, array[i].suit)
n = 2
print("_________________","\n", "Random cards")
CardResult = CardDesk(array)
CardResult.RandomCard(n)
print("_________________", "\n", "Maxcard")
CardResult.MaxCard()
print("_________________", "\n", "Mincard")
CardResult.MinCard()