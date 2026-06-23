import re
from pathlib import Path
from datetime import datetime
from .logger_setup import logger
from .report_generator import report_generator

class EmailExtractor:
    """
    Extracts unique email addresses from a given text file using regular expressions.
    """
    
    # Regex pattern for matching valid email addresses
    EMAIL_REGEX = r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}'

    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def extract(self):
        """Reads the file, extracts unique emails, prints them, and logs the results."""
        if not self.file_path.exists() or not self.file_path.is_file():
            logger.error(f"Extract Emails - Failed - File Not Found: {self.file_path}")
            print(f"Error: The file '{self.file_path}' was not found.")
            return

        print(f"\nExtracting emails from: {self.file_path}")
        logger.info(f"Extract Emails - Started - Reading {self.file_path}")

        try:
            with open(self.file_path, 'r', encoding='utf-8') as file:
                content = file.read()

            if not content.strip():
                logger.error(f"Extract Emails - Failed - Empty File: {self.file_path}")
                print("Error: The file is empty.")
                return

            # Find all emails and convert to set to remove duplicates
            extracted_emails = set(re.findall(self.EMAIL_REGEX, content))

            if not extracted_emails:
                print("No email addresses found in the file.")
                logger.info("Extract Emails - Success - No Emails Found")
                return

            print("\nExtracted Email Addresses:")
            current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            
            for email in extracted_emails:
                print(f"- {email}")
                # Save to report
                report_generator.add_email_record(email, current_date)

            print(f"\nTotal unique emails found: {len(extracted_emails)}")
            logger.info("Extract Emails - Success - Emails Extracted Successfully")

        except PermissionError:
            logger.error("Extract Emails - Failed - Permission Error while reading file")
            print("Error: Permission denied while accessing the file.")
        except Exception as e:
            logger.error(f"Extract Emails - Failed - {str(e)}")
            print(f"An unexpected error occurred: {e}")

def run_email_extractor():
    file_path = input("Enter the text file path to extract emails from: ").strip()
    extractor = EmailExtractor(file_path)
    extractor.extract()
