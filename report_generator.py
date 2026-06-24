import csv
import os
from pathlib import Path

class ReportGenerator:
    """
    Handles generating and appending data to CSV reports.
    """
    def __init__(self):
        self.reports_dir = Path("reports")
        self.reports_dir.mkdir(exist_ok=True)
        
        self.file_report_path = self.reports_dir / "file_report.csv"
        self.email_report_path = self.reports_dir / "email_report.csv"
        self.webpage_report_path = self.reports_dir / "webpage_report.csv"
        
        self._initialize_reports()

    def _initialize_reports(self):
        """Creates the report files with headers if they don't exist."""
        # Initialize File Report
        if not self.file_report_path.exists():
            with open(self.file_report_path, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["File Name", "File Type", "Destination Folder", "Date"])
                
        # Initialize Email Report
        if not self.email_report_path.exists():
            with open(self.email_report_path, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["Email Address", "Date"])
                
        # Initialize Webpage Report
        if not self.webpage_report_path.exists():
            with open(self.webpage_report_path, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(["URL", "Title", "Date"])

    def add_file_record(self, file_name: str, file_type: str, destination_folder: str, date: str):
        """Appends a record to the file organization report."""
        with open(self.file_report_path, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([file_name, file_type, destination_folder, date])

    def add_email_record(self, email_address: str, date: str):
        """Appends a record to the email extraction report."""
        with open(self.email_report_path, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([email_address, date])

    def add_webpage_record(self, url: str, title: str, date: str):
        """Appends a record to the webpage scraping report."""
        with open(self.webpage_report_path, mode='a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([url, title, date])

# Expose a single instance
report_generator = ReportGenerator()
