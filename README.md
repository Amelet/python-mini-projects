# Python mini projects

## Automation with Selenium
Use Selenium to test a submission form on a website

## PassChecker
Test your password using https://haveibeenpwned.com if it has ever been compromised.<br>
The algorithm accepts a list of passwords given in the list_to_check.txt. If several passwords are given, they should be separated by comma.<br>
To check each password, the algorithm will:
1. Hash each password using sha1;
2. Get first five characters of hashed password;
3. Send a request to api.pwnedpasswords.com/range/{first 5 hash characters} to check if first five characters of the password match with compromised passwords;
4. Retrieve the list of compromised passwords that start with the same five characters;
5. On the computer where python is run, the algorithm compares remaining characters of a being checked password with the retrieved ones;
6. The algorithm returns counts how many times the password is found in the data set.


## Web scraper
Scraping https://news.ycombinator.com/ website to retrieve links to the news that have >99 votes. The algorithm checks first three pages of the website.


## Check pass validity
(length and used characters) + unittest of the code
Passwords should be >= 8 characters long, a-z, A-Z, 0-9, #%$@, and end with a number

## PDF Merger

This Python project allows you to merge multiple PDF files into a single PDF file. It uses the PyPDF2 library to handle PDF file processing.

### How it works

The script accepts a list of PDF files as command-line arguments and processes them in the order they are provided. It appends each PDF file to a new file called `merged.pdf`, which will be created in the same directory as the script. The script also prints the progress of each processed file and a final message once all files have been merged.

### Usage

To use the script, run the following command:

```bash
python pdf_merger.py file1.pdf file2.pdf file3.pdf


