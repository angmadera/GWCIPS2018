def intro():
    while(True):

        name = input("Hello, I am a friendly bot. What is your name? ")
        print("Nice meeting you, {}!".format(name))
        break

def roll_dice():
    d = input("Press 'D' to roll the dice. ")
    if d == "d":
        from random import randint
        x = randint(1, 6)
        print("You rolled", x)

def roll_twice():
        roll_again = input("Would you like to roll again? ")
        if roll_again == "yes":
            roll_dice()
        elif roll_again == "no":
            main()
        else:
            main()

def roll():
    roll_dice()
    roll_twice()

def joke_main():
    joke_answer = input("Would you like to hear another joke?")
    if joke_answer == "yes":
        print(v)
    if joke_answer == "no":
        main()

def joke1():
    input("Knock Knock. ")
    input("Esch. ")
    print("Bless you! ")

def joke2():
    input("What do you call a snowman in July?")
    print("A puddle.")

def joke3():
    input("What does a dolphin say when he is confused?")
    print("Be more Pacific.")

def joke4():
    input("Why does Snoop Dogg need an umbrella?")
    print("Fo' Drizzle.")

jokelist = [joke1(), joke2(), joke4(), joke3()]

def main():
    choice = input("What may I help you with? I can tell jokes and roll dice. If you would like to exit, please press the number 1 button. ")
    if choice == "roll dice":
        roll()
    elif choice == "tell joke":
        v = random.choice(jokelist)
        print(v)
        joke_main()
    elif choice == "1":
        exit()
    else:
        print("That is not a choice. Please try again!")
        print(choice)

print(intro())
print(main())
