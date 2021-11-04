import config
from parser import Parser

USERNAME = config.USERNAME
PASSWORD = config.PASSWORD
a = Parser(USERNAME, PASSWORD)
a.parse()
for i in range(6):
    for k in a[i]:
        print(f"{k.name}: {k.homework }")
