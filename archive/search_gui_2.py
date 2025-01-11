import os
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QLineEdit, QPushButton,
    QTableWidget, QTableWidgetItem, QHeaderView, QAbstractItemView, QWidget
)
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime


# Database Configuration
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


# Modern GUI with PyQt5
class ScreenshotSearchApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Modern Screenshot Search")
        self.setGeometry(100, 100, 800, 600)

        # Main Layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Search Bar
        self.search_bar = QLineEdit(self)
        self.search_bar.setPlaceholderText("Search screenshots...")
        self.search_bar.setFont(QFont("Arial", 12))
        layout.addWidget(self.search_bar)

        # Search Button
        self.search_button = QPushButton("Search", self)
        self.search_button.setFont(QFont("Arial", 12))
        self.search_button.clicked.connect(self.perform_search)
        layout.addWidget(self.search_button)

        # Results Table
        self.results_table = QTableWidget(self)
        self.results_table.setColumnCount(3)
        self.results_table.setHorizontalHeaderLabels(["File Name", "Text Snippet", "Timestamp"])
        self.results_table.horizontalHeader().setStretchLastSection(True)
        self.results_table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.results_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.results_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        layout.addWidget(self.results_table)

    def perform_search(self):
        """Search the database and display results."""
        query = self.search_bar.text().strip()
        if not query:
            return

        # Query the database
        results = session.query(Screenshot).filter(Screenshot.text.like(f"%{query}%")).all()

        # Populate the table
        self.results_table.setRowCount(len(results))
        for row_idx, result in enumerate(results):
            self.results_table.setItem(row_idx, 0, QTableWidgetItem(result.file_name))
            snippet = result.text[:50] + "..." if result.text and len(result.text) > 50 else result.text
            self.results_table.setItem(row_idx, 1, QTableWidgetItem(snippet))
            self.results_table.setItem(row_idx, 2, QTableWidgetItem(str(result.timestamp)))


# Main Function
def main():
    app = QApplication([])
    window = ScreenshotSearchApp()
    window.show()
    app.exec_()


if __name__ == "__main__":
    Base.metadata.create_all(engine)  # Ensure the database schema exists
    main()
