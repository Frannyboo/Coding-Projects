from stuff import people_a 
from stuff import vs, hlg_logo
import random
game_continue = True
# make 2 dictionaries to have the name of the person as the key and the more info as the value
score = 0
# make 2 variables which would take a random choice from each of the dictionaries

    #choice_b = random.choice(people_a)
print(hlg_logo)
choice_a = random.choice(people_a)
choice_b = random.choice(people_a)
if choice_a == choice_b:
    choice_b = random.choice(people_a)
# use a print statement to display the words

person_name_a = choice_a["name"]
person_descr_a = choice_a["description"]
person_country_a = choice_a["country"]
person_followers_a = choice_a["followers"]

person_name_b = choice_b["name"]
person_descr_b = choice_b["description"]
person_country_b = choice_b["country"]
person_followers_b = choice_b["followers"]


def compare(person_followers_a , person_followers_b):
    if person_followers_a > person_followers_b:
        return "A"
    elif person_followers_a < person_followers_b:
        return "B"

case_a = print(f"Compare A: {person_name_a}, {person_descr_a} from {person_country_a}")
print(vs)
case_b = print(f"Against B: {person_name_b}, {person_descr_b} from {person_country_b}")

guess = input("Who do you think has more followers A or B?:").upper()
answer = compare(person_followers_a, person_followers_b)
while game_continue: 
    if guess == answer:
        score += 1
        print(f"You were right! your current score is {score}")
        if answer == "A":
            case_a = print(f"Compare A: {person_name_a}, {person_descr_a} from {person_country_a}")
            print(vs)
            choice_b = random.choice(people_a)
            person_name_b = choice_b["name"]
            person_descr_b = choice_b["description"]
            person_country_b = choice_b["country"]
            person_followers_b = choice_b["followers"]
            if choice_a == choice_b:
               choice_b = random.choice(people_a) 
            case_b = print(f"Against B: {person_name_b}, {person_descr_b} from {person_country_b}")
            answer = compare(person_followers_a , person_followers_b)
        else:
            case_a = print(f"Compare A: {person_name_b}, {person_descr_b} from {person_country_b}")
            print(vs)
            choice_b = random.choice(people_a)
            person_name_b = choice_b["name"]
            person_descr_b = choice_b["description"]
            person_country_b = choice_b["country"]
            person_followers_b = choice_b["followers"]
            if choice_a == choice_b:
                choice_b = random.choice(people_a) 
            case_b = print(f"Against B: {person_name_b}, {person_descr_b} from {person_country_b}")
            answer = compare(person_followers_a , person_followers_b)
        #case_c = print(f"Against B: {person_name_c}, {person_descr_c} from {person_country_c}")
        guess = input("Who do you think has more followers A or B?:").upper()

    elif guess != answer:
        print(f"The correct answer is {answer}")
        print(f"Your score is {score}")
        game_continue = False
