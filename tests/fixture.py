import pytest


class Hands:
    def __init__(self):
        self.sf1 = "6C 7C 8C 9C TC".split()  # Straight Flush
        self.sf2 = "6D 7D 8D 9D TD".split()  # Straight Flush
        self.fk = "9D 9H 9S 9C 7D".split()  # Four of a Kind
        self.fh = "TD TC TH 7C 7D".split()  # Full House
        self.fl = "JD 9D 8D 3D 2D".split()  # Flush
        self.st = "9H 8H 7H 6H 5D".split()  # Straight
        self.three = "9H 9C 9D 6D 5D".split()  # Three of a Kind
        self.tp = "TD TC 8H 8D 6H".split()  # Two Pair
        self.op = "JS JD 6H 5C 2D".split()  # One Pair
        self.ah = "AH KC TD 6D 2D".split()  # A High
        self.th = "TH 9C 7D 6C 2D".split()  # T High


@pytest.fixture(scope='module')
def hands():
    "Test cases for the functions in poker program."
    print("invoke hands()")
    return Hands()
