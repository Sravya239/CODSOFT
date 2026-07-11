import tkinter as tk
import random

choices = ["Rock", "Paper", "Scissors"]

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score

    computer_choice = random.choice(choices)

    if user_choice == computer_choice:
        result = "It's a Tie!"
    elif (
        (user_choice == "Rock" and computer_choice == "Scissors") or
        (user_choice == "Paper" and computer_choice == "Rock") or
        (user_choice == "Scissors" and computer_choice == "Paper")
    ):
        result = "You Win!"
        user_score += 1
    else:
        result = "Computer Wins!"
        computer_score += 1

    user_label.config(text=f"Your Choice: {user_choice}")
    computer_label.config(text=f"Computer Choice: {computer_choice}")
    result_label.config(text=result)
    score_label.config(
        text=f"Score\nYou: {user_score}    Computer: {computer_score}"
    )

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0

    user_label.config(text="Your Choice: ")
    computer_label.config(text="Computer Choice: ")
    result_label.config(text="")
    score_label.config(text="Score\nYou: 0    Computer: 0")

root = tk.Tk()
root.title("Rock Paper Scissors")
root.geometry("450x450")
root.resizable(False, False)

title = tk.Label(root, text="Rock Paper Scissors Game", font=("Arial", 18, "bold"))
title.pack(pady=15)

instruction = tk.Label(
    root,
    text="Choose Rock, Paper, or Scissors",
    font=("Arial", 12)
)
instruction.pack()

button_frame = tk.Frame(root)
button_frame.pack(pady=20)

rock_btn = tk.Button(
    button_frame,
    text="Rock",
    width=12,
    command=lambda: play("Rock")
)
rock_btn.grid(row=0, column=0, padx=5)

paper_btn = tk.Button(
    button_frame,
    text="Paper",
    width=12,
    command=lambda: play("Paper")
)
paper_btn.grid(row=0, column=1, padx=5)

scissors_btn = tk.Button(
    button_frame,
    text="Scissors",
    width=12,
    command=lambda: play("Scissors")
)
scissors_btn.grid(row=0, column=2, padx=5)

user_label = tk.Label(root, text="Your Choice: ", font=("Arial", 12))
user_label.pack(pady=5)

computer_label = tk.Label(root, text="Computer Choice: ", font=("Arial", 12))
computer_label.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 14, "bold"))
result_label.pack(pady=10)

score_label = tk.Label(root, text="Score\nYou: 0    Computer: 0", font=("Arial", 12))
score_label.pack(pady=10)

reset_btn = tk.Button(root, text="Reset Game", width=15, command=reset_game)
reset_btn.pack(pady=15)

root.mainloop()