print("Welcome to treasure island. Find the treasure")
choice1 = input(
    'You\'re in a crossroad, where want to go? Type "left" or "right".\n'
).lower()

if choice1 == "left":
    choice2 = input("wait or swim\n").lower()
    if choice2 == "swim":
        choice3 = input("red or blue\n").lower()
        if choice3 == "red":
            print("You win")
        else:
            print("You lost")
    else:
        print("You lost")
else:
    print("You lost")
