# 🚨 Don't change the code below 👇
print("Welcome to the BMI calculator")
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_square = height**2
bmi = round(float(weight / height_square))
if bmi < 18.5:
    print(f"Your bmi is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi < 25:
    print(f"Your bmi is {bmi}, you are normal weight")
elif bmi > 25 and bmi < 30:
    print(f"Your bmi is {bmi}, you are slightly overweight")
elif bmi > 30 and bmi < 35:
    print(f"Your bmi is {bmi}, you are obese")
else:
    print(f"Your bmi is {bmi}, you are clinically obese")
