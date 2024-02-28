# PyMuPDF PDF Image Extraction Tool

This Python script utilizes PyMuPDF to extract images from PDF files. It offers a simple interface with PySimpleGUI for selecting PDF files from which images will be extracted.

## Features

- **PDF Image Extraction**: Extracts images embedded in PDF documents.
- **Image Filtering**: Skips images below a certain dimension or file size, ensuring only relevant images are extracted.
- **User Interface**: Features a simple GUI for easy file selection and progress tracking.
- **Output Customization**: Saves extracted images according to their page nr. in a directory and optionally zips them for convenient handling.

- Usage
To use the tool, follow these steps:

Run the script from your terminal or command prompt:
python pdf_image_extractor.py

If no PDF file is specified as a command-line argument, a file selection dialog will appear. Choose the PDF file you wish to extract images from.
The script will create a folder in the same location as the PDF file to store the extracted images.
After extraction, it will also create a zip file containing all the images for easy download and sharing.

