import random


def converting_ace(sum_list, input_cards):
    if sum_list > 21:
        for i in range(len(input_cards)):
            if input_cards[i] == 11:
                input_cards.remove(input_cards[i])
                input_cards.insert(i, 1)
    return input_cards


play_game = True
while play_game:
    play_or_not = input("Do you want play game of Blackjack? Type 'y' or 'n': ").lower()
    if play_or_not == "y":
        print("BLACKJACK")

        cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

        user_cards = []
        first_card = random.choice(cards)
        user_cards.append(first_card)
        second_card = random.choice(cards)
        user_cards.append(second_card)

        user_cards = converting_ace(sum(user_cards), user_cards)
        user_sum = sum(user_cards)

        computer_cards = []
        computer_card = random.choice(cards)
        computer_cards.append(computer_card)

        another_card = True
        print(f"Your cards {user_cards}, current score: {user_sum}")
        print(f"Computer's first card: {computer_card}")
        if user_sum > 21:
            print("You lost...")
            another_card = False

        while another_card:
            further_choice = input("Type 'y' to get another card, type 'n' to pass: ").lower()
            if further_choice == "y":
                another_card = random.choice(cards)
                user_cards.append(another_card)
                user_cards = converting_ace(sum(user_cards), user_cards)
                user_sum = sum(user_cards)
                print(f"Your cards {user_cards}, current score: {user_sum}")
                print(f"Computer's first card: {computer_card}")
                if user_sum > 21:
                    print("You lost...")
                    another_card = False
            elif further_choice == "n":
                another_card = False
                while sum(computer_cards) < 18:
                    computer_cards.append(random.choice(cards))
                    computer_cards = converting_ace(sum(computer_cards), computer_cards)
                user_sum = sum(user_cards)
                if user_sum <= 21:
                    if sum(computer_cards) > 21:
                        print(f"Your final hand: {user_cards}, final score: {user_sum}")
                        print(f"Computer's final hand {computer_cards}, final score: {sum(computer_cards)}")
                        print("Opponent went over. You win! :)")
                    elif user_sum > sum(computer_cards):
                        print(f"Your final hand: {user_cards}, final score: {user_sum}")
                        print(f"Computer's final hand {computer_cards}, final score: {sum(computer_cards)}")
                        print("You win! :)")
                    elif user_sum < sum(computer_cards):
                        print(f"Your final hand: {user_cards}, final score: {user_sum}")
                        print(f"Computer's final hand {computer_cards}, final score: {sum(computer_cards)}")
                        print("Opponent win! ")
                    else:
                        print(f"Your final hand: {user_cards}, final score: {user_sum}")
                        print(f"Computer's final hand {computer_cards}, final score: {sum(computer_cards)}")
                        print("Draw")
                else:
                    print(f"Your final hand: {user_cards}, final score: {user_sum}")
                    print("You lost...")
    else:
        play_game = False

