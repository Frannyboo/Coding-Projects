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
# end_of_game = False
# lives = 5
def game():
  end_of_game = False
  lives = 5
  while not end_of_game:
    player = int(input("pick a number, 0 for rock, 1 for paper and 2 for scissors \n"))
    number_chosen = random.randint(0,2)
    #number_chosen is the computer playing
    if number_chosen == 0:
      print(f"Computer chose \n {rock}")
    elif number_chosen == 1:
      print(f"Computer chose \n {paper}")
    else:
      print(f"Computer chose \n {scissors}")

    if player == 0:
      print(f"You chose \n {rock}")
    elif player == 1:
      print(f"You chose \n {paper}")
    elif player == 2:
      print(f"You chose \n {scissors}")
    else:
      print("Please pick a valid number")

    if number_chosen == 0 and player == 1:
      print("You win!")
    elif number_chosen == 1 and player == 0:
      lives -= 1
      print(f"You lose! you have {lives} lives left")
    elif number_chosen == 1 and player == 2:
      print("You win!")
    elif number_chosen == 2 and player == 1:
      lives -= 1
      print(f"You lose! you have {lives} lives left")
    elif number_chosen == 0 and player == 2:
      lives -= 1
      print(f"You lose! you have {lives} lives left")
    elif number_chosen == 2 and player == 0:
      print("You win!")

    if lives == 0:
      end_of_game = True         
      go_again = input("Do you want to play again? y or n \n")
      if go_again == "y":
        game()
      else:
        end_of_game = True
game()