import tkinter as tk
from tkinter import messagebox
import random

class WordMasterGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Word Master")
        self.root.geometry("500x400")

        self.words_list = ["PYTHON", "DATA", "FILES", "SEARCH", "LOGIC", "LIST"]
        self.target_word = random.choice(self.words_list)
        self.guessed_letters = []
        self.attempts_left = 6

        self.setup_ui()

    def setup_ui(self):
        self.title_label = tk.Label(self.root, text="Word Master", font=("Arial", 24, "bold"))
        self.title_label.pack(pady=20)

        self.display_label = tk.Label(self.root, text=self.get_display_text(), font=("Courier", 30))
        self.display_label.pack(pady=20)

        self.input_entry = tk.Entry(self.root, font=("Arial", 18), width=5, justify="center")
        self.input_entry.pack(pady=10)

        self.btn = tk.Button(self.root, text="Guess", command=self.process_guess, width=10)
        self.btn.pack(pady=10)

        self.status_label = tk.Label(self.root, text=f"Attempts: {self.attempts_left}", fg="blue")
        self.status_label.pack(pady=10)

    def get_display_text(self):
        return " ".join([char if char in self.guessed_letters else "_" for char in self.target_word])

    def process_guess(self):
        char = self.input_entry.get().upper()
        self.input_entry.delete(0, tk.END)

        if char and char not in self.guessed_letters:
            self.guessed_letters.append(char)
            if char not in self.target_word:
                self.attempts_left -= 1
            
            self.update_game()

    def update_game(self):
        self.display_label.config(text=self.get_display_text())
        self.status_label.config(text=f"Attempts: {self.attempts_left}")

        if "_" not in self.get_display_text():
            messagebox.showinfo("Result", "You Won!")
            self.root.destroy()
        elif self.attempts_left <= 0:
            messagebox.showwarning("Result", f"Game Over! Word was: {self.target_word}")
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = WordMasterGame(root)
    root.mainloop()
