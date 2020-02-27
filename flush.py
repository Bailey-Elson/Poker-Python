#!/usr/bin/env python3.8

def check_flush(hand):
    hearts = 0
    clubs = 0 
    diamonds = 0
    spades = 0
    for i in range(0,len(hand)):
        card = (list(hand[i]))
        suit = card[len(card)-1]
        if suit == 'H':
            hearts = hearts + 1
        elif suit == 'C':
            clubs = clubs + 1
        elif suit == 'D':
            diamonds = diamonds + 1
        else:
            spades = spades + 1
    if hearts >= 5 or clubs >= 5 or diamonds >= 5 or spades >= 5:
        flush = True
    else:
        flush = False
    return flush
