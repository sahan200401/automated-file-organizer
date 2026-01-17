File Organizer
A Python script that automatically organizes files in a folder by categorizing them into subfolders based on their file extensions.

Features
  Scans a specified folder for files
  Identifies file extensions
  Categorizes files into predefined categories (Images, Documents, Videos, Code, Other)
  Automatically creates category folders and moves files into them

How It Works
  Folder Selection: Prompts you to enter a folder path
  File Detection: Scans the folder and lists all files
  Extension Analysis: Identifies unique file extensions present
  Categorization: Maps extensions to categories:

Images: .jpg, .png, .jpeg
Documents: .pdf, .txt, .docx
Videos: .mp4, .mkv
Code: .py, .java, .js
Other: Any extension not in the above categories

Organization: Creates category folders and moves files accordingly

< ------------------------------------------------------------------------------------------------------------------------------------------------------------->


python file_organizer.py
```
```
enter the folder path.. /path/to/your/folder
```
```

< -- Before -- >

MyFolder/
├── photo.jpg
├── document.pdf
├── script.py
├── video.mp4
└── notes.txt
```
< -- After -- >
```
MyFolder/
├── Images/
│   └── photo.jpg
├── Documents/
│   ├── document.pdf
│   └── notes.txt
├── Code/
│   └── script.py
└── Videos/
    └── video.mp4
