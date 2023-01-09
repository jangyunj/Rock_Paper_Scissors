import random

user_points = 0
computer_points = 0

print('Welcome to the game of Rock, Paper, Scissors! :D')
while True:
    options = ['rock', 'paper',' scissors']
    user_input = input("--Make a selection--\nRock, Paper, Scissors OR Exit to quit the game: ").lower()
    computer_input = random.choice(options)

    if user_input == 'exit':
        print('\nYou have chosen to exit the game.\nHave a great day, goodbye!')
        print(f'---Final Score---\n You: {user_points} \n Computer: {computer_points}\n')
        quit()

    if user_input == 'rock':
        print("You have chosen rock.")
        if computer_input == 'rock':
            print("The computer has chosen rock. It's a tie! \n")
        elif computer_input == 'paper':
            print("The computer has chosen paper. Computer wins! \n")
            computer_points += 1
        elif computer_input == 'scissors':
            print("The computer has chosen scissors. You win! \n")
            user_points += 1

    elif user_input == 'paper':
        print("You have chosen paper.")
        if computer_input == 'paper':
            print("The computer has chosen paper. It's a tie! \n")
        elif computer_input == 'rock':
            print("The computer has chosen rock. You win! \n")
            user_points += 1
        elif computer_input == 'scissors':
            print("The computer has chosen scissors. Computer wins! \n")
            computer_points += 1

    elif user_input == 'scissors':
        print("You have chosen scissors.")
        if computer_input == 'scissors':
            print("The computer has chosen scissors. It's a tie! \n")
        elif computer_input == 'rock':
            print("The computer has chosen rock. Computer wins! \n")
            computer_points += 1
        elif computer_input == 'paper':
            print("The computer has chosen paper. You win! \n")
            user_points += 1

    else:
        print('Invalid input \n')



