#!/usr/bin/env python3.8
from flush import check_flush
from straight import check_straight

def check_straight_flush(hand):
    flush = check_flush(hand)
    sf = [] 
    suit = []
    if flush == True:
        for i in range(0,len(hand)):
            card = (list(hand[i]))
            suit.append(card[len(card)-1])
        flush_suit = max(set(suit), key = suit.count)
        for i in range(0,len(hand)):
            card = (list(hand[i]))
            if card[len(card)-1] == flush_suit:
                sf.append(card[0]) 
    straight = check_straight(sf) 
    if straight == True and flush == True:
        straight_flush = True
    else:
        straight_flush = False
    return straight_flush     