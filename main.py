import fitz  # PyMuPDF
import tkinter as tk
from tkinter import filedialog
import os
import pyperclip

class PDFHighlightExtractor:
    def __init__(self, root):
        self.root = root
        self.highlighted_text = []
        self.file_path = ""
        
        self.open_button = tk.Button(self.root, text="Open PDF", command=self.open_pdf_file)
        self.open_button.pack(pady=20)
        
        self.selected_file_label = tk.Label(self.root, text="Selected PDF: ")
        self.selected_file_label.pack()
        
        self.page_range_label = tk.Label(self.root, text="Page Range (e.g., 1-5): ")
        self.page_range_label.pack()
        
        self.page_range_entry = tk.Entry(self.root)
        self.page_range_entry.pack()
        
        self.text_entry = tk.Text(self.root, wrap=tk.WORD, height=10, width=60)
        self.text_entry.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        
        self.scrollbar = tk.Scrollbar(self.root, orient=tk.VERTICAL, command=self.text_entry.yview)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.text_entry.config(yscrollcommand=self.scrollbar.set)
        
        self.copy_button = tk.Button(self.root, text="Copy Selected Text", command=self.copy_text)
        self.copy_button.pack(pady=8)
        
        self.save_button = tk.Button(self.root, text="Save As", command=self.save_text)
        self.save_button.pack(pady=8)
    
    def open_pdf_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        self.extract_highlighted_text(self.file_path)
        
    def extract_highlighted_text(self, pdf_file):
        file_name = os.path.basename(pdf_file)
        self.selected_file_label.config(text=f"Selected PDF: {file_name}")
        
        # Get the specified page range from entry
        page_range = self.page_range_entry.get().strip()
        
        if '-' in page_range:
            start_page, end_page = page_range.split('-')
            start_page = int(start_page.strip())
            end_page = int(end_page.strip())
        else:
            start_page = 1
            end_page = None
        
        # Open the provided PDF file
        doc = fitz.open(pdf_file)
        self.highlighted_text = []
        
        # Iterate through each page in the document
        for page_num in range(len(doc)):
            if end_page and page_num + 1 > end_page:
                break
            if page_num + 1 >= start_page:
                page = doc.load_page(page_num)
                
                # Get a list of all annotations on the page
                annotations = page.annots()
                
                for annot in annotations:
                    # Check if annotation is a highlight
                    if annot.type[0] == 8:  # 8 corresponds to highlight type in fitz
                        # Extract the highlighted text
                        highlight = page.get_text("text", clip=annot.rect)
                        self.highlighted_text.append(highlight.strip())
        
        doc.close()
        
        # Clear previous text in text_entry
        self.text_entry.delete(1.0, tk.END)
        
        # Insert each highlighted text into the text widget
        for text in self.highlighted_text:
            self.text_entry.insert(tk.END, text + "\n\n")
    
    def save_text(self):
        if not self.highlighted_text:
            return
        
        saving_filename = filedialog.asksaveasfilename(filetypes=[("Text files", "*.txt"), ("Markdown Files", "*.md")])
        if saving_filename:
            with open(saving_filename, 'w') as file:
                file.write("\n\n".join(self.highlighted_text))
    
    def copy_text(self):
        if self.highlighted_text:
            pyperclip.copy("\n\n".join(self.highlighted_text))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Extract Highlighted Text")
    app = PDFHighlightExtractor(root)
    root.mainloop()
