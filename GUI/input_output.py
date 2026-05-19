# Input and Output using tkinter
import tkinter as tk
def create_io_window():
    # Create the main window
    root = tk.Tk()
    root.title("Input and Output Window")
    root.geometry("400x300")

    # Add a label and entry for input
    input_label = tk.Label(root, text="Enter something:")
    input_label.pack(pady=5)
    input_entry = tk.Entry(root)
    input_entry.pack(pady=5)

    # Add a label to display output
    output_label = tk.Label(root, text="Output will be shown here")
    output_label.pack(pady=20)

    # Function to update output label
    def update_output():
        user_input = input_entry.get()
        output_label.config(text=f"You entered: {user_input}")

    # Add a button to submit input
    submit_button = tk.Button(root, text="Submit", command=update_output)
    submit_button.pack(pady=10)

    # Start the GUI event loop
    root.mainloop()
if __name__ == "__main__":
    create_io_window()