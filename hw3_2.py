import random

lotnums=list()
numbers=[]
min = int(input("Введіть нижню межу діапазону: "))
max = int(input("Введіть верхню межу діапазону:  "))
quantity = int(input("Введіть кількість номерів в лотереї: "))  

def get_numbers_ticket(min, max, quantity):

    for i in (min, max, quantity):

        if (min >=1 and max<=1000) and 1<quantity<999:
            numbers = random.sample(range(min, max+1), quantity)
        else:
            print("Невірно введені дані")    

lotnums = sorted(numbers)
lotmums = lotnums.append(numbers)
      
print(f"Лотерейні номери {lotnums}")