import os
import shutil
from pathlib import Path
from datetime import datetime
from collections import defaultdict
from .logger_setup import logger
from .report_generator import report_generator

class FileOrganizer:
    """
    Automates organizing files in a specified directory into categorized folders based on their extensions.
    """
    
    # Mapping of categories to a list of extensions (without the dot)
    CATEGORY_MAPPING = {
        "Images": ["jpg", "jpeg", "png"],
        "Documents": ["pdf", "docx"],
        "Excel": ["xlsx", "csv"],
        "Text Files": ["txt"]
    }

    def __init__(self, source_path: str):
        self.source_dir = Path(source_path)

    def _get_category(self, extension: str) -> str:
        """Determines the category folder based on the file extension."""
        extension = extension.lower().strip('.')
        for category, exts in self.CATEGORY_MAPPING.items():
            if extension in exts:
                return category
        return "Others" # For files that don't match the known extensions

    def organize(self):
        """Scans the source directory and moves files into their corresponding category folders."""
        if not self.source_dir.exists() or not self.source_dir.is_dir():
            logger.error(f"Organize Files - Failed - Invalid source directory: {self.source_dir}")
            print(f"Error: The directory '{self.source_dir}' does not exist.")
            return

        print(f"\nScanning directory: {self.source_dir}")
        logger.info(f"Organize Files - Started - Scanning {self.source_dir}")

        moved_counts = defaultdict(int)

        try:
            for item in self.source_dir.iterdir():
                if item.is_file():
                    extension = item.suffix
                    category = self._get_category(extension)
                    
                    # Create the destination category folder if it doesn't exist
                    dest_folder = self.source_dir / category
                    dest_folder.mkdir(exist_ok=True)
                    
                    dest_path = dest_folder / item.name
                    
                    # Move the file
                    shutil.move(str(item), str(dest_path))
                    moved_counts[category] += 1
                    
                    # Add to report
                    current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    report_generator.add_file_record(
                        file_name=item.name,
                        file_type=extension,
                        destination_folder=category,
                        date=current_date
                    )
            
            # Print output report
            print("\nOrganization complete. Summary:")
            for category, count in moved_counts.items():
                print(f"{count} {category} files moved")
                
            if not moved_counts:
                print("No files were found to move.")
            
            logger.info("Organize Files - Success - Files Organized Successfully")
            
        except PermissionError:
            logger.error("Organize Files - Failed - Permission Error while moving files")
            print("Error: Permission denied while accessing files.")
        except Exception as e:
            logger.error(f"Organize Files - Failed - {str(e)}")
            print(f"An unexpected error occurred: {e}")

def run_file_organizer():
    source = input("Enter the source folder path to organize: ").strip()
    organizer = FileOrganizer(source)
    organizer.organize()
