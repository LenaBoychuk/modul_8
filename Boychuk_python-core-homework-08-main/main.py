from datetime import datetime, date, timedelta
current_date = date.today() + timedelta(days=0)

def get_birthdays_per_week(users):
    #current_date = datetime(2023, 12, 26)

    #from datetime import date # Без цього не бачить локальну змінну data
    #current_date = date.today() + timedelta(days=0)

    # створення послідовності днів тижня для ключів
    # початок від сьогодні, якщо це не понеділок і не вихідні. Інакше з суботи
    #(субота і неділя навмисно тут)
    current_weekday = current_date.weekday()
    dict_remember = {}
    dict_remember_keys = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    if current_weekday in [1, 2, 3, 4]:
        for _ in range(current_weekday + 2):
            day_replace = dict_remember_keys.pop(0)
            dict_remember_keys.append(day_replace)

    # поправка для перебігу дат у відповідності до послідовності днів тижня        
    if current_weekday in [1, 2, 3, 4, 5]:
        amendment = 0
    elif current_weekday == 6:
        amendment = -1
    elif current_weekday == 0:
        amendment = -2

#   # цикл на виявлення іменинників (враховано і кілька іменинників в день)
    for i in range(7):

        dict_remember[dict_remember_keys[i]] = []# пусті списки (це вигідно тільки для Monday, якщо ДР на вихідних) 
        interval = timedelta(days=i+amendment)
        date = current_date + interval
        for j in users: 
            if j['birthday'].month == date.month and j['birthday'].day == date.day:
                dict_remember[dict_remember_keys[i]].append(j['name'])
                continue   
    users = dict_remember #за вимогою повертає users
    #перенесення з вихідних на понеділок

    if users['Saturday'] != []:
        for _ in range(len(users['Saturday'])):
            replaced_name = users['Saturday'].pop()
            users['Monday'].append(replaced_name)
    if users['Sunday'] != []:
         for _ in range(len(users['Sunday'])):
            replaced_name = users['Sunday'].pop()
            users['Monday'].append(replaced_name)
    #видалення із словника пустих списків
    for key in dict_remember_keys:
        if users[key] == []: 
            users.pop(key)
    return users
    


if __name__ == "__main__":
    users = [{"name": "Bill Gates", "birthday": datetime(1955, 10, 28).date()},
 {"name": "Bella", "birthday": datetime(1980, 9, 13).date()},
 {"name": "Syr", "birthday": datetime(1970, 9, 10).date()},
 {"name": "Sar", "birthday": datetime(1970, 9, 9).date()},
 {"name": "Sar", "birthday": datetime(1972, 9, 8).date()},
 {"name": "Aga", "birthday": datetime(1974, 9, 7).date()},
 {"name": "Tan", "birthday": datetime(1976, 9, 6).date()},
 {"name": "Lor", "birthday": datetime(1976, 9, 5).date()},
 {"name": "Lar", "birthday": datetime(1976, 9, 5).date()},
 {"name": "Lyr", "birthday": datetime(1976, 9, 4).date()},
 {"name": "Sfr", "birthday": datetime(1970, 9, 3).date()}]

    result = get_birthdays_per_week(users)
    print(result)
    # Виводимо результат

    
    for day_name, names in result.items():
        print(f"{day_name}: {', '.join(names)}")
