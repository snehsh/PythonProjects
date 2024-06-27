import random
from art import logo

money_in_bank = 1000

def deal_card():
    """Returns a random card from the deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card

def calculate_score(cards):
    """Take a list of cards and return the score calculated from the cards"""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)

def compare(user_score, computer_score, bet):
    global money_in_bank
    if user_score > 21 and computer_score > 21:
        money_in_bank -= bet
        return f"You went over. You lose 😤, current balance: {money_in_bank}"
    if user_score == computer_score:
        return f"Draw 🙃, current balance: {money_in_bank}"
    elif computer_score == 0:
        money_in_bank -= bet
        return f"Lose, opponent has Blackjack 😱, current balance: {money_in_bank}"
    elif user_score == 0:
        money_in_bank += bet
        return f"Win with a Blackjack 😎, current balance: {money_in_bank}"
    elif user_score > 21:
        money_in_bank -= bet
        return f"You went over. You lose 😭, current balance: {money_in_bank}"
    elif computer_score > 21:
        money_in_bank += bet
        return f"Opponent went over. You win 😁, current balance: {money_in_bank}"
    elif user_score > computer_score:
        money_in_bank += bet
        return f"You win 😃, current balance: {money_in_bank}"
    else:
        money_in_bank -= bet
        return f"You lose 😤, current balance: {money_in_bank}"

def play_game():
    global money_in_bank
    print(logo)
    global bet
    bet = int(input(f"How much would you like to bet?, money in bank is: {money_in_bank}: "))
    user_cards = []
    computer_cards = []
    is_game_over = False
    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: ")
            if user_should_deal == "y":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"   Your final hand: {user_cards}, final score: {user_score}")
    print(f"   Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score, bet))

while input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y" and money_in_bank > 0:
    play_game()
