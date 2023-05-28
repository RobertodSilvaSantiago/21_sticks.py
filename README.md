# 21_sticks.py

This code is implementing a game where the player plays against a bot that always makes calculated moves. The game is played with a pile of 21 sticks, and the players take turns removing a certain number of sticks from the pile. The objective of the game is to force the opponent to take the last stick.

Here's a breakdown of the code:

The get_valid_input function takes a prompt as input and repeatedly prompts the user to enter a number between 1 and 3 until a valid input is received. It checks if the user input is a digit and within the range [1, 2, 3]. If the input is valid, it is returned as an integer.

The calculate_bot_move function takes the current number of sticks in the game as input and returns the number of sticks the bot should take. The function follows a predetermined strategy based on the number of sticks remaining. It has specific cases for sticks 1-7, and for any other number of sticks, it calculates the number of sticks to take based on a formula.

The play_game function simulates the game. It initializes the number of sticks to 21 and the current player to 1. It continues the game as long as there are sticks remaining. In each iteration, it displays the number of sticks remaining. If it's the bot's turn (player 1), it calls the calculate_bot_move function to determine the number of sticks the bot should take. If it's the player's turn, it prompts for input using the get_valid_input function. It checks for valid input and continues the loop until a valid input is received. It then updates the number of sticks remaining and switches the player. The game ends when there are no sticks left, and it declares the bot as the winner.

The main function is the entry point of the program. It simply calls the play_game function.

The if __name__ == "__main__": condition ensures that the main function is executed only if the script is run directly, not when it's imported as a module.

Overall, the code sets up a simple game where the bot always wins by making calculated moves.




