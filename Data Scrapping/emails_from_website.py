import re
import requests
from bs4 import BeautifulSoup

# Define the website URL
url = "https://www.fakemailgenerator.com/#/armyspy.com/Moul1946/"  

# Fetch the webpage content
response = requests.get(url)

# If the request was successful, proceed to extract emails
if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Extract all text content from the page
    webpage_text = soup.get_text()

    # Define the same email regex pattern
    email_pattern = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+'

    # Use regex to find all emails in the page content
    emails = re.findall(email_pattern, webpage_text)

    # Output the found emails
    print(f"Found {len(emails)} emails on {url}:")
    for email in emails[:50]:  # Print first 50 emails
        print(email)
else:
    print(f"Failed to retrieve the webpage. Status code: {response.status_code}")
