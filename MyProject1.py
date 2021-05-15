import random
name = input("Enter your name : ")
print(f"Hello {name.title()},\nYour name contains {len(name)} alphabets.")
if len(name) <=0:
    print("You didn\'t entered any name. No problem, let\'s play a game.")
elif len(name) <5:
    print("It\'s a very small name.\nNow, let\'s play a game.")
elif 5<= len(name) <=8:
    print("You entered a name that contains average characters.\nNow, let\'s play a game.")
else:
    print("It\'s a very big name. I think you entered your full name.\nNow, let\'s play a game.")
congrats = "\U0001F600 " + "Congratulations you guess the currect number "

num1 = 88
guessing_number1 = int(input("Guess a number between 1 to 99 : "))

if num1 == guessing_number1:
    print(congrats)

else:
    if num1 > guessing_number1:
        print("Sorry you choose a smaller number.")
    if num1 < guessing_number1:
        print("Sorry, you choose a bigger number.")

num2 = random.randint(1, 9) # using a random number
guessing_number2 = int(input("Guess a number between 1 to 9 : "))

if guessing_number2 == num2:
    if num2 == guessing_number2 and num1 == guessing_number1:
        print(congrats + "again.")
    else:
        print(congrats)

else:
    print("Sorry you chose the wrong number")

if num1 != guessing_number1 and num2 != guessing_number2:
    print("Opps, looks like you lose again.\nNow, let me make it easy for you.")

    num3 = random.randint(1, 2)
    gdl = "Good Luck"
    guessing_number3 = int(input("Guess a number between 1 or 2 : "))

    if num3 == guessing_number3:
        print("Yahoo! Finally, you win." + " \U0001F600" )
    else:
        print("So Sad, you lose once agaian.\nPlease start from the begining and play with me again.")
        print(gdl.center(19, "*"))
else:
    pass