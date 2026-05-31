import random

words = ["python", "hangman", "laptop", "journey", "galaxy"]

word = random.choice(words)
guessed = []
wrong = 0
max_wrong = 6

print("Welcome to Hangman!")
print("The word has", len(word), "letters.")

while wrong < max_wrong:
    display = ""
    for letter in word:
        if letter in guessed:
            display += letter + " "
        else:
            display += "_ "
    print("\nWord:", display)
    print("Wrong guesses left:", max_wrong - wrong)

    if len(guessed) == 0:
        print("Guessed letters: None")
    else:
        print("Guessed letters:", guessed)

    if "_" not in display:
        print("Congratulations! You guessed the word:", word)
        break

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    if guess in guessed:
        print("You already guessed that letter.")
        continue

    guessed.append(guess)

    if guess in word:
        print("Good guess!")
    else:
        wrong += 1
        print("Wrong guess!")

else:
    print("Game over! The word was:", word)
