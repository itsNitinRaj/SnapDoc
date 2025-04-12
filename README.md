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

### 4. Configuration
Copy the example environment file and configure it for your system:
```bash
cp .env.example .env
```
Edit the `.env` file to set your Tesseract path and other settings.

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
│── .env.example      # Example environment variables
```

## Future Scope

### Planned Enhancements
🔮 **System Tray App**: Native system tray application for easy access and configuration  
🔮 **Web Interface**: Develop a web-based dashboard for more intuitive searching and viewing  
🔮 **AI-Powered Search**: Implement semantic search capabilities to find screenshots by concept, not just exact text  
🔮 **Image Classification**: Auto-categorize screenshots (code, websites, documents) for better organization  
🔮 **Cloud Sync**: Optional cloud backup and sync across multiple devices  
🔮 **Advanced OCR Options**: Support for multiple languages and handwriting recognition  
🔮 **Hotkey Support**: Custom hotkeys for quick screenshot capture and search  

### Roadmap
1. **Short-term**: Adding native system tray application for easy access and configuration
2. **Mid-term**: Improve OCR accuracy and search performance
3. **Long-term**: Develop cross-platform GUI and mobile companion app

## Contributing
Want to improve SnapDoc? Feel free to fork the repo, open issues, and submit pull requests! 🚀

