''' AUTHORS:
RISHI - R3YZE1  
RAV - RAV0110 ''' 

import customtkinter as ctk
import random
from tkinter import messagebox

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

def start_game():
    def submit_word():
        nonlocal word, topic, difficulty

        word = word_entry.get().lower().strip()
        topic = topic_entry.get().strip()

        if not word.isalpha():
            messagebox.showerror("Error", "Word must contain only letters.")
            return

        difficulty = difficulty_var.get()
        if difficulty == "custom":
            custom_letters = custom_reveal_entry.get().lower().strip()
            revealed_letters.update(set(custom_letters))

        revealed_letters.update(reveal_letters(word, difficulty))
        guessed_letters.update(revealed_letters)

        word_frame.pack_forget()
        game_frame.pack()
        update_game_display()

    def update_game_display():
        word_display.configure(text=display_word(word, guessed_letters))
        hint_label.configure(text=f"Hint: {topic}")
        guessed_label.configure(text=f"Guessed letters: {', '.join(sorted(guessed_letters))}")
        attempts_label.configure(text=f"Attempts remaining: {attempts}")

    def guess_letter():
        nonlocal attempts
        guess = guess_entry.get().lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showerror("Error", "Please enter a single valid letter.")
            return

        if guess in guessed_letters:
            messagebox.showinfo("Info", "You already guessed that letter.")
            return

        guessed_letters.add(guess)
        if guess in word:
            if set(word).issubset(guessed_letters):
                messagebox.showinfo("You Win!", f"Congratulations! The word was: {word}")
                game_frame.pack_forget()
                main_menu.pack()
        else:
            nonlocal attempts
            attempts -= 1
            if attempts == 0:
                messagebox.showinfo("Game Over", f"You lost! The word was: {word}")
                game_frame.pack_forget()
                main_menu.pack()

        update_game_display()
        guess_entry.delete(0, ctk.END)

    word = ""
    topic = ""
    difficulty = "easy"
    revealed_letters = set()
    guessed_letters = set()
    attempts = 6

    main_menu.pack_forget()

    word_frame = ctk.CTkFrame(root)
    word_frame.pack()

    ctk.CTkLabel(word_frame, text="Enter the word:").pack()
    word_entry = ctk.CTkEntry(word_frame)
    word_entry.pack()

    ctk.CTkLabel(word_frame, text="Enter the topic:").pack()
    topic_entry = ctk.CTkEntry(word_frame)
    topic_entry.pack()

    difficulty_var = ctk.StringVar(value="easy")

    ctk.CTkLabel(word_frame, text="Select difficulty:").pack()
    ctk.CTkRadioButton(word_frame, text="Easy", variable=difficulty_var, value="easy").pack()
    ctk.CTkRadioButton(word_frame, text="Hard", variable=difficulty_var, value="hard").pack()
    ctk.CTkRadioButton(word_frame, text="Custom", variable=difficulty_var, value="custom").pack()

    ctk.CTkLabel(word_frame, text="Custom letters to reveal (if custom selected):").pack()
    custom_reveal_entry = ctk.CTkEntry(word_frame)
    custom_reveal_entry.pack()

    ctk.CTkButton(word_frame, text="Start Game", command=submit_word).pack()

    game_frame = ctk.CTkFrame(root)

    word_display = ctk.CTkLabel(game_frame, font=("Courier", 24))
    word_display.pack()

    hint_label = ctk.CTkLabel(game_frame, text="Hint:")
    hint_label.pack()

    guessed_label = ctk.CTkLabel(game_frame, text="Guessed letters:")
    guessed_label.pack()

    attempts_label = ctk.CTkLabel(game_frame, text="Attempts remaining:")
    attempts_label.pack()

    guess_entry = ctk.CTkEntry(game_frame)
    guess_entry.pack()

    ctk.CTkButton(game_frame, text="Guess", command=guess_letter).pack()

def quit_game():
    root.destroy()

ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

root = ctk.CTk()
root.title("Hangman")

main_menu = ctk.CTkFrame(root)
main_menu.pack()

ctk.CTkLabel(main_menu, text="HANGMAN", font=("Courier", 32)).pack()

ctk.CTkButton(main_menu, text="Start Game", command=start_game).pack()

ctk.CTkButton(main_menu, text="Quit", command=quit_game).pack()

root.mainloop()
