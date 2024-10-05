
# Email Scraping Projects using Python and Regex

This repository contains two Python projects for scraping emails using regular expressions (regex):

1. **Scraping Emails from Large Text Files**
2. **Scraping Emails from Websites**

Both projects utilize regex patterns to extract email addresses from large datasets and websites, demonstrating different scraping techniques for learning and practical use.

---

## Project 1: Scraping Emails from Large Text Files

This project focuses on extracting email addresses from a large text file using regex. The script reads the content of a text file and applies a regex pattern to identify and extract valid email addresses.

### Features

- Handles large text datasets.
- Efficiently extracts email addresses using regex.
- Outputs the total number of emails found and a sample of the extracted emails.

To run the project, use the script: `Emails_from_text.py`.

---

## Project 2: Scraping Emails from a Website

This project scrapes email addresses from a website using the **BeautifulSoup** library along with regex. The script fetches the content of a webpage, extracts all text, and applies a regex pattern to find and extract email addresses.

### Features

- Fetches webpage content and parses it with BeautifulSoup.
- Uses regex to extract valid email addresses from the page's text content.
- Displays the total number of emails found and a sample of them.

To run the project, use the script: `Emails_from_web.py`.

---

## Requirements

- Python 3.x
- Dependencies:
  - `beautifulsoup4`
  - `requests`
