import os
from datetime import datetime
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
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Screenshot(id={self.id}, file_name='{self.file_name}', timestamp='{self.timestamp}')>"


def initialize_database():
    """Ensure the database and tables exist."""
    Base.metadata.create_all(engine)


def search_database(query):
    """Search for screenshots containing the query string."""
    try:
        print(query)
        results = session.query(Screenshot).filter(Screenshot.text.like(f"%{query}%")).all()
        print(results)
        return results
    except Exception as e:
        print(f"Error during search: {e}")
        return []


def display_search_results(results):
    """Display search results in the terminal."""
    if not results:
        print("\nNo matches found.")
        return

    print("\nSearch Results:")
    print("=" * 50)
    for result in results:
        print(f"File Name: {result.file_name}")
        print(f"Text Snippet: {result.text[:100]}")  # Display the first 100 characters
        print(f"Timestamp: {result.timestamp}")
        print("-" * 50)


def start_search_interface():
    """Start the search CLI."""
    print("Welcome to Screenshot Search!")
    while True:
        query = input("\nEnter search text (or type 'exit' to quit): ").strip()
        if query.lower() == "exit":
            print("Exiting search interface.")
            break

        results = search_database(query)
        display_search_results(results)


if __name__ == "__main__":
    # Initialize the database
    initialize_database()

    # Start the search interface
    start_search_interface()
