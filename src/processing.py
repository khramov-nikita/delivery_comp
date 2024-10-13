import pandas as pd
import datetime
import os


path = os.path.dirname(__file__)
comp_path = os.path.join(path[:-3], "data", "comp.xlsx")
shifts_path = os.path.join(path[:-3], "data", "shifts.xlsx")
result_path = os.path.join(path[:-3], "data", "result.xlsx")


def processing():
    shifts = pd.read_excel(shifts_path)
    shifts_list: list = shifts.to_dict(orient="records", into=dict)

    comp = pd.read_excel(comp_path)
    comp_list: list = comp.to_dict(orient="records", into=dict)

    managers = set()
    for shift in shifts_list:
        managers.add(shift['Имя'])

    managers_and_shifts = dict()
    for manager in managers:
        managers_and_shifts[manager] = []

    comp_datetime = []
    for comp in comp_list:
        date = datetime.datetime.strptime(comp['Дата заказа'], "%d.%m.%Y")
        time = datetime.datetime.strptime(comp['Время заказа'], "%H:%M:%S")
        comp_datetime.append((date, time))


    print(comp_datetime)
    print(managers)
    print(shifts_list)
    print(comp_list)


if __name__ == "__main__":
    processing()
