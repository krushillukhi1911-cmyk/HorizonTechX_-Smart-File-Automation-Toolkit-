# HorizonTechX_SmartFileAutomationToolkit

## Project Overview
The **Smart File Automation Toolkit** is a menu-driven Python application designed to automate common, repetitive tasks. It acts as an all-in-one suite for file organization, data extraction, and web scraping, packaged with professional-grade logging and reporting features.

This project is beginner-friendly yet structured following real-world software architecture principles, making it an excellent addition to a portfolio or resume.

## Features
1. **Organize Files**: Automatically categorize and move files from a source directory into specific folders (Images, Documents, Excel, Text Files) based on their extensions.
2. **Extract Emails**: Read a given text file, extract all valid email addresses using Regular Expressions, and remove duplicates.
3. **Scrape Website Title**: Fetch a webpage URL and extract its HTML `<title>` tag.
4. **View Reports**: Review auto-generated CSV reports summarizing all automated actions.
5. **Logging System**: A robust logging mechanism that records the status, timestamp, and details of all operations to `logs/automation.log`.

## Folder Structure
```text
SmartFileAutomationToolkit/
├── main.py
├── modules/
│   ├── __init__.py (optional)
│   ├── file_organizer.py
│   ├── email_extractor.py
│   ├── webpage_scraper.py
│   ├── report_generator.py
│   └── logger_setup.py
├── logs/
│   └── automation.log
├── reports/
│   ├── file_report.csv
│   ├── email_report.csv
│   └── webpage_report.csv
├── sample_data/
│   ├── source_folder/
│   ├── destination_folder/
│   └── emails.txt
├── requirements.txt
└── README.md
```

## Installation Steps
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/HorizonTechX_SmartFileAutomationToolkit.git
   cd HorizonTechX_SmartFileAutomationToolkit
   ```
2. **Create a virtual environment (Optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage Instructions
1. Run the application from the terminal:
   ```bash
   python main.py
   ```
2. Follow the on-screen menu prompts.
   - For **Organizing Files**, provide the path to your source folder (e.g., `sample_data/source_folder`).
   - For **Extracting Emails**, provide the path to your text file (e.g., `sample_data/emails.txt`).
   - For **Scraping Website Title**, provide a valid URL (e.g., `https://www.python.org`).
3. Check the `logs/automation.log` for execution details or choose option `4` in the main menu to view generated CSV reports.

## Screenshots Section
> *Add screenshots of your terminal running the application, showing the main menu, successful operations, and report outputs.*

## Future Enhancements
- Add support for organizing more file types (e.g., Videos, Audio, Archives).
- Implement a graphical user interface (GUI) using Tkinter or PyQt.
- Expand email extraction to support reading from Word or PDF documents.
- Add multi-threading for scraping multiple websites concurrently.
- Provide email notifications upon task completion.

## Author Information
Developed by **[Krushil Lukhi]**
