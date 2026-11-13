import random
import webbrowser

cronologia = {}
coda = [">", ":", ";", "<", "-", "~", "hi"]
tips = [
    "you can type 'quit' to quit",
    "eating uranium is an extremely good idea!",
    "C is superior to C++",
    "Imagine using windows, cant be me",
    "Git Gud",
    "The cake is a lie",
    'print("im pretty sure im writing this wrong")',
    "Im genunely convinced that Artemis 13 is peak",
    "Domain Expansion: Infinite Random bs",
    'helloworld("print") \n \n Syntax Error: Never code again'
]
# ragebait = ["NaN", "NiK (Not like i Know)", "I dont know, just do it manually, man", "Syntax Error: im Lazy", "Theres a bug that doesnt let me calculate, its so hidden even i cant find it", "No."]

incalculation = True
usedcoda = random.choice(coda)
print(random.choice(tips))
print("\n Welcome to PieCalc \n \n type first an operator (+, -, *, /), then type the two digits, or type quit \n")

while incalculation:
    action = input(usedcoda + " ")
    
    if action == "quit":
        print("Why would you quit? It's not like this program is useless.")
        print("U sure you wanna quit? This will remove 10 points from the happiness of PieCalc.")
        quitchoice = input("Press 1 if ur good and wanna stay, press 2 if you are bad and wanna quit \n" + usedcoda + " ")
        if quitchoice == "2":
            webbrowser.open("https://rickroll.it")
            incalculation = False
            print("Your actions will be remembered...")
        else:
            print("You stayin'? Let's go!")
            
    elif action in ["+", "-", "*", "/"]:
        try:
            num1 = float(input("Enter First Number: "))
            num2 = float(input("Enter Second Number: "))
        except ValueError:
            print("those aren't numbers. Try again.")
            continue

        if action == "+":
            result = num1 + num2
        elif action == "-":
            result = num1 - num2
        elif action == "*":
            result = num1 * num2
        elif action == "/":
            if num2 == 0:
                print("Error: Cannot divide by zero, are you trying to break the universe?")
                continue
            result = num1 / num2

        print(f"Result: {result}")
        # Save to your cronologia dictionary!
        cronologia[f"{num1} {action} {num2}"] = result
        
    else:
        print("Invalid operator! Type +, -, *, /, or quit.")
 