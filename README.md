# 🗂️ sortiere_desktop

A small Python script that automatically tidies up your desktop by sorting files into categorized subfolders based on their file types.

## 🚀 Features

- Automatically detects your desktop folder (local or OneDrive).
- Supports a wide range of common file types (PDFs, images, programs, music, videos, etc.).
- Smart detection of `.lnk` files (distinguishing between shortcuts and web links).
- No external dependencies required.

## 📁 Supported File Types

| Category        | Extensions |
|-----------------|------------|
| PDF             | `.pdf` |
| Programs        | `.exe`, `.msi`, `.bat` |
| Images          | `.jpg`, `.jpeg`, `.png`, `.gif`, `.bmp`, `.tiff` |
| Documents       | `.doc`, `.docx`, `.txt`, `.odt`, `.rtf` |
| Spreadsheets    | `.xls`, `.xlsx`, `.ods`, `.csv` |
| Presentations   | `.ppt`, `.pptx`, `.odp` |
| Archives        | `.zip`, `.rar`, `.7z`, `.tar`, `.gz` |
| Videos          | `.mp4`, `.avi`, `.mkv`, `.mov` |
| Music           | `.mp3`, `.wav`, `.flac` |
| Code            | `.py`, `.js`, `.html`, `.css`, `.cpp`, `.java` |
| Web Links       | `.url`, `.htm`, `.html`, `.webloc`, `.lnk`, `.webp` |

## 🛠️ Installation

1. Clone this repository or download the ZIP file.
2. Make sure Python 3 is installed.
3. Run the script using:

```bash
python sortiere_desktop.py


📝 License
This project is licensed under the MIT License. See the LICENSE file for details.

⚠️ Note
This script physically moves files into new folders — there is no preview or undo functionality. Use it with care.
