import os
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

# Define the folder to monitor (update with your screenshot folder path)
SCREENSHOT_FOLDER = os.path.expanduser("C:\Users\Nitin\Pictures\Screenshots")

class ImageFileHandler(FileSystemEventHandler):
    """Custom event handler for monitoring image files."""
    
    def on_created(self, event):
        """Triggered when a new file is created in the monitored folder."""
        # Check if the new file is an image (based on extension)
        if not event.is_directory and event.src_path.endswith(('.png', '.jpg', '.jpeg')):
            file_name = os.path.basename(event.src_path)
            print(f"New image detected: {file_name}")

def start_monitoring():
    """Set up folder monitoring using watchdog."""
    # Ensure the screenshot folder exists
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
            pass  # Keep the script running to monitor the folder
    except KeyboardInterrupt:
        print("Stopping monitoring...")
        observer.stop()
    
    observer.join()

if __name__ == "__main__":
    start_monitoring()
