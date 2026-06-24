import logging
import os
from pathlib import Path

def setup_logger():
    """
    Sets up and configures the logger for the application.
    """
    # Ensure logs directory exists
    log_dir = Path("logs")
    log_dir.mkdir(exist_ok=True)
    log_file = log_dir / "automation.log"

    # Define the log format
    # Format: Timestamp Level Message (We will format message as "Operation - Status")
    formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s', datefmt='%Y-%m-%d %H:%M:%S')

    logger = logging.getLogger("SmartFileAutomation")
    logger.setLevel(logging.INFO)

    # Create file handler
    file_handler = logging.FileHandler(log_file)
    file_handler.setFormatter(formatter)
    
    # Create console handler for real-time feedback
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(formatter)

    # Avoid adding handlers multiple times
    if not logger.handlers:
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)

    return logger

# Expose a configured logger instance
logger = setup_logger()
