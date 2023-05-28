"""This function takes a prompt as an input and repeatedly prompts
the user to enter a number between 1-3 until a valid input is received"""
def get_valid_input(prompt):
  while True:
    user_input = input(prompt)
    if user_input.isdigit() and int(user_input) in [1, 2, 3]:
      return int(user_input)
    print("Invalid input, please enter a number between 1-3")


"""The function takes the current number of sticks in the game as an input
and returns the number of sticks the bot should take"""
def calculate_bot_move(sticks):
  if sticks == 1:
    Bot = 1
  elif sticks == 2:
    Bot = 2
  elif sticks == 3:
    Bot = 3
  elif sticks == 4:
    Bot = 1
  elif sticks == 5:
    Bot = 1
  elif sticks == 6:
    Bot = 2
  elif sticks == 7:
    Bot = 3
  else:
    sticks_taken = (sticks - 1) % 4
    if sticks_taken == 0:
      Bot = 1
    else:
      Bot = sticks_taken
  return Bot

"""This function simulates a game where the bot always wins by making
calculated moves, the function tracks remaining sticks and current player"""
def play_game():
  sticks = 21
  player = 1
  while sticks > 0:
    print(f"{sticks} sticks in the pile.")
    if player == 1:
      sticks_taken = calculate_bot_move(sticks)
      print(f"Bot takes: {sticks_taken}")
    else:
      sticks_taken = get_valid_input(f"Player {player} takes: ")
      if sticks_taken > sticks or sticks_taken > 3:
        print("Invalid input, please enter a valid number of sticks")
        continue
    sticks -= sticks_taken
    if sticks <= 0:
      break
    player = 3 - player 
  print("0 sticks in the pile.\n")
  print(f"Bot {player} won!")


"""The main() function is the entry point of the program that executes
the bot game"""
def main():
  play_game()
 

if __name__ == "__main__":
  main()
