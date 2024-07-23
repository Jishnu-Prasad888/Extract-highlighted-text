
---

# PDF Highlight Extractor

## Overview

The **PDF Highlight Extractor** is a graphical user interface (GUI) application built using tkinter in Python. It allows users to open a PDF file, extract highlighted text from specific pages, save the extracted text to a file, and copy it to the clipboard.

## Features

- **Open PDF**: Users can select a PDF file using a file dialog.
- **Extract Highlighted Text**: The application extracts highlighted text from the specified page range in the PDF file.
- **Save As**: Users can save the extracted text to a text file (.txt) or markdown file (.md) using a file dialog.
- **Copy Selected Text**: Copies the extracted text to the clipboard for easy sharing.

## GUI Components

### Buttons

- **Open PDF**: Opens a file dialog to select a PDF file for text extraction.
- **Copy Selected Text**: Copies the extracted text to the clipboard.
- **Save As**: Saves the extracted text to a file.

This documentation provides an overview of the PDF Highlight Extractor application, detailing its features, GUI components, classes, methods, and usage instructions. Adjustments can be made based on specific requirements or additional functionality.
### Labels and Entry

- **Selected PDF**: Displays the name of the currently selected PDF file.
- **Page Range (e.g., 1-5)**: Allows users to specify a page range from which text should be extracted.

### Text Widget

- Displays the extracted highlighted text from the PDF file. Supports scrolling for longer texts.

### Scrollbar

- Provides vertical scrolling functionality for the Text widget.

## Classes and Methods

### `PDFHighlightExtractor`

#### Methods

- **`__init__(self, root)`**: Initializes the GUI components and sets up event handlers.
- **`open_pdf_file(self)`**: Opens a file dialog to select a PDF file and calls `extract_highlighted_text`.
- **`extract_highlighted_text(self, pdf_file)`**: Extracts highlighted text from the specified page range in the PDF file using PyMuPDF (fitz).
- **`save_text(self)`**: Saves the extracted text to a file selected via a file dialog.
- **`copy_text(self)`**: Copies the extracted text to the clipboard.

## Usage

1. **Select PDF**: Click the "Open PDF" button and select a PDF file from your computer.
2. **Specify Page Range**: Enter the desired page range (e.g., "1-5") in the "Page Range" entry.
3. **Extract and Display**: The application will extract highlighted text from the specified pages and display it in the text area.
4. **Save or Copy Text**: Use the "Save As" button to save the extracted text to a file or the "Copy Selected Text" button to copy it to the clipboard.

---
