import datetime
from datetime import datetime, timedelta
today = datetime.today()
today_date = today.date()

certain_date_string = input("Введіть дату у форматі РРРР.ММ.ДД: ")
certain_date_object = datetime.strptime(certain_date_string, "%Y.%m.%d")

def get_days_from_today():
    if today_date != certain_date_object:
        difference = datetime.strptime(certain_date_string,"%Y.%m.%D") - datetime.today
        print(difference.days)
    else:
        print("Дата введена невірно")         
