from search import Screenshot, Base

import os
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Database configuration
DB_PATH = os.path.expanduser("ss_doc.db")
engine = create_engine(f"sqlite:///{DB_PATH}")
Base.metadata.create_all(engine)  # Ensure the tables are created
Session = sessionmaker(bind=engine)
db = Session()

# Debugging: Check if the database file exists
if not os.path.exists(DB_PATH):
    print(f"Database file does not exist: {DB_PATH}")
else:
    # Debugging: Print all records in the Screenshot table
    all_screenshots = db.query(Screenshot).all()
    print(f"All screenshots: {all_screenshots}")

    # Query for the record with id 3
    result = db.query(Screenshot).filter(Screenshot.id == 3).first()
    print(f"Result for id 3: {result}")