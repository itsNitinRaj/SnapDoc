### MONITORING SCREENSHOTS || APPLYING OCR || SAVING IT IN DATABASE ###

import os
from tkinter import Tk, Label, Entry, Button, Text, Scrollbar, VERTICAL, END, Frame
from tkinter.messagebox import showerror
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database configuration
DB_PATH = os.path.expanduser("ss_doc.db")
engine = create_engine(f"sqlite:///{DB_PATH}")
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()


# Define the Screenshot model
class Screenshot(Base):
    __tablename__ = "screenshots"
    id = Column(Integer, primary_key=True, autoincrement=True)
    file_name = Column(String, nullable=False)
    text = Column(String, nullable=True)
    timestamp = Column(DateTime)

    def __repr__(self):
        return f"<Screenshot(id={self.id}, file_name='{self.file_name}', timestamp='{self.timestamp}')>"


def search_database(query):
    """Search for screenshots containing the query string."""
    try:
        results = session.query(Screenshot).filter(Screenshot.text.like(f"%{query}%")).all()
        return results
    except Exception as e:
        showerror("Database Error", f"An error occurred: {e}")
        return []


def display_results(results):
    """Display search results in the GUI."""
    result_area.delete("1.0", END)  # Clear previous results

    if not results:
        result_area.insert(END, "No matches found.\n")
        return

    for result in results:
        result_area.insert(END, f"File Name: {result.file_name}\n")
        result_area.insert(END, f"Timestamp: {result.timestamp}\n")
        result_area.insert(END, f"Text Snippet: {result.text[:100]}...\n")
        result_area.insert(END, "-" * 50 + "\n")


def handle_search():
    """Handle the search button click."""
    query = search_entry.get().strip()
    if not query:
        showerror("Input Error", "Please enter a search query.")
        return

    results = search_database(query)
    display_results(results)


# GUI Setup
app = Tk()
app.title("Screenshot Search")
app.geometry("600x400")

# Search Label and Entry
search_label = Label(app, text="Search:")
search_label.pack(pady=5)

search_entry = Entry(app, width=50)
search_entry.pack(pady=5)

# Search Button
search_button = Button(app, text="Search", command=handle_search)
search_button.pack(pady=5)

# Results Area
frame = Frame(app)
frame.pack(fill="both", expand=True)

scrollbar = Scrollbar(frame, orient=VERTICAL)
scrollbar.pack(side="right", fill="y")

result_area = Text(frame, wrap="word", yscrollcommand=scrollbar.set, height=15)
result_area.pack(fill="both", expand=True)

scrollbar.config(command=result_area.yview)

# Run the GUI
app.mainloop()
