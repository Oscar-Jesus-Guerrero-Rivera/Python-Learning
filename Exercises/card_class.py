"""
Assignment
Complete the Card class.

Define a constructor that takes rank and suit as parameters and sets rank, 
suit, rank_index, and suit_index instance variables.
You will need the indexes of the ranks, and suits to help you compare 
them against each other. Keep in mind that a rank and a suit are just strings within a list.

Overload the comparison operators:
Overload the following comparison operators:

==: eq
>: gt
<: lt
Ranking the Cards
A card is "greater than" another card if it has a higher rank. 
However, if the ranks are the same, the card with the higher suit is 
"greater than" the other card. This same logic applies to the "less than" operator. 
The "equal to" operator should check that the rank AND suit are equal.

The suits and ranks are defined as global variables. The lower the index, 
the lower the rank or suit.
"""

SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]


class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.rank_index = RANKS.index(rank)
        self.rank_suit = SUITS.index(suit)

    def __eq__(self, other):
        return (self.rank_index, self.rank_suit) == (other.rank_index, other.rank_suit)

    def __lt__(self, other):
        return (self.rank_index, self.rank_suit) < (other.rank_index, other.rank_suit)


    def __gt__(self, other):
        return (self.rank_index, self.rank_suit) > (other.rank_index, other.rank_suit)


    # don't touch below this line

    def __str__(self):
        return f"{self.rank} of {self.suit}"
    

    # test Cases


SUITS = ["Clubs", "Diamonds", "Hearts", "Spades"]

RANKS = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

run_cases = [
    ("Ace", "Hearts", "Queen", "Hearts", False, True),
    ("2", "Spades", "2", "Hearts", False, True),
]

submit_cases = run_cases + [
    ("Ace", "Spades", "Ace", "Spades", True, False),
    ("3", "Diamonds", "7", "Clubs", False, False),
    ("King", "Clubs", "King", "Hearts", False, False),
    ("Queen", "Diamonds", "Jack", "Spades", False, True),
    ("10", "Hearts", "10", "Hearts", True, False),
]


def test(rank_1, suit_1, rank_2, suit_2, expected_eq, expected_gt):
    print("---------------------------------")
    print(f"Inputs: {rank_1} of {suit_1}, {rank_2} of {suit_2}")
    print("Expected:")
    print(f" * Equal: {expected_eq}")
    print(f" * Greater than: {expected_gt}")
    print(f" * Less than: {not (expected_eq or expected_gt)}")

    card_1 = Card(rank_1, suit_1)
    card_2 = Card(rank_2, suit_2)
    result_eq = card_1 == card_2
    result_gt = card_1 > card_2
    result_lt = card_1 < card_2
    print("Actual:")
    print(f" * Equal: {result_eq}")
    if result_eq != expected_eq:
        print("Fail")
        return False
    print(f" * Greater than: {result_gt}")
    if result_gt != expected_gt:
        print("Fail")
        return False
    print(f" * Less than: {result_lt}")
    if result_lt == (expected_eq or expected_gt or None):
        print("Fail")
        return False
    print("Pass")
    return True


def main():
    passed = 0
    failed = 0
    for test_case in test_cases:
        correct = test(*test_case)
        if correct:
            passed += 1
        else:
            failed += 1
    if failed == 0:
        print("============= PASS ==============")
    else:
        print("============= FAIL ==============")
    print(f"{passed} passed, {failed} failed")


test_cases = submit_cases
if "__RUN__" in globals():
    test_cases = run_cases

main()
