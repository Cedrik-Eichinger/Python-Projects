import customtkinter as ctk
import random as r 
import zufallsworte as zufall

hangman_states = [
    """
       -----
           |
           |
           |
           |
           |
    --------
    """,
    """
       -----
       |   |
           |
           |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
           |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
       |   |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|   |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\  |
           |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      /    |
           |
    --------
    """,
    """
       -----
       |   |
       O   |
      /|\  |
      / \  |
           |
    --------
    """,
    """
       -----
       |   |
      [O   |
      /|\  |
      / \  |
           |
    --------
    """,
    """
       -----
       |   |
      [O]  |
      /|\  |
      / \  |
           |
    --------
    """,
]

fallback_words = ["lol"]

chosen_word = zufall.zufallswoerter(1)

if isinstance(chosen_word, list) and len(chosen_word) > 0:
    chosen_word = chosen_word[0]
else:
    chosen_word = r.choice(fallback_words)
chosen_word = str(chosen_word).lower()

guessed_letters = []
attempts_left = 9

ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.geometry("800x600")
app.title("Hangman Spiel")

def reset_game():
    global chosen_word, guessed_letters, attempts_left
    chosen_word = zufall.zufallswoerter(1)
    if isinstance(chosen_word, list) and len(chosen_word) > 0:
        chosen_word = chosen_word[0]
    else:
        chosen_word = r.choice(fallback_words)
    chosen_word = str(chosen_word).lower()
    guessed_letters = []
    attempts_left = 9
    update_display()
    message_label.configure(text="")
    guess_button.configure(state="normal")
    entry.configure(state="normal")
    play_again_button.pack_forget()

def update_display():
    display_word = " ".join(letter if letter in guessed_letters else "_" for letter in chosen_word)
    word_label.configure(text=display_word)
    attempts_label.configure(text=f"Versuche übrig {attempts_left}")
    hangman_index = min(9 -attempts_left, 9)
    hangman_label.configure(text=hangman_states[hangman_index])

def guess_letter(event=None):
    global attempts_left
    letter = entry.get().lower()
    entry.delete(0, ctk.END)

    if attempts_left <= 0:
        return

    if letter in guessed_letters:
        message_label.configure(text="Buchstabe bereits geraten!")
    elif letter in chosen_word:
        guessed_letters.append(letter)
        message_label.configure(text="Richtig geraten!")
    else:
        guessed_letters.append(letter)
        attempts_left -= 1
        message_label.configure(text="Falsch geraten!")

    update_display()

    if "_" not in word_label.cget("text"):
        message_label.configure(text="Gewonnen!")
        guess_button.configure(state="disabled")
        entry.configure(state="disabled")
        play_again_button.pack(pady=10)
    elif attempts_left <= 0:
        message_label.configure(text=f"Verloren! Das Wort war: {chosen_word}")
        guess_button.configure(state="disabled")
        entry.configure(state="disabled")
        play_again_button.pack(pady=10)

header_frame = ctk.CTkFrame(app)
header_frame.pack(fill="x", pady=10)
header_label = ctk.CTkLabel(header_frame, text="Hangman Spiel", font=("Arial", 24))
header_label.pack(pady=10)

word_label = ctk.CTkLabel(app, text="", font=("Arial", 24))
word_label.pack(pady=20)

entry = ctk.CTkEntry(app, width=200, placeholder_text="Buchstabeneingabe...")
entry.pack(pady=10)

guess_button = ctk.CTkButton(app, text="Raten", command=guess_letter)
guess_button.pack(pady=10)

attempts_label = ctk.CTkLabel(app, text=f"Versuche übrig {attempts_left}", font=("Arial", 18))
attempts_label.pack(pady=10)

message_label = ctk.CTkLabel(app, text="", font=("Arial", 18))
message_label.pack(pady=10)

play_again_button = ctk.CTkButton(app, fg_color="green", text="Nochmal spielen", command=reset_game)

hangman_label = ctk.CTkLabel(app, text="", font=("Courier", 14))
hangman_label.pack(pady=10)

entry.bind("<Return>", guess_letter)


if __name__ == "__main__":
    update_display()
    app.mainloop()

