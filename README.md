# mini_projects

**Project #1: Automation with Selenium**
Use Selenium to test a submission form on a website


**Project#2: PassChecker**
Test your password using https://haveibeenpwned.com if it has ever been compromised.
The algorithm accepts a list of passwords given in the list_to_check.txt. If several passwords are given, they should be separated by comma. 
To check each passord, the algorithm will:
1. Hash each password using sha1;
2. Get first five characters of hashed password;
3. Send a request to api.pwnedpasswords.com/range/{first 5 hash characters} to check if first five characters of the password match with compromised passwords;
4. Retrieve the list of compromised passords that start with the same five characters;
5. On the computer where python is run, the algorithm compares remaining characters of a being checked password with a retrieved ones;
6. The algorithm returns counts how many times the password is found in the data set.


**Project 3: Web scraper**
Scraping https://news.ycombinator.com/ website to retrieve links to the news that have >99 votes. The algorithm checks first three pages of the website.


**Project 4: Check pass validity (length and used characters) + unittest of the code**
Passwords should be >= 8 characters long, a-z, A-Z, 0-9, #%$@, and end with a number

