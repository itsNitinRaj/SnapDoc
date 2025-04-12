import os
from datetime import datetime
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from PIL import Image
import pytesseract
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import time
import pytz
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Path to monitor
SCREENSHOT_FOLDER = os.getenv("SCREENSHOT_FOLDER")

# Path to the Tesseract executable from .env
TESSERACT_PATH = os.getenv("TESSERACT_PATH", "C:/Program Files/Tesseract-OCR/tesseract.exe")
pytesseract.pytesseract.tesseract_cmd = TESSERACT_PATH

# Database configuration from .env
DATABASE_NAME = os.getenv("DATABASE_NAME", "database.db")
engine = create_engine(f"sqlite:///{DATABASE_NAME}")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

# Define the IST timezone
IST = pytz.timezone('Asia/Kolkata')

# Define the Screenshot model
class Screenshot(Base):
    __tablename__ = "screenshots"
    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String, nullable=False)
    text = Column(String, nullable=True)
    timestamp = Column(DateTime, default=datetime.now(IST))

    def __repr__(self):
        return f"<Screenshot(id={self.id}, file_name='{self.file_name}', timestamp='{self.timestamp}')>"


def initialize_database():
    """Create database tables if they don't exist."""
    Base.metadata.create_all(engine)
    print(f"Database initialized at {DATABASE_NAME}")


class ImageFileHandler(FileSystemEventHandler):
    """Custom event handler for monitoring image files."""

    def on_created(self, event):
        """Triggered when a new file is created in the monitored folder."""
        if not event.is_directory and event.src_path.endswith(('.png', '.jpg', '.jpeg')):
            file_name = os.path.basename(event.src_path)
            print(f"New image detected: {file_name}")
            time.sleep(1)
            process_image(event.src_path)


def process_image(file_path):
    """Perform OCR on the new image and save data to the database."""
    try:
        # Open the image
        image = Image.open(file_path)

        # Perform OCR using Tesseract
        extracted_text = pytesseract.image_to_string(image)

        # Save data to the database
        save_to_database(os.path.basename(file_path), extracted_text)

    except Exception as e:
        print(f"Error processing image {file_path}: {e}")


def save_to_database(file_name, text):
    """Save the extracted data to the SQLite database."""
    try:
        new_screenshot = Screenshot(file_name=file_name, text=text)
        session.add(new_screenshot)
        session.commit()
        print(f"Saved to database: {file_name}")
    except Exception as e:
        session.rollback()
        print(f"Error saving to database: {e}")


def start_monitoring():
    """Set up folder monitoring using watchdog."""
    if not os.path.exists(SCREENSHOT_FOLDER):
        print(f"Screenshot folder not found: {SCREENSHOT_FOLDER}")
        return

    # Initialize the database
    initialize_database()

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
