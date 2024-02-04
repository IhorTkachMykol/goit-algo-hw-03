import datetime

def get_days_from_today(today, certain_date_object):
    if today != certain_date_object:
        difference = certain_date_object - today
        print("Різниця в днях:", difference.days)
    else:
        print("Введена дата співпадає з сьогоднішньою")

try:
    today = datetime.datetime.today().date()

    certain_date_string = input("Введіть дату у форматі РРРР-ММ-ДД: ")
    certain_date_object = datetime.datetime.strptime(certain_date_string, "%Y-%m-%d").date()

    get_days_from_today(today, certain_date_object)

except ValueError:
    print("Неправильний формат дати. Введіть дату у форматі РРРР-ММ-ДД")
