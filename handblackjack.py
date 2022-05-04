def hand_total(hand):
    # Tong gia tri la bai
    total = 0
    # So quan bai at
    aces = 0
    for card in hand:
        if card in ['J', 'Q', 'K']:
            total += 10
        # Tinh so quan bai at
        elif card == 'A':
            aces += 1
        # Convert 1->10
        else:
            total += int(card)
    # At this point, total is the sum of this hand's cards *not counting aces*.

    # Add aces, counting them as 1 for now. This is the smallest total we can make from this hand
    total += aces
    while total + 10 <= 21 and aces > 0:
        total += 10
        aces -= 1
    return total


def blackjack_hand_greater_than(hand_1, hand_2):
    total_1 = hand_total(hand_1)
    total_2 = hand_total(hand_2)
    return total_1 <= 21 and (total_1 > total_2 or total_2 > 21)


print(blackjack_hand_greater_than(['K'], ['3', '4']))
