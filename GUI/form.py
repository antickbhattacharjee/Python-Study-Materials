# Input forms for user data collection using tkinter
import tkinter as tk
def create_form():
    # Create the main window
    root = tk.Tk()
    root.title("User Input Form")
    root.geometry("400x300")

    # Add a label and entry for name
    name_label = tk.Label(root, text="Name:")
    name_label.pack(pady=5)
    name_entry = tk.Entry(root)
    name_entry.pack(pady=5)

    # Add a label and entry for email
    email_label = tk.Label(root, text="Email:")
    email_label.pack(pady=5)
    email_entry = tk.Entry(root)
    email_entry.pack(pady=5)

    # Add a submit button
    submit_button = tk.Button(root, text="Submit", command=lambda: print(f"Name: {name_entry.get()}, Email: {email_entry.get()}"))
    submit_button.pack(pady=20)

    # Start the GUI event loop
    root.mainloop()
if __name__ == "__main__":
    create_form()