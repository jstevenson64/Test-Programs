import tkinter as tk  # Import the tkinter library

def on_button_click():
    """
    Event handler function that updates the label text
    when the button is clicked.
    """
    label.config(text="Button clicked!")  # Change the label text to "Button clicked!"

# Create the main application window
root = tk.Tk()

# Set the title of the main window
root.title("Simple Tkinter App")

# Create a label widget with initial text "Hello, Tkinter!"
label = tk.Label(root, text="Hello, Tkinter!")
# Add the label widget to the window
label.pack()

# Create a button widget with the text "Click Me"
# and assign the on_button_click function to be called when the button is clicked
button = tk.Button(root, text="Click Me", command=on_button_click)
# Add the button widget to the window
button.pack()

# Start the Tkinter event loop, which waits for user interactions
root.mainloop()