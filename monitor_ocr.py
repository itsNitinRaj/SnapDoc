import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image
import pytesseract

# Path to monitor (update this to your screenshot folder)
SCREENSHOT_FOLDER = os.path.expanduser("~/Pictures/Screenshots")

# Path to the Tesseract executable (update if needed)
PYTESSERACT_CMD = r"C:\\Program Files\\Tesseract-OCR\\tesseract.exe"  # Windows
# Uncomment the following line for Linux/Mac if needed
# PYTESSERACT_CMD = "tesseract"

pytesseract.pytesseract.tesseract_cmd = PYTESSERACT_CMD


class ImageFileHandler(FileSystemEventHandler):
    """Custom event handler for monitoring image files."""

    def on_created(self, event):
        """Triggered when a new file is created in the monitored folder."""
        if not event.is_directory and event.src_path.endswith(('.png', '.jpg', '.jpeg')):
            file_name = os.path.basename(event.src_path)
            print(f"New image detected: {file_name}")
            process_image(event.src_path)


def process_image(file_path):
    """Perform OCR on the new image and display the extracted text."""
    try:
        # Open the image
        image = Image.open(file_path)

        # Perform OCR using Tesseract
        extracted_text = pytesseract.image_to_string(image)

        # Display the extracted text
        print(f"Extracted text from {os.path.basename(file_path)}:")
        print(extracted_text.strip() or "No text found in the image.")
        print("-" * 50)

    except Exception as e:
        print(f"Error processing image {file_path}: {e}")


def start_monitoring():
    """Set up folder monitoring using watchdog."""
    if not os.path.exists(SCREENSHOT_FOLDER):
        print(f"Screenshot folder not found: {SCREENSHOT_FOLDER}")
        return

    # Set up the observer and event handler
    event_handler = ImageFileHandler()
    observer = Observer()
    observer.schedule(event_handler, path=SCREENSHOT_FOLDER, recursive=False)

    # Start monitoring
    observer.start()
    print(f"Monitoring folder: {SCREENSHOT_FOLDER}")

    try:
        while True:
            pass  # Keep the script running
    except KeyboardInterrupt:
        print("Stopping monitoring...")
        observer.stop()

    observer.join()


if __name__ == "__main__":
    start_monitoring()
