from art import logo, vs
from data import data
import random
import os
clear = lambda: os.system('clear')


def play_game():
    score = 0
    current_topic = random.choice(data)
    comparing_topic = random.choice(data)
    guessed_wrong = False
    while not guessed_wrong:
        clear()
        if comparing_topic['follower_count'] > current_topic['follower_count']:
            correct_answer = 'B'
        else:
            correct_answer = 'A'
        print(logo)
        print(f"Compare A. {current_topic['name']}, a {current_topic['description']} from {current_topic['country']}")
        print(vs)
        print(f"Compare B. {comparing_topic['name']}, a {comparing_topic['description']} from {comparing_topic['country']}")
        answer = input('Who has more followers? Type "A" or "B": ')
        if answer == correct_answer:
            score += 1
            current_topic = comparing_topic
            comparing_topic = random.choice(data)
        else:
            guessed_wrong = True
            print(f"That's wrong! Your final score was {score}")

while input("Would you like to play the Higher-Lower game? Type 'y' for yes:  ") == 'y':
    play_game()