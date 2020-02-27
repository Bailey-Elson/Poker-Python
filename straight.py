#!/usr/bin/env python3.8

def check_straight(hand):
    is_straight = 0
    hand_ace_high = []
    hand_ace_low = []
    for i in range(0,len(hand)):
        card = (list(hand[i]))
        if card[0] == 'K':
            hand_ace_high.append('13')
            hand_ace_low.append('13')
        elif card[0] == '1':
            hand_ace_high.append('10')
            hand_ace_low.append('10')
        elif card[0] == 'Q':
            hand_ace_high.append('12')
            hand_ace_low.append('12')
        elif card[0] == 'J':
            hand_ace_high.append('11')
            hand_ace_low.append('11')
        elif card[0] == 'A':
            hand_ace_high.append('14')
            hand_ace_low.append('1')
        else:
            hand_ace_high.append(card[0])
            hand_ace_low.append(card[0])
    for i in range(0, len(hand_ace_high)): 
        hand_ace_high[i] = int(hand_ace_high[i])
        hand_ace_low[i] = int(hand_ace_low[i])
    hand_ace_high.sort()
    hand_ace_low.sort()
    hand_ace_high = list(dict.fromkeys(hand_ace_high))
    hand_ace_low = list(dict.fromkeys(hand_ace_low))
    hand_ace_high = list(dict.fromkeys(hand_ace_high))
    hand_ace_low = list(dict.fromkeys(hand_ace_low))
    if len(hand_ace_high)<5:
        straight = False
    else:
        if len(hand_ace_high) == 5:
            loop = 1
        if len(hand_ace_high) == 6:
            loop = 2
        if len(hand_ace_high) == 7:
            loop = 3
        for i in range (0,loop):
            is_straight = check_straight_2(hand_ace_high, is_straight)
            is_straight = check_straight_2(hand_ace_low, is_straight)
            hand_ace_high.pop()
            hand_ace_low.pop()
    if is_straight != 0:
        straight = True
    else:
        straight = False
    return straight

def check_straight_2(hand, is_straight):
    second = int(hand[0]-hand[1]+1)
    third = int(hand[1]-hand[2]+1)
    fourth = int(hand[2]-hand[3]+1)
    fifth = int(hand[3]-hand[4]+1)
    if second == 0 and third == 0 and fourth == 0 and fifth == 0:
        is_straight = is_straight + 1
    return is_straight
