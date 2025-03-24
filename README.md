# SnapDoc

_Automatically capture, store, and search your screenshots like a native OS feature._

## Overview
SnapDoc is a lightweight tool that runs in the background, automatically detecting new screenshots, applying OCR, and storing them in a local database. It provides an easy way to search your past screenshots using keywords.

## Features
✅ Monitors the screenshot folder for new images  
✅ Extracts text from screenshots using OCR (Tesseract)  
✅ Stores image paths and extracted text in a local SQLite database  
✅ Provides a simple GUI for searching past screenshots  
✅ Runs smoothly in the background as a native OS feature  

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/itsNitinRaj/SnapDoc.git
cd SnapDoc
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Install Tesseract OCR (Required for Text Extraction)
- **Windows:** [Download here]([https://github.com/UB-Mannheim/tesseract/wiki](https://tesseract-ocr.github.io/tessdoc/Downloads))  
- **Linux (Ubuntu/Debian):**  
  ```bash
  sudo apt install tesseract-ocr
  ```
- **Mac (Homebrew):**  
  ```bash
  brew install tesseract
  ```

## Usage

### Starting SnapDoc (Monitoring Screenshots)
- **Windows:** Double-click `start.bat` to launch SnapDoc in the background.
- **Linux/Mac:** Run:  
  ```bash
  python main.py
  ```

### Searching Past Screenshots
- **Windows:** Double-click `search.bat` to open the search tool.
- **Linux/Mac:** Run:  
  ```bash
  python search.py
  ```

### How It Works
1. Take a screenshot using `PrtScn` (Windows) or `Cmd + Shift + 4` (Mac).
2. SnapDoc automatically detects it, extracts text, and saves it.
3. Use `search.bat` (or `search.py`) to find past screenshots using keywords.

## File Structure
```
SnapDoc/
│── main.py           # Background script to monitor screenshots
│── search.py         # GUI to search stored screenshots
│── start.bat         # Windows batch script to start monitoring
│── search.bat        # Windows batch script to start search UI
│── requirements.txt  # Dependencies list
│── .gitignore        # Ignore unnecessary files
```

## Contributing
Want to improve SnapDoc? Feel free to fork the repo, open issues, and submit pull requests! 🚀

