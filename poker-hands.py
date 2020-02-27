#!/usr/bin/env python3.8

from random import randint
from createShuffle import create_pack, shuffle_cards

from royalFlush import check_royal_flush
from straightFlush import check_straight_flush
from fourOfAKind import check_four_of_a_kind
from fullHouse import check_full_house
from flush import check_flush
from straight import check_straight
from threeOfAKind import check_three_of_a_kind
from twoPair import check_two_pair
from pair import check_pair

def deal_hands(deck):
    hand = []
    for i in range(0,7):
        hand.append(deck[0])
        deck.pop(0)
    print("Your cards are\n")
    for i in range (0,7):
        print(hand[i])
    return hand, deck

royal_flush = False
straight_flush = False
foak = False
full_house = False
flush = False
straight = False
toak = False
two_pair = False
pair = False

deck = create_pack()
deck = shuffle_cards(deck)
hand, deck = deal_hands(deck)

royal_flush = check_royal_flush(hand)
if royal_flush == False:
    straight_flush = check_straight_flush(hand)
    if straight_flush == False:
        foak = check_four_of_a_kind(hand)
        if foak == False:
            full_house = check_full_house(hand)
            if full_house == False:
                flush = check_flush(hand)
                if flush == False:
                    straight = check_straight(hand)
                    if straight == False:
                        toak = check_three_of_a_kind(hand)
                        if toak == False:
                            two_pair = check_two_pair(hand)
                            if two_pair == False:
                                pair = check_pair(hand)
                                if pair == False:
                                    print("You have a high card")
                                else:
                                    print("You have a pair")                       
                            else:
                                print("You have two pair")
                        else:
                            print("You have three of a kind")
                    else:
                        print("You have a straight")
                else:
                    print("You have a flush")
            else:
                print("You have a full house")    
        else:
            print("You have four of a kind")
    else:
        print("You have straight flush")
else:
    print("You have a royal flush")
