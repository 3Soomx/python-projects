import random as rd
import colorama as cl
from colorama import Fore, Back, Style

options = ["rock","paper","scissor"]
cu = 0
cc = 0
i = 0
while True:
    user_input = input("Type Rock / Paper / Scissor /, Or q to Quit ").lower()

    if user_input == "q" :
        break
    if user_input not in options:
        continue
    rand_num = rd.randint(0,2)
    c_pick =options[rand_num]
    print("Computer Picked : ", c_pick)

    
    if user_input == "rock" and c_pick == "scissor" :
      print("You is win! ")
      cu += 1
    elif user_input == "scissor" and c_pick == "paper" :
      print("You is win! ")
      cu += 1  
    elif user_input == "paper" and c_pick == "rock" :
      print( '\033[31m'+ 'You is win!')
      cu += 1  
    else:
        print("Computer is win! ")
        cc += 1

print("You won", cu, "times")
print("The computer won", cc, "times")

print("Goodby")