#print the starting words of the game
#
import random
#end = False
def guessing_game():
    end = False
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100")
    number_chosen = random.randint(1,100)
    difficulty = input("Chose a difficulty. 'easy' or 'hard' \n")
    if difficulty == "easy":
        attempts = 10
    else: 
        attempts = 5
    #print(number_chosen)
    def easy():
        print("You have 10 attempts to guess the number")

    def hard():
        print("You have 5 attempts to guess the number")
        #attempts = 10
    if difficulty == "easy":
        easy()
    else:
        hard()
    while not end: 
        guess = int(input("Guess a number \n"))
        if guess != number_chosen:
            attempts -= 1
            if guess < number_chosen:
                print(f"Too low! You have {attempts} attempts left ")
            elif guess > number_chosen:
                print(f"Too high! You have {attempts} attempts left ")
        else:
            end = True
            print(f"You got it! the number is {number_chosen}")
        if attempts == 0 and guess != number_chosen:
            end = True
            print("You lose!")
        if end == True:
            go_again = input("Would you like to go again? y or n")
            if go_again == "y":
                guessing_game()   
guessing_game()