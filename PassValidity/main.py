import sys
import re

def check_pass_validity(string):
    #pass checker
    pattern = re.compile(r"[a-zA-Z\d$%#@]{7,}\d")
    a = pattern.fullmatch(string)
    if a != None:
        return True
    else:
        return None

if __name__ == "__main__":
    while True:
        string = input("password:    ")
        a = check_pass_validity(string)

        if a==None:
            print("Passwords should be >= 8 characters long, a-z, A-Z, 0-9, #%$@, and end with a nuber")
        else:
            print("Password is accepted")
            break
