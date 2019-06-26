import re

pw = input("Input test password\n")

def checkPW(pw):
    pwRegex = re.compile(r'[a-zA-Z]{8,}', re.IGNORECASE)
