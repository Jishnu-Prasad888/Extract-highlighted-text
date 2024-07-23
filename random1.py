import tkinter as tk
import pyperclip


def copy_text():
    selected_text = text_entry.selection_get()
    pyperclip.copy(selected_text)

# Create main Tkinter window
root = tk.Tk()
root.title("Scrollable Text Box Example")

# Create a Text widget
text_entry = tk.Text(root, wrap=tk.WORD, height=10, width=40)
text_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Create a Scrollbar widget
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=text_entry.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure Text widget to use Scrollbar
text_entry.config(yscrollcommand=scrollbar.set)

# Sample large paragraph
large_paragraph = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla nec odio in tortor vestibulum auctor. 
Nulla facilisi. Etiam pretium metus sit amet ipsum dictum, id vehicula purus fringilla. 
Maecenas maximus, mi nec ultricies ultricies, tortor nisi convallis justo, eu mattis ligula justo nec nisi. 
Sed laoreet dolor quis odio lobortis, eget consectetur urna volutpat. 
"""

# Insert the large paragraph into the Text widget
text_entry.insert(tk.END, large_paragraph)

# Allow text selection and copying
text_entry.config(state=tk.NORMAL)

# Create a button to copy selected text
copy_button = tk.Button(root, text="Copy Selected Text", command=copy_text)
copy_button.pack(pady=5)

# Start the Tkinter main loop
root.mainloop()
