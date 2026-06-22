import sys
from pathlib import Path

# Import the module runners and logger
from modules.file_organizer import run_file_organizer
from modules.email_extractor import run_email_extractor
from modules.webpage_scraper import run_webpage_scraper
from modules.logger_setup import logger

def display_menu():
    """Displays the main application menu."""
    print("\n====================================")
    print(" SMART FILE AUTOMATION TOOLKIT")
    print("====================================")
    print("1. Organize Files")
    print("2. Extract Emails")
    print("3. Scrape Website Title")
    print("4. View Reports")
    print("5. Exit")
    print("====================================")

def view_reports():
    """Reads and displays the contents of the generated CSV reports."""
    print("\nAvailable Reports:")
    reports_dir = Path("reports")
    
    if not reports_dir.exists() or not any(reports_dir.iterdir()):
        print("No reports found.")
        return

    for report_file in reports_dir.glob("*.csv"):
        print(f"\n--- {report_file.name} ---")
        try:
            with open(report_file, 'r', encoding='utf-8') as f:
                content = f.read()
                # Print the content, or a message if the file only has headers or is empty
                lines = content.strip().split('\n')
                if len(lines) <= 1:
                    print("Report is empty (no records).")
                else:
                    print(content.strip())
        except Exception as e:
            print(f"Error reading {report_file.name}: {e}")
            logger.error(f"Failed to read report {report_file.name}: {e}")

def main():
    """Main application loop."""
    logger.info("Application Started")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            logger.info("User selected: Organize Files")
            run_file_organizer()
        elif choice == '2':
            logger.info("User selected: Extract Emails")
            run_email_extractor()
        elif choice == '3':
            logger.info("User selected: Scrape Website Title")
            run_webpage_scraper()
        elif choice == '4':
            logger.info("User selected: View Reports")
            view_reports()
        elif choice == '5':
            logger.info("Application Exited")
            print("Exiting Smart File Automation Toolkit. Goodbye!")
            sys.exit(0)
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram interrupted by user. Exiting...")
        logger.info("Application Exited via KeyboardInterrupt")
        sys.exit(0)
    except Exception as e:
        logger.critical(f"Fatal error occurred: {e}")
        print(f"\nA fatal error occurred: {e}")
        sys.exit(1)
