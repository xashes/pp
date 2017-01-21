"""
Hand object
"""


class Hand:
    """
    Poker hand object
    """

    def __init__(self, cards):
        "init a poker hand with a list of cards"
        self.cards = cards

    @property
    def rank(self):
        """
        Return a tuple indicating the ranking of the hand.
        """
        counts, ranks = zip(*self._groups)

        return (8 if self._is_flush and self._is_straight else
                7 if (4, 1) == counts else
                6 if (3, 2) == counts else
                5 if self._is_flush else
                4 if self._is_straight else
                3 if (3, 1, 1) == counts else
                2 if (2, 2, 1) == counts else
                1 if (2, 1, 1, 1) == counts else
                0), ranks

    @property
    def _card_ranks(self):
        """
        Return a list of the ranks, sorted with higher first.
        """
        ranks = ['__23456789TJQKA'.index(r) for r, s in self.cards]
        ranks.sort(reverse=True)
        if ranks == [14, 5, 4, 3, 2]:
            return [5, 4, 3, 2, 1]
        return ranks

    @property
    def _is_flush(self):
        """
        Return True is the hand is flush
        """
        suits = [s for r, s in self.cards]
        return len(set(suits)) == 1

    @property
    def _is_straight(self):
        """
        Return True if the hand is straight
        """
        return len(set(self._card_ranks)) == 5 and (
            max(self._card_ranks) - min(self._card_ranks) == 4)

    @property
    def _groups(self):
        """
        Return [(counts, rank),...] based on card ranks,
        sorted with higher first.
        Example: [9, 9, 9, 6, 3] => [(3, 9), (1, 6), (1, 3)]
        """
        groups = [(self._card_ranks.count(x), x) for x in set(self._card_ranks)]
        groups.sort(reverse=True)
        return groups
