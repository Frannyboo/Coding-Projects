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
end_of_game = False
#while end_of_game:
player = int(input("pick a number, 0 for rock, 1 for paper and 2 for scissors"))
random = random.randint(0,2)
if random == 0:
  print(f"Computer chose \n {rock}")
elif random == 1:
  print(print(f"Computer chose \n {paper}"))
else:
  print(print(f"Computer chose \n {scissors}"))

if player == 0:
  print(f"You chose \n {rock}")
elif player == 1:
  print(f"You chose \n {paper}")
elif player == 2:
  print(f"You chose \n {scissors}")
else:
  print("Please pick a valid number")

if random == 0 and player == 1:
  print("You win!")
elif random == 1 and player == 0:
  print("You lose!")
elif random == 1 and player == 2:
  print("You win!")
elif random == 2 and player == 1:
  print("You lose!")
elif random == 0 and player == 2:
  print("You lose!")
elif random == 2 and player == 0:
  print("You win!")

        



    