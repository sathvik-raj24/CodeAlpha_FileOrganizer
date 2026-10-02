# CodeAlpha File Organizer

## About

A Python-based File Organizer that automatically organizes files into different folders based on their file types. This project was developed as part of the CodeAlpha Python Programming Internship.

## Features

- Automatically organizes files by type
- Creates folders automatically
- Supports images, documents, videos, audio files, archives, and Python files
- Places unsupported file types into an Others folder
- Skips existing folders
- Uses file extensions to identify file categories

## File Categories

- Images
- Documents
- Videos
- Audio
- Archives
- Python
- Others

## Technologies Used

- Python
- OS module
- Shutil module

## Python Concepts Used

- Dictionaries
- Lists
- Loops
- Conditional statements
- File handling
- String operations
- Exception and path handling

## How It Works

1. The user provides the path of the folder to organize.
2. The program checks whether the folder exists.
3. It reads the files inside the folder.
4. The program identifies each file using its extension.
5. It creates the appropriate category folder if required.
6. It moves the file into the corresponding folder.
7. Unsupported file types are moved to the Others folder.

## How to Run

1. Make sure Python is installed.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

python file_organizer.py

5. Enter the full path of the folder you want to organize.

## Example

Before organizing:

Test_Files
- photo.jpg
- notes.txt
- song.mp3
- video.mp4
- code.py
- document.pdf

After organizing:

Test_Files
- Images
  - photo.jpg
- Documents
  - notes.txt
  - document.pdf
- Audio
  - song.mp3
- Videos
  - video.mp4
- Python
  - code.py

## Project Objective

The objective of this project is to automate file organization using Python by identifying file extensions and moving files into appropriate folders while practicing Python file handling, loops, dictionaries, conditional statements, and the os and shutil modules.

## Internship

This project was developed as part of the CodeAlpha Python Programming Internship.