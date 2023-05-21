# Day 11 of 100 for the Udemy Python Bootcamp
# Blackjack game capstone project

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

# Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

# Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

from art import logo
import random
import os

# This is moved to the top of the code to ensure it can be called at anytime
# Hint 6: Create a function called calculate_score() that takes a List of cards as input and returns the score. Look up the sum() function to help you do this.
# Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.
def calculate_score(cards):
    """Takes a list of cards in hand and returns a score from them"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
# Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

# Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.
def compare_score(user_score, computer_score):
    """Checks the win/lose condition for the user and the computer opponent"""
    if user_score == computer_score:
        return "Draw"
    elif computer_score == 0:
        return "You Lose, the opponent has Blackjack"
    elif user_score == 0:
        return "You Win! You got Blackjack!"
    elif user_score > 21:
        return "You went over. You Lose."
    elif computer_score > 21:
        return "You Win! Your opponent went over."
    elif user_score > computer_score:
        return "You Win!"
    else:
        return "You Lose."

# Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
# 11 is the Ace.
# cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def deal_card():
    """Picks a random card from the deck"""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def play_blackjack():
    print(logo)
    # Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
    user_cards = []
    computer_cards = []
    game_over = False

    for card in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    # DEBUG STEP
    # print(f"User Cards = {user_cards}, Comptuer Cards = {computer_cards}")

    # Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"Users Hand = {user_cards}, User Total = {user_score}")
        print(f"Opponents Hand = {computer_cards[0]}\n")

        # Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.
        while computer_score != 0 and computer_score < 17:
            computer_cards.append(deal_card())
            computer_score = calculate_score(computer_cards)

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        #Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.
        else:
            user_should_deal = input("Press 'y' to hit, and press 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
                # Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.
            else:
                game_over = True

        # Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
        print(f"Your Hand = {user_cards}, your card total = {user_score}")
        print(f"Opponents Hand = {computer_cards}, with a total of {computer_score}")
        print(compare_score(user_score, computer_score))

while input("\nDo you want to play a game of Blackjack? Type 'y' to play, press 'q' to quit: ") == "y":
    os.system("cls")
    play_blackjack()

