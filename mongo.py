from pymongo import MongoClient
from pymongo.server_api import ServerApi
from bson.objectid import ObjectId


client = MongoClient(
    "mongodb+srv://ihormongo:240471@authors.jmixi1f.mongodb.net/",
    server_api=ServerApi('1')
)

# Вибір або створення бази даних
db = client['cats_database']
# Вибір або створення колекції
cats_collection = db['cats']

result_one = db.cats.insert_one(
    {
        "name": "barsik",
        "age": 3,
        "features": ["ходить в капці", "дає себе гладити", "рудий"],
    }
)

print(result_one.inserted_id)

result_many = db.cats.insert_many(
    [
        {
            "name": "Lama",
            "age": 2,
            "features": ["ходить в лоток", "не дає себе гладити", "сірий"],
        },
        {
            "name": "Liza",
            "age": 4,
            "features": ["ходить в лоток", "дає себе гладити", "білий"],
        },
    ]
)
print(result_many.inserted_ids)


# Читання (Read)
def read_all_cats():
    """Функція для виведення всіх записів із колекції."""
    cats = cats_collection.find()
    for cat in cats:
        print(cat)

def read_cat_by_name(name):
    """Функція для виведення інформації про кота за ім'ям."""
    cat = cats_collection.find_one({"name": name})
    if cat:
        print(cat)
    else:
        print("Кіт з таким ім'ям не знайдено.")

# Оновлення (Update)
def update_cat_age(name, new_age):
    """Функція для оновлення віку кота за ім'ям."""
    cats_collection.update_one({"name": name}, {"$set": {"age": new_age}})
    print("Вік кота оновлено.")

def add_cat_feature(name, new_feature):
    """Функція для додавання нової характеристики кота за ім'ям."""
    cats_collection.update_one({"name": name }, {"$push": {"features": new_feature}})
    print("Нову характеристику додано.")

# Видалення (Delete)
def delete_cat_by_name(name):
    """Функція для видалення запису з колекції за ім'ям тварини."""
    cats_collection.delete_one({"name": name})
    print("Кіт видалено.")

def delete_all_cats():
    """Функція для видалення всіх записів із колекції."""
    cats_collection.delete_many({})
    print("Всіх котів видалено.")


   # Тестування
if __name__ == "__main__":

    while True:  # Безкінечний цикл для інтерактивного введення команд
        
        print("\nМеню:")
        print("1. Переглянути всіх котів")
        print("2. Знайти кота за ім'ям")
        print("3. Оновити вік кота")
        print("4. Додати характеристику кота")
        print("5. Видалити кота за ім'ям")
        print("6. Видалити всіх котів")
        print("7. Вийти з програми")

        choice = input("\nВведіть номер опції: ")

        if choice == "1":
            try:
                read_all_cats()
            except Exception as e:
                print(f"Помилка: {e}")

        elif choice == "2":
            name = input("Введіть ім'я кота: ")
            try:
                read_cat_by_name(name)
            except Exception as e:
                print(f"Помилка: {e}")

        elif choice == "3":
            name = input("Введіть ім'я кота: ")
            new_age = int(input("Введіть новий вік кота: "))
            try:
                update_cat_age(name, new_age)
            except Exception as e:
                print(f"Помилка: {e}")

        elif choice == "4":
            name = input("Введіть ім'я кота: ")
            new_feature = input("Введіть нову характеристику: ")
            try:
                add_cat_feature(name, new_feature)
            except Exception as e:
                print(f"Помилка: {e}")

        elif choice == "5":
            name = input("Введіть ім'я кота, якого потрібно видалити: ")
            try:
                delete_cat_by_name(name)
            except Exception as e:
                print(f"Помилка: {e}")

        elif choice == "6":
            confirm = input("Ви впевнені, що хочете видалити всіх котів? (Так/Ні): ")
            if confirm.lower() == "так":
                try:
                    delete_all_cats()
                except Exception as e:
                    print(f"Помилка: {e}")
            else:
                print("Операція видалення скасована.")

        elif choice == "7":
            print("До побачення!")
            break

        else:
            print("Невідома опція. Будь ласка, введіть правильний номер опції.")
