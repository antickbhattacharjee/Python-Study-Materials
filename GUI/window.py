# How to create a window in a GUI application using Tkinter
import tkinter as tk
def create_window():
    # Create the main window
    root = tk.Tk()
    root.title("My GUI Window")
    root.geometry("400x300")

    # Add a label to the window
    label = tk.Label(root, text="Hello, Tkinter!")
    label.pack(pady=20)

    # Start the GUI event loop
    root.mainloop()
if __name__ == "__main__":
    create_window()