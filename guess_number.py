number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))

cap = 10

if guess == number:
   print("Congratulations! You guessed the right number.")
else:
    print("No you guessed wrong, try again")
    while guess != number:
        guess = (input("What number am I thinking of? "))
        cap = cap - 1
        print(f'You have {cap} guesses left to correctly guess the number')
        if guess == 'q':
            print(f"The number is {number}")
            break
        if int(guess) == number:
            print("Congratulations! You guessed the right number.")
            break
        if int(guess) != number:
            print("No you guessed wrong, try again")
        if cap == 0:
            print(f"The number is {number}")
            break
            if int(guess) > number:
                print("You guessed too high")
            if int(guess) < number:
                print("You guessed too low")


