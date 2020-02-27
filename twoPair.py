#!/usr/bin/env python3.8
def check_two_pair(hand):
    num_card = []
    for i in range(0,len(hand)):
        card = (list(hand[i]))
        num_card.append(card[0])
    common_card = max(set(num_card), key = num_card.count)
    amount = 0
    num2_card = []
    for i in range(0,len(num_card)):
        if common_card == num_card[i]:
            amount = amount + 1
        else:
            num2_card.append(num_card[i])

    if amount == 2:
        num_card = num2_card
        common_card = max(set(num_card), key = num_card.count)
        amount = 0
        for i in range(0,len(num_card)):
            if common_card == num_card[i]:
                amount = amount + 1
        if amount == 2:
            two_pair = True
        else:
            two_pair = False
    else: 
        two_pair = False
    return two_pair