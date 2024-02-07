number = 10

print("I'm thinking of a number...")
guess = int(input("What number am I thinking of? "))


if guess == number:
   print("Congratulations! You guessed the right number.")
else:
    print("No you guessed wrong, try again")
    while guess != number:
        guess = (input("What number am I thinking of? "))
        if guess == 'q':
            print(f"The number is {number}")
            break
        if int(guess) == number:
            print("Congratulations! You guessed the right number.")
            break
        if int(guess) != number:
            print("No you guessed wrong, try again")

