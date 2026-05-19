# Rock,Paper, Siccors Game using tkinter
import tkinter as tk
import random
def create_rps_game():
    # Create the main window
    root = tk.Tk()
    root.title("Rock, Paper, Scissors Game")
    root.geometry("400x300")

    # Add a label for instructions
    instruction_label = tk.Label(root, text="Choose Rock, Paper, or Scissors:")
    instruction_label.pack(pady=10)

    # Add buttons for Rock, Paper, and Scissors
    choices = ["Rock", "Paper", "Scissors"]
    user_choice = tk.StringVar()

    def play_game():
        user = user_choice.get()
        computer = random.choice(choices)
        if user == computer:
            result = "It's a tie!"
        elif (user == "Rock" and computer == "Scissors") or \
             (user == "Paper" and computer == "Rock") or \
             (user == "Scissors" and computer == "Paper"):
            result = "You win!"
        else:
            result = "Computer wins!"
        result_label.config(text=f"Computer chose: {computer}\n{result}")
    for choice in choices:
        rb = tk.Radiobutton(root, text=choice, variable=user_choice, value=choice)
        rb.pack(anchor='w')
    # Add a button to play the game
    play_button = tk.Button(root, text="Play", command=play_game)
    play_button.pack(pady=10)
    # Add a label to display the result
    result_label = tk.Label(root, text="")
    result_label.pack(pady=20)
    # Start the GUI event loop
    root.mainloop()
if __name__ == "__main__":
    create_rps_game()