# Python mini projects

## 🔖Automation with Selenium
This Python project demonstrates how to use Selenium WebDriver to interact with and test a web page. The script uses Selenium's Chrome WebDriver to automate actions on the "Selenium Easy" demo web page.

## 🔖PassChecker -- Password Pwned Checker

This Python project helps you check whether your password has been exposed in a data breach using the "Have I Been Pwned?" API (https://haveibeenpwned.com/Passwords). The script reads a list of passwords from a text file and checks each password against the API to determine if it has been compromised.

### How it works

The script performs the following steps for each password in the provided list:

1. Encodes the password as a UTF-8 string.
2. Hashes the password using the SHA-1 algorithm.
3. Retrieves the first five characters of the hashed password.
4. Sends a request to the "Have I Been Pwned?" API with the first five characters of the hashed password.
5. Parses the API response to find the list of compromised passwords that start with the same five characters.
6. Compares the remaining characters of the hashed password with the retrieved list.
7. If a match is found, the script prints the number of times the password has been found in data breaches. Otherwise, it prints that the password has not been found.

### Usage

1. Create a text file named `list_to_check.txt` in the same directory as the script.
2. Add the passwords you want to check to the file, separated by commas. Each line can have multiple passwords.
3. Run the script using the following command:
```bash
python password_pwned_checker.py
```

## 🔖Web scraper
This project is a Python script that scrapes news articles from the Hacker News website (https://news.ycombinator.com/) and prints the articles that have received over 99 votes checking 3 pages on the Hacker News website.
The script uses the `requests` and `BeautifulSoup` libraries to fetch and parse the HTML content of the website, and then the `pprint` library to print the resulting list of articles in a neat and easy-to-read format.

## 🔖Check pass validity
(length and used characters) + unittest of the code
Passwords should be >= 8 characters long, a-z, A-Z, 0-9, #%$@, and end with a number

## 🔖PDF Merger

This Python project allows you to merge multiple PDF files into a single PDF file. It uses the PyPDF2 library to handle PDF file processing.

### How it works

The script accepts a list of PDF files as command-line arguments and processes them in the order they are provided. It appends each PDF file to a new file called `merged.pdf`, which will be created in the same directory as the script. The script also prints the progress of each processed file and a final message once all files have been merged.

### Usage

To use the script, run the following command:

```bash
python pdf_merger.py file1.pdf file2.pdf file3.pdf
```

