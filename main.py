import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog
import os
import pyperclip


global highlighted_text_string
highlighted_text_string = ""

def extract_highlighted_text(pdf_file):
    file_name = os.path.basename(pdf_file)
    selected_file_label.config(text=f"Selected PDF: {file_name}")
    # Open the provided PDF file
    doc = fitz.open(pdf_file)   
    highlighted_text = []
    
    # Iterate through each page in the document
    for page_num in range(len(doc)):
        page = doc.load_page(page_num)
        
        # Get a list of all annotations on the page
        annotations = page.annots()
        
        for annot in annotations:
            # Check if annotation is a highlight
            if annot.type[0] == 8:  # 8 corresponds to highlight type in fitz
                # Extract the highlighted text
                highlight = page.get_text("text", clip=annot.rect)
                highlighted_text.append(highlight.strip())    
    doc.close()
    text_entry.insert(tk.END, highlighted_text)
    return highlighted_text

def open_pdf_file():
    global file_path
    file_path = filedialog.askopenfilename(filetypes= [("PDF files" , "*.pdf")])
    global highlighted_text
    global highlighted_text_string
    highlighted_text_string = ""
    highlighted_text = extract_highlighted_text(file_path)
    for idx, text in enumerate(highlighted_text, start=1):
        highlighted_text_string = highlighted_text_string + (f"{text}               ")

def copy_text():
    pyperclip.copy(highlighted_text_string)

if __name__ == "__main__": 
    root = tk.Tk()
    root.title("Extract Higlighted Text")
    open_button = tk.Button(root , text="Open PDF" , command=open_pdf_file)
    open_button.pack(pady = 20)
    selected_file_label = tk.Label(root, text="Selected PDF : ")
    selected_file_label.pack()
    text_entry = tk.Text(root, wrap=tk.WORD, height=10, width=40)
    text_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=text_entry.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    text_entry.config(yscrollcommand=scrollbar.set)
    text_entry.config(state=tk.NORMAL)
    copy_button = tk.Button(root,text="Copy Selected Text", command=copy_text)
    copy_button.pack(pady=8)
    root.mainloop()