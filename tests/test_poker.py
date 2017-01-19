# -*- coding: utf-8 -*-
"""
Tests for the poker package
"""

from .fixture import hands
from .poker import *


def test_poker(hands):
    print('invoke test_poker')
    assert poker(hands.sf1, hands.sf2, hands.fk,
                 hands.fh) == [hands.sf1, hands.sf2]
    assert poker(hands.fk, hands.fh) == [hands.fk]
    assert poker(hands.fh, hands.fl) == [hands.fh]
    assert poker(hands.fl, hands.st) == [hands.fl]
    assert poker(hands.st, hands.three) == [hands.st]


def test_hand_rank(hands):
    print('invoke test_hand_rank')
    assert hand_rank(hands.sf1) == (8, 10)


def test_card_ranks():
    pass


def test_flush():
    pass


def test_straight():
    pass


def test_kind():
    pass


def test_two_pair():
    pass
