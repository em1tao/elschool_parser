import requests
from bs4 import BeautifulSoup


class Lesson:

    def __init__(self, name: str, homework: str, time: str):
        self.name = name
        self.homework = homework
        self.time = time


class Day:

    def __init__(self, name: str, date: str, lessons: list):
        self.name = name
        self.date = date
        self.lessons = lessons

    def __getitem__(self, key: int):
        return self.lessons[key]


class Parser:

    def __init__(self, login: str, password: str) -> None:
        """
        :param login: A string representing of the login.
        :param password: A string representing of the password.
        """
        self.login = login
        self.password = password
        self.days = []
        self.session = requests.session()

    def __authorization(self) -> bool:
        """Authorizes into the diary."""
        form_data = {'login': self.login, 'password': self.password}
        auth_request = self.session.post('https://elschool.ru/logon/index', 
                                         data=form_data)
        return auth_request.status_code == 200

    def __parse_lesson(self, lesson: BeautifulSoup) -> Lesson:
        lesson_name = lesson.find('div', {'class': 'flex-grow-1'}).text
        lesson_time = lesson.find('div', {'class': 'diary__discipline__time'}).text
        homework = lesson.find('div', {'class': 'diary__homework-text'}).text
        return Lesson(lesson_name, homework, lesson_time)

    def __parse_day(self, table: BeautifulSoup) -> Day:
        lessons_elements = table.findAll('tr', {'class': 'diary__lesson'})
        day_name, day_date = lessons_elements[0].find('td', {'class': 'diary__dayweek'}).text.split()
        lessons = []
        for lesson in lessons_elements:
            lessons.append(self.__parse_lesson(lesson))
        return Day(day_name, day_date, lessons)

    def parse(self) -> str:
        if not self.__authorization():
            return 'Authorization failed'
        main_request = self.session.get('https://elschool.ru/users/diaries')
        parsed_html = BeautifulSoup(main_request.content, "lxml")
        diary = parsed_html.find('div', {'class': 'diaries'})
        tables = diary.findAll('tbody')
        for table in tables[:-1]:
            self.days.append(self.__parse_day(table))
        return 'Successful'
 
    def __getitem__(self, key):
        return self.days[key]
