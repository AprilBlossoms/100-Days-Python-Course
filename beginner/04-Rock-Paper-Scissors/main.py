rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random
options = [rock, paper, scissors]
answer = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
computer_answer = random.choice(options)
print("You chose:")
print(options[int(answer)])
print("Computer chose:")
print(computer_answer)
if int(answer) == 0:
  if computer_answer == scissors:
    print("You Win")
  elif computer_answer == rock:
    print("It's A Draw")
  else:
    print("You Lose")
elif int(answer) == 1:
  if computer_answer == scissors:
    print("You Lose")
  elif computer_answer == rock:
    print("You Win")
  else:
    print("It's A Draw")
else:
  if computer_answer == scissors:
    print("It's A Draw")
  elif computer_answer == rock:
    print("You Lose")
  else:
    print("You Win")