# import datetime
# x = datetime.datetime.now()
# print(x.year)
# print(x.strftime("%A"))



# import datetime
# x = datetime.datetime(2018, 6, 1)
# print(x.strftime("%B"))



# import datetime
# first = datetime.datetime(2023, 4, 17)
# second = datetime.datetime(2024, 7, 30)
# third = datetime.datetime(2023, 6, 3)

# sum_days = [int(first.strftime("%d")), int(second.strftime("%d")), int(third.strftime("%d"))]
# print(sum(sum_days))





# from datetime import datetime
# from datetime import timedelta
# now = datetime.now()
# date_first = datetime(2005, 8, 27) # <--- Tutaj wprowadź swoją datę urodzenia
# day = now - date_first
# print(day.days)



# import datetime
# import time

# time.sleep(5)
# x = datetime.datetime.now()
# print(x.strftime("%A"))




# import datetime
# import time

# def main():
#     print("Цей код виведе сьогоднішню дату через 5 сек.")
    
#     # Затримка на 5 сек
#     time.sleep(5)
    
#     # Отримання поточної дати та часу
#     today = datetime.datetime.now()
    
#     # Виведення сьогоднішньої дати
#     print("Сьогоднішня дата:", today.strftime("%Y-%m-%d"))

# if __name__ == "__main__":
#     main()




from datetime import datetime, date, timedelta
date_object = datetime.strptime("2023-Nov-15", "%Y-%b-%d")
new_date = date_object + timedelta(days=5)
print(new_date.strftime("%Y-%b-%d"))

