''' AUTHORS
TEAM HANGMAN
R3YZE1 - RISHI - https://github.com/R3YZE1
'''
import random

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def reveal_letters(word, difficulty, custom_revealed=None):
    if difficulty == "easy":
        num_to_reveal = max(1, int(len(word) * random.uniform(0.25, 0.5)))
    elif difficulty == "hard":
        num_to_reveal = max(1, int(len(word) * 0.25))
    elif difficulty == "custom":
        return custom_revealed
    else:
        return set()

    revealed = set(random.sample(word, num_to_reveal))
    return revealed

def display_hangman(attempts):
    stages = [
        """
           +---+
               |
               |
               |
              ===
        """,
        """
           +---+
           O   |
               |
               |
              ===
        """,
        """
           +---+
           O   |
           |   |
               |
              ===
        """,
        """
           +---+
           O   |
          /|   |
               |
              ===
        """,
        """
           +---+
           O   |
          /|\  |
               |
              ===
        """,
        """
           +---+
           O   |
          /|\  |
          /    |
              ===
        """,
        """
           +---+
           O   |
          /|\  |
          / \  |
              ===
        """ 
    ]
    return stages[6 - attempts]
# ''' PS, the last stage is literally me after my teammates help me with nothing in the code.''' 
def hangman():
    print("Welcome to Two-Player Hangman!")

    while True:
        print("\nMain Menu:")
        print("1. Start Game")
        print("2. Quit")
        choice = input("Choose an option: ").strip()

        if choice == "2":
            print("Thanks for playing!")
            break
        elif choice != "1":
            print("Invalid option. Try again.")
            continue

        # FRONTMAN inputs the word and topic
        word = input("\nFRONTMAN, enter the word: ").lower().strip()
        topic = input("Enter the hint: ").strip()
        
        if not word.isalpha():
            print("Word must contain only letters. Restarting...")
            continue

        # FRONTMAN selects difficulty
        print("\nChoose Difficulty:")
        print("1. Easy")
        print("2. Hard")
        print("3. Custom")
        difficulty_choice = input("Enter difficulty (1-3): ").strip()

        if difficulty_choice == "1":
            difficulty = "easy"
        elif difficulty_choice == "2":
            difficulty = "hard"
        elif difficulty_choice == "3":
            difficulty = "custom"
            custom_revealed = set(input("FRONTMAN, enter the letters to reveal (e.g., 'ae'): ").lower())
        else:
            print("Invalid difficulty choice. Restarting...")
            continue

        revealed_letters = reveal_letters(word, difficulty, custom_revealed if difficulty == "custom" else None)

        guessed_letters = set(revealed_letters)
        attempts = 6

        print("\nPLAYER, try to guess the word!")
        print(f"Hint: {topic}")
        print(f"Revealed letters: {', '.join(sorted(revealed_letters))}")

        while attempts > 0:
            print(display_hangman(attempts))
            print("\n" + display_word(word, guessed_letters))
            print(f"Attempts remaining: {attempts}")
            print(f"Guessed letters: {', '.join(sorted(guessed_letters))}")

            guess = input("Enter a letter: ").lower()

            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single valid letter.")
                continue

            if guess in guessed_letters:
                print("You already guessed that letter.")
                continue

            guessed_letters.add(guess)

            if guess in word:
                print("Good guess!")
                if set(word).issubset(guessed_letters):
                    print(f"\nYOU WIN! The word was: {word}")
                    break
            else:
                print("Wrong guess!")
                attempts -= 1

        if attempts == 0:
            print(display_hangman(attempts))
            print(f"\nYOU GUESSED IT WRONG, AND YOU DIE. The word was: {word}")

if __name__ == "__main__":
    hangman()
