import random
from os import system, name


def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def deal_cards():
    card = random.choice(cards)
    return card


def calculate_score(player_cards):
    if sum(player_cards) == 21 and len(player_cards) == 2:
        return 0
    if 11 in player_cards and sum(player_cards) > 21:
        player_cards.remove(11)
        player_cards.append(1)
    return sum(player_cards)


def compare_score(user_score, computer_score):
    if user_score > 21 and computer_score > 21:
        return "Your score went over. You LOSE\n\n"

    if user_score == computer_score:
        return "Draw\n\n"
    elif computer_score == 0:
        return "Opponent has a BLACKJACK. You LOSE\n\n"
    elif user_score == 0:
        return "You have a BLACKJACK. You WIN\n\n"
    elif computer_score > 21:
        return "Opponent's Score went over. You WIN\n\n"
    elif user_score > 21:
        return "Your Score went over. You LOSE\n\n"
    elif user_score > computer_score:
        return "You WIN\n\n"
    else:
        return "You LOSE\n\n"


def play_game():
    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append((deal_cards()))
        computer_cards.append(deal_cards())

    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"    Your Cards are {user_cards} and Your Score is {user_score}")
        print(f"    Opponents Card is [{computer_cards[0]}]")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            deal = input("Enter y to deal or any other input to pass: ")
            if deal == 'y' or deal == 'Y':
                user_cards.append(deal_cards())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_cards())
        computer_score = calculate_score(computer_cards)

    print(f"    Your final hand: {user_cards}, final score: {user_score}")
    print(f"    Computer's final hand: {computer_cards}, final score: {computer_score}\n\n")
    print(compare_score(user_score, computer_score))


if __name__ == '__main__':
    choice = "y"
    print("Welcome to BLACKJACK")
    while choice == 'y' or choice == 'Y':
        choice = input("Do you want to play a Hand? (y for YES or any other key for NO): ")
        clear()
        if choice == 'y' or choice == 'Y':
            play_game()
        else:
            print("Thanks for playing!")
            exit(0)
