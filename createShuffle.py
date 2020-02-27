#!/usr/bin/env python3.8

from random import randint

def create_pack():
    deck = []
    for i in range (1,5):
        for j in range(1,14):
            if j == 1:
                card_num = str('A')
            elif j == 11:
                card_num = str('J')
            elif j == 12:
                card_num = str('Q')
            elif j == 13:
                card_num = str('K')
            else:
                card_num = str(j)
            if i == 1:
                card_suit = str(' H')
            elif i == 2:
                card_suit = str(' D')
            elif i == 3:
                card_suit = str(' S')
            elif i == 4:
                card_suit = str(' C')
            card = str(card_num + card_suit)
            deck.append(card)
    return deck

def shuffle_cards(deck):
    shuffled_deck = []
    for i in range(0,len(deck)):
        card = randint(0,len(deck)-1)
        shuffled_deck.append(deck[card])
        deck.pop(card)
    deck = shuffled_deck
    return deck