def add(n1 , n2):
    return n1 + n2

def subtract(n1 , n2):
    return n1 - n2

def divide(n1 , n2):
    return n1 / n2

def multiply(n1 , n2):
    return n1 * n2

operations = {
    "+" : add, 
    "-" : subtract, 
    "/" : divide, 
    "*" : multiply,
}
def calculator():
    num1 = float(input("Whats the first number?: \n"))
    for sign in operations:
        print(sign)
    opp = input("Pick an operation from the list above?: \n")
    if opp not in operations:
        print("You entered an invalid value")
        opp = input("Pick an operation from the list above?: \n")




    num2 = float(input("Whats the second number?: \n"))
    operation_chosen = operations[opp]
    answer = operation_chosen(num1 , num2)

    print(f"{num1} {opp} {num2} = {answer}")
    end = False
    while not end:
        end_game = input(f"Type y if you want to continue working with {answer}, type n to start again  and e to end\n")
        if end_game == "y":
            for sign in operations:
                print(sign)
            opp = input("Pick an operation from the list above?: \n")
            num3 = float(input("Pick another number \n"))
            operation_chosen = operations[opp]
            new_number = answer
            answer = operation_chosen(new_number , num3)

            print(f"{new_number} {opp} {num3} = {answer}")
        elif end_game == "e":
            end = True
        else:
            end = True
            calculator()
calculator()