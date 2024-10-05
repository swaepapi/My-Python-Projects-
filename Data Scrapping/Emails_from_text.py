# Extracting emails from text 

import re
import os

os.chdir(r"C:\Users\fidel\OneDrive\Desktop\MY PROJECTS\My-Python-Projects-\Data Scrapping")


def extract_emails_from_text(text):
    # Regex pattern for extracting emails
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Find all email addresses in the given text
    emails = re.findall(email_pattern, text)
    
    return emails

def read_large_file(file_path):
    try:
        with open(file_path, 'r', encoding='latin-1') as file:
            text_data = file.read()
        return text_data
    except Exception as e:
        print(f"Error reading file: {e}")
        return ""

if __name__ == "__main__":
    file_path = "large_text_file.txt"  # Path to your large text file
    text_data = read_large_file(file_path)
    
    if text_data:
        emails = extract_emails_from_text(text_data)
        print(f"Found {len(emails)} email addresses:")
        print(emails)
