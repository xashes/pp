# -*- coding: utf-8 -*-

from pp.hand import Hand
from pp.rank import *

from .const import *


def test_init():
    """
    test cases for __init__ method
    """
    assert Hand(SF1).cards == '6C 7C 8C 9C TC'.split()


def test_rank():
    """
    test cases for rank method
    """
    assert Hand(SF1).rank == (8, (10, 9, 8, 7, 6))
    assert Hand(SF2).rank == (8, (10, 9, 8, 7, 6))
    assert Hand(FK).rank == (7, (9, 7))
    assert Hand(FH).rank == (6, (10, 7))
    assert Hand(FL).rank == (5, (11, 9, 8, 3, 2))
    assert Hand(ST).rank == (4, (9, 8, 7, 6, 5))
    assert Hand(STA).rank == (4, (5, 4, 3, 2, 1))
    assert Hand(THREE).rank == (3, (9, 6, 5))
    assert Hand(TP).rank == (2, (10, 8, 6))
    assert Hand(OP).rank == (1, (11, 6, 5, 2))
    assert Hand(AH).rank == (0, (14, 13, 10, 6, 2))
    assert Hand(TH).rank == (0, (10, 9, 7, 6, 2))


def test_card_ranks():
    assert card_ranks(SF1) == [10, 9, 8, 7, 6]
    assert card_ranks(STA) == [5, 4, 3, 2, 1]


def test_is_straight():
    assert is_straight(SF1)
    assert is_straight(FK) is False
    assert is_straight(FH) is False
    assert is_straight(ST)
    assert is_straight(STA)
    assert is_straight(TP) is False


def test_is_flush():
    """
    test cases for _is_flush method
    """
    assert is_flush(SF1)
    assert is_flush(FK) is False
    assert is_flush(FL)


def test_groups():
    assert groups(FK) == [(4, 9), (1, 7)]
    assert groups(THREE) == [(3, 9), (1, 6), (1, 5)]
    assert groups(OP) == [(2, 11), (1, 6), (1, 5), (1, 2)]
