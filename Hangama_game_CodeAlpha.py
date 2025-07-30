import random
# Step 1: Welcome Message and Rules
print("Welcome to the Hangman Game!\n")
print("Rules:")
print("1. You have to guess the hidden word one letter at a time.")
print("2. You can make only 6 wrong guesses.")
print("3. The word is randomly chosen from a list of 5 fruits.")
print("4. If you guess all letters correctly, you win.")
print("5. If your 6 guesses are wrong, the game is over.")
print("\nLet's start the game!\n")
# Step 2: Word list
words = ['apple', 'banana', 'mango', 'grape', 'orange']
word = random.choice(words)
# Step 3: Setup
display = ['_'] * len(word)
chances = 6
guessed = []
# Step 4: Game loop
while chances > 0 and '_' in display:
    print("Word:", ' '.join(display))
    guess = input("Guess a letter: ").lower()
    # Check: Is it a single alphabet letter?
    if not guess.isalpha() or len(guess) != 1:
        print("Invalid input. Please enter a single alphabet letter.\n")
        continue
    if guess in guessed:
        print("You already guessed that letter.\n")
        continue
    guessed.append(guess)
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                display[i] = guess
        print("Correct guess!\n")
    else:
        chances -= 1
        print("Wrong guess. Chances left:", chances, "\n")
# Step 5: End result
print("Final word:", ' '.join(display))
if '_' not in display:
    print("Congratulations! You guessed the word:", word)
    print("Thanks for playing!")
else:
    print("Game Over! The word was:", word)
    print("Better luck next time. Try again!")