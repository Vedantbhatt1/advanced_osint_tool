import requests
import re
from bs4 import BeautifulSoup

def scrape_emails(url):
    emails = set()
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        text = soup.get_text()
        emails.update(re.findall(r"[\w\.-]+@[\w\.-]+", text))
    except Exception as e:
        emails.add(f"Error scraping emails: {e}")
    return list(emails)