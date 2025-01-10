"""
Assignment
Finish the DeckOfCards class. The SUITS and RANKS of each card 
have been provided for you as class variables. You won't need to 
modify them, but you will need to use them.

Constructor
Initialize a private empty list called cards.
Fill that empty list by calling the create_deck method within the constructor.
create_deck(self)
This method should create a (Rank, Suit) tuple for all 52 cards in the 
deck and append them to the cards list.

Order matters! The cards should be appended to the list in the 
following order: all ranks of hearts, then diamonds, then clubs, 
and finally spades. Within each suit, the cards should be ordered 
from lowest rank (Ace) to highest rank (King).

shuffle_deck(self)
This method should use the random.shuffle() method (available from the random package) 
to shuffle the cards in the deck.

deal_card(self)
This method should .pop() the first card off the top of the deck 
(top of the deck is the end of the list) and return it. 
If there are no cards left in the deck the method should instead return None.
"""
# Solution

import random

class DeckOfCards:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "Ace",
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
    ]

    def __init__(self):
        self.__cards = list()
        self.create_deck()

    def create_deck(self):
        self.__cards = [
            (rank, suit) 
            for suit in self.SUITS 
            for rank in self.RANKS
        ]

    def shuffle_deck(self):
        random.shuffle(self.__cards)

    def deal_card(self):
        try:
            return self.__cards.pop()
        except:
            return None

    # don't touch below this line

    def __str__(self):
        return f"The deck has {len(self.__cards)} cards"

# Test Cases


run_cases = [
    ("shuffle_deck", 3, [("9", "Hearts"), ("Jack", "Clubs"), ("10", "Spades")]),
    (
        "deal_card",
        4,
        [("King", "Spades"), ("Queen", "Spades"), ("Jack", "Spades"), ("10", "Spades")],
    ),
    ("deal_card", 3, [("King", "Spades"), ("Queen", "Spades"), ("Jack", "Spades")]),
]

submit_cases = run_cases + [
    ("shuffle_deck", 3, [("9", "Hearts"), ("Jack", "Clubs"), ("10", "Spades")]),
    (
        "deal_card",
        4,
        [("King", "Spades"), ("Queen", "Spades"), ("Jack", "Spades"), ("10", "Spades")],
    ),
    ("deal_card", 3, [("King", "Spades"), ("Queen", "Spades"), ("Jack", "Spades")]),
    ("shuffle_deck", 3, [("9", "Hearts"), ("Jack", "Clubs"), ("10", "Spades")]),
    ("deal_card", 3, [("King", "Spades"), ("Queen", "Spades"), ("Jack", "Spades")]),
    (
        "deal_card",
        53,
        [
            ("King", "Spades"),
            ("Queen", "Spades"),
            ("Jack", "Spades"),
            ("10", "Spades"),
            ("9", "Spades"),
            ("8", "Spades"),
            ("7", "Spades"),
            ("6", "Spades"),
            ("5", "Spades"),
            ("4", "Spades"),
            ("3", "Spades"),
            ("2", "Spades"),
            ("Ace", "Spades"),
            ("King", "Clubs"),
            ("Queen", "Clubs"),
            ("Jack", "Clubs"),
            ("10", "Clubs"),
            ("9", "Clubs"),
            ("8", "Clubs"),
            ("7", "Clubs"),
            ("6", "Clubs"),
            ("5", "Clubs"),
            ("4", "Clubs"),
            ("3", "Clubs"),
            ("2", "Clubs"),
            ("Ace", "Clubs"),
            ("King", "Diamonds"),
            ("Queen", "Diamonds"),
            ("Jack", "Diamonds"),
            ("10", "Diamonds"),
            ("9", "Diamonds"),
            ("8", "Diamonds"),
            ("7", "Diamonds"),
            ("6", "Diamonds"),
            ("5", "Diamonds"),
            ("4", "Diamonds"),
            ("3", "Diamonds"),
            ("2", "Diamonds"),
            ("Ace", "Diamonds"),
            ("King", "Hearts"),
            ("Queen", "Hearts"),
            ("Jack", "Hearts"),
            ("10", "Hearts"),
            ("9", "Hearts"),
            ("8", "Hearts"),
            ("7", "Hearts"),
            ("6", "Hearts"),
            ("5", "Hearts"),
            ("4", "Hearts"),
            ("3", "Hearts"),
            ("2", "Hearts"),
            ("Ace", "Hearts"),
            None,
        ],
    ),
]


def test(action, num_cards, expected):
    print("---------------------------------")
    print(f"Testing action: {action}, dealing {num_cards} cards")
    print(f"Expected Output:")
    print_cards(expected)
    deck = DeckOfCards()
    random.seed(1)
    result = []

    if action == "shuffle_deck":
        print("Shuffling deck...")
        deck.shuffle_deck()
        print(f"dealing {num_cards} cards")
        for _ in range(num_cards):
            result.append(deck.deal_card())

    elif action == "deal_card":
        for _ in range(num_cards):
            result.append(deck.deal_card())

    print(f"Actual Output:")
    print_cards(result)
    if result == expected:
        print("Pass")
        return True
    else:
        print("Fail")
        return False


def print_cards(cards):
    for card in cards:
        if card is None:
            print("* <None>")
        else:
            print(f"* {card[0]} of {card[1]}")


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
