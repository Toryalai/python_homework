def make_hangman(secret_word):
    guesses = []

    def hangman_closure(letter):
        guesses.append(letter)

        output = ""
        for c in secret_word:
            if c in guesses:
                output += c
            else:
                output += "_"

        print(output)

        for c in secret_word:
            if c not in guesses:
                return False

        return True

    return hangman_closure


secret = input("Enter secret word: ")
game = make_hangman(secret)

done = False
while not done:
    guess = input("Guess a letter: ")
    done = game(guess)

print("You won!")
