import requests
from bs4 import BeautifulSoup
from datetime import datetime
from .logger_setup import logger
from .report_generator import report_generator

class WebpageScraper:
    """
    Fetches a webpage URL and extracts its title tag.
    """
    
    def __init__(self, url: str):
        self.url = url

    def _ensure_schema(self, url: str) -> str:
        """Ensures the URL has a schema (http/https)."""
        if not url.startswith('http://') and not url.startswith('https://'):
            return 'https://' + url
        return url

    def scrape_title(self):
        """Fetches the webpage and parses the title."""
        if not self.url.strip():
            logger.error("Scrape Website Title - Failed - Invalid URL (Empty)")
            print("Error: Invalid URL.")
            return

        formatted_url = self._ensure_schema(self.url.strip())
        print(f"\nFetching: {formatted_url}")
        logger.info(f"Scrape Website Title - Started - Fetching {formatted_url}")

        try:
            # Set a timeout and User-Agent to avoid getting blocked or hanging
            headers = {
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
            }
            response = requests.get(formatted_url, headers=headers, timeout=10)
            
            # Raise an exception for HTTP errors
            response.raise_for_status()

            # Parse HTML content
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract title
            title_tag = soup.find('title')
            
            if title_tag and title_tag.string:
                title = title_tag.string.strip()
            else:
                title = "No title tag found"

            print(f"Title Found: {title}")
            
            # Save to report
            current_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            report_generator.add_webpage_record(formatted_url, title, current_date)
            
            logger.info("Scrape Website Title - Success - Website Title Scraped Successfully")

        except requests.exceptions.MissingSchema:
            logger.error(f"Scrape Website Title - Failed - Invalid URL: {formatted_url}")
            print(f"Error: Invalid URL format '{formatted_url}'.")
        except requests.exceptions.ConnectionError:
            logger.error(f"Scrape Website Title - Failed - Internet Connection Failure for {formatted_url}")
            print("Error: Internet Connection Failure or DNS resolution failed.")
        except requests.exceptions.Timeout:
            logger.error(f"Scrape Website Title - Failed - Timeout while fetching {formatted_url}")
            print("Error: The request timed out. The server might be down or slow.")
        except requests.exceptions.HTTPError as errh:
            logger.error(f"Scrape Website Title - Failed - HTTP Error: {errh}")
            print(f"HTTP Error: {errh}")
        except Exception as e:
            logger.error(f"Scrape Website Title - Failed - {str(e)}")
            print(f"An unexpected error occurred: {e}")

def run_webpage_scraper():
    url = input("Enter the URL to scrape the title from: ").strip()
    scraper = WebpageScraper(url)
    scraper.scrape_title()
