# 📌Функция получает на вход текст вида: “1-й четверг ноября”, “3я среда мая” и т.п. 
# 📌Преобразуйте его в дату в текущем году. 
# 📌Логируйте ошибки, если текст не соответсвует формату.
import re
import locale
import logging
from datetime import date
from datetime import timedelta
locale.setlocale(locale.LC_ALL, "Russian")

def parse_date(string):
    try:
        weekdays = {
            'понедельник': 0,
            "вторник": 1,
            "среда": 2,
            "четверг": 3,
            "пятница": 4,
            "суббота": 5,
            "воскресенье": 6,
        }
        months = {'января': 1, 
                'февраля': 2, 
                'марта': 3, 
                'апреля': 4, 
                'мая': 5, 
                'июня': 6, 
                'июля': 7, 
                'августа': 8, 
                'сентября': 9, 
                'октября': 10, 
                'ноября': 11, 
                'декабря': 12
                }
        
        day_no = int(re.findall(r'\d+', string)[0])
        _weekday = weekdays[string.split()[1]]
        _months = months[string.split()[2]]

        startdate = date(2023, _months, 1)
        weekday_count = 0
        while weekday_count < day_no:

            if startdate.weekday() == _weekday:
                weekday_count += 1
            startdate += timedelta(days = 1)
        return startdate - timedelta(days = 1)
    except Exception as e:
        logging.basicConfig(level=logging.INFO, filename="loger.log", filemode="a",
                    format='%(levelname)s, %(asctime)s, %(message)s')
        logging.error(e)

print(parse_date(input('>>>')))