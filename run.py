import config
from parser import Parser

USER = config.USER
PASSWORD = config.PASSWORD
a = Parser(USER, PASSWORD)
a.parse()
print(a.days)
