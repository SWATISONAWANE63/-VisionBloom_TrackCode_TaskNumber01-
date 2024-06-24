# import random

# def get_computer_choice():
#     choices = ['rock', 'paper', 'scissors']
#     return random.choice(choices)

# def get_user_choice():
#     while True:
#         user_input = input("Enter your choice (rock, paper, or scissors) or 'exit' to quit: ").lower()
#         if user_input in ['rock', 'paper', 'scissors', 'exit']:
#             return user_input
#         else:
#             print("Invalid input. Please try again.")

# def determine_winner(user_choice, computer_choice):
#     if user_choice == computer_choice:
#         return "It's a tie!"
#     elif (user_choice == 'rock' and computer_choice == 'scissors') or \
#          (user_choice == 'paper' and computer_choice == 'rock') or \
#          (user_choice == 'scissors' and computer_choice == 'paper'):
#         return "You win!"
#     else:
#         return "You lose!"

# def play_game():
#     print("Welcome to Rock, Paper, Scissors!")
    
#     while True:
#         user_choice = get_user_choice()
#         if user_choice == 'exit':
#             print("Thanks for playing! Goodbye!")
#             break
        
#         computer_choice = get_computer_choice()
#         print(f"Computer chose: {computer_choice}")
        
#         result = determine_winner(user_choice, computer_choice)
#         print(result)

# if __name__ == "__main__":
#     play_game()
