"""
Higher or Lower
"""
############### Higher or Lower #####################
# Euuuuuuuu

from day9_1 import logo5, vs, data
import random

print(logo5)
CHAMPION = random.choice(data)
POINTS = 0
GAME_OVER = False

def fight():
    global CHAMPION
    challenger = random.choice(data)
    while challenger == CHAMPION:
        challenger = random.choice(data)
    print(f"Compare A: {CHAMPION['name']}, {CHAMPION['description']}, from {CHAMPION['country']}.")
    print(vs)
    print(f"Compare B: {challenger['name']}, {challenger['description']}, from {challenger['country']}.")
    return challenger

def bet():
    global POINTS
    global CHAMPION
    global GAME_OVER

    while not GAME_OVER:
        challenger = fight()
        player_choice = input('Who has more followers? Type \'A\' or \'B\': ').lower()
        if CHAMPION['follower_count'] > challenger['follower_count']:
            if player_choice == 'a':
                CHAMPION = CHAMPION
                POINTS += 1
                print(f'You\'re right! Current score:{POINTS}.')
            else:
                GAME_OVER = True
                print(f'Sorry, that\'s wrong. Final score:{POINTS}.')
        if CHAMPION['follower_count'] < challenger['follower_count']:
            CHAMPION = challenger
            if player_choice == 'b':
                 CHAMPION = challenger
                POINTS += 1
                print(f'You\'re right! Current score:{POINTS}.')
            else:
                GAME_OVER = True
                print(f'Sorry, that\'s wrong. Final score:{POINTS}.')
bet()

############### Higher or Lower #####################
# Dr. Angela Yu
"""
from day9_1 import logo5, vs, data
import random

def get_random_account():
    """Get data from random account"""
    return random.choice(data)

def format_data(account):
    """Format account into printable format: name, description and country"""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    # print(f'{name}: {account["follower_count"]}')
    return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
    """Checks followers against user's guess
    and returns True if they got it right.
    Or False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def game():
    print(logo5)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()
    while game_should_continue:
        account_a = account_b
        account_b = get_random_account()
        while account_a == account_b:
            account_b = get_random_account()
        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")
        guess = input("Who has more followers? Type 'A' or 'B': ").lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)
        print(logo5)
        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.")
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")
game()
"""