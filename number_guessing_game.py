import random

print("=" * 40)
print("WELCOME TO NUMBER GUESSING GAME")
print("=" * 40)

while True:

    print("\nChoose Difficulty")
    print("1. Easy (1 - 50)")
    print("2. Medium (1 - 100)")
    print("3. Hard (1 - 200)")

    choice = input("Enter your choice (1/2/3): ")

    if choice == "1":
        limit = 50
    elif choice == "2":
        limit = 100
    elif choice == "3":
        limit = 200
    else:
        print("Invalid Choice! Default level selected.")
        limit = 100

    secret_number = random.randint(1, limit)

    attempts = 0
    max_attempts = 10

    print(f"\nGuess the number between 1 and {limit}")
    print(f"You have {max_attempts} attempts.\n")

    while attempts < max_attempts:

        try:
            guess = int(input("Enter your guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        attempts += 1

        if guess < 1 or guess > limit:
            print("Number is out of range.")
            continue

        if guess < secret_number:
            print("Too Low!")
        elif guess > secret_number:
            print("Too High!")
        else:
            print("\n🎉 Congratulations!")
            print("You guessed the correct number.")
            print("Attempts Used:", attempts)
            print("Score:", (max_attempts - attempts + 1) * 10)
            break

        print("Remaining Attempts:", max_attempts - attempts)

    else:
        print("\n Game Over!")
        print("The correct number was:", secret_number)

    play = input("\nDo you want to play again? (yes/no): ").lower()

    if play != "yes":
        print("\nThank you for playing!")
        print("Have a great day ")
        break