def card_ranks(hand):
    """
    Return a list of the ranks, sorted with higher first.
    """
    ranks = ['__23456789TJQKA'.index(r) for r, s in hand]
    ranks.sort(reverse=True)
    if ranks == [14, 5, 4, 3, 2]:
        return [5, 4, 3, 2, 1]
    return ranks

def suits(hand):
    return [s for r, s in hand]

def is_flush(hand):
    return len(set(suits(hand))) == 1

def is_straight(hand):
    return (card_ranks(hand)[0] - card_ranks(hand)[-1]) == 4 and (len(set(card_ranks(hand))) == 5)

def groups(hand):
    """
    Return [(counts, rank),...] based on card ranks,
    sorted with higher first.
    Example: [9, 9, 9, 6, 3] => [(3, 9), (1, 6), (1, 3)]
    """
    groups = [(card_ranks(hand).count(r), r) for r in set(card_ranks(hand))]
    groups.sort(reverse=True)
    return groups

def hand_rank(hand):
    pass




