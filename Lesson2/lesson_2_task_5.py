def mounth_to_season(mounth):
    if mounth in [12, 1, 2]:
     return "Зима"
    elif mounth in [3, 4, 5]:
     return "Весна"
    elif mounth in [6, 7, 8]:
     return "Лето"
    elif mounth in [9, 10, 11]:
     return "Осень"
    else:
     return "Неверный номер месяца"


print(mounth_to_season(1))
print(mounth_to_season(5))
print(mounth_to_season(6))
print(mounth_to_season(10))
print(mounth_to_season(15))
