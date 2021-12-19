import random

logo =  """
   ______                        ________            _   __                __             
  / ____/_  _____  __________   /_  __/ /_  ___     / | / /_  ______ ___  / /_  ___  _____
 / / __/ / / / _ \/ ___/ ___/    / / / __ \/ _ \   /  |/ / / / / __ `__ \/ __ \/ _ \/ ___/
/ /_/ / /_/ /  __(__  |__  )    / / / / / /  __/  / /|  / /_/ / / / / / / /_/ /  __/ /    
\____/\__,_/\___/____/____/    /_/ /_/ /_/\___/  /_/ |_/\__,_/_/ /_/ /_/_.___/\___/_/     
                                                                                       
"""
print(logo)
def start_game(turns):
  num_of_turns = turns
  game_over = False
  number = random.randint(1, 100)

  

  while not game_over:
    guess = input("I'm thinking of a number between 1 and 100. Guess a number.")
    if int(guess) == number:
      print(f"You win! The number was {number}")
      game_over = True
    elif int(guess) > number:
      print("Too High")
      num_of_turns -= 1
      print(f"Turns Remaining: {num_of_turns}")   
    else:
      print("Too Low")
      num_of_turns -= 1
      print(f"Turns Remaining: {num_of_turns}")
    
    if num_of_turns == 0:
      print(f"You ran out of turns. The number was {number}. You lose.")
      game_over = True
  
        
difficulty = input("Choose a difficulty, type easy or hard.")
if difficulty == "easy":
  start_game(10)
elif difficulty == "hard":
  start_game(5)
else:
  print("Please choose either easy or hard")
