#!/usr/bin/env python3.8
from flush import check_flush

def check_royal_flush(hand):
    flush = check_flush(hand)
    royal = []
    suit = []
    royal_flush = False
    royal_flush_count = 0
    if flush == True:
        for i in range(0,len(hand)):
            card = (list(hand[i]))
            suit.append(card[len(card)-1])
        flush_suit = max(set(suit), key = suit.count)
        for i in range(0,len(hand)):
            card = (list(hand[i]))
            if card[len(card)-1] == flush_suit:
                royal.append(card[0])

        for i in range(0,len(royal)):
            if royal[i] == 'K':
                royal_flush_count = royal_flush_count + 1   
        for i in range(0,len(royal)):
            if royal[i] == 'Q':
                royal_flush_count = royal_flush_count + 1
        for i in range(0,len(royal)):
            if royal[i] == 'J':
                royal_flush_count = royal_flush_count + 1
        for i in range(0,len(royal)):
            if royal[i] == '1':
                royal_flush_count = royal_flush_count + 1  
        for i in range(0,len(royal)):
            if royal[i] == 'A':
                royal_flush_count = royal_flush_count + 1

    if royal_flush_count == 5:
        royal_flush = True
  
    return royal_flush