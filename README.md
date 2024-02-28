# PyMuPDF PDF Image Extraction Tool

This Python script utilizes PyMuPDF to extract images from PDF files efficiently. It offers a user-friendly interface with PySimpleGUI for selecting PDF files from which images will be extracted. The script is designed to be straightforward, making it accessible for users with minimal technical background.

## Features

- **PDF Image Extraction**: Extracts images embedded in PDF documents.
- **Image Filtering**: Skips images below a certain dimension or file size, ensuring only relevant images are extracted.
- **User Interface**: Features a simple GUI for easy file selection and progress tracking.
- **Output Customization**: Saves extracted images according to their page nr. in a directory and optionally zips them for convenient handling.

## Prerequisites

Before running this script, ensure you have the following installed:

- Python 3.x
- PyMuPDF (v1.18.18 or later)
- PySimpleGUI

## Installation

1. Install the necessary Python packages if you haven't already:

```bash
pip install PyMuPDF PySimpleGUI
