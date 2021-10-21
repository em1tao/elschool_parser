import requests
from bs4 import BeautifulSoup
import config

USER = config.USER
PASSWORD = config.PASSWORD


class Lesson:
    def __init__(self,):
        pass


class Day:
    def __init__(self, name: str):
        self.name = name
        self.lessons = []
        

form_data = {'login': USER, 'password': PASSWORD}
session = requests.session()
session.post('https://elschool.ru/logon/index', data=form_data)
main_request = session.get('https://elschool.ru/users/diaries')
parsed_html = BeautifulSoup(main_req.content, "lxml")
