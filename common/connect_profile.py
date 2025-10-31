import json
from datetime import date
from dateutil.relativedelta import relativedelta



def start_profile(id: int):
    with open('json_files/profile.json', 'r') as f:
        data = json.load(f)
    
    if str(id) not in data:
        with open('json_files/profile.json', 'w') as f1:
            a = {id: {"tarif": "Start",
                      "time": "Бесконечно",
                      "all_filters": "Ограниченно"}}
            json.dump(a, f1, indent=2)
            

def read_profile(id: int):
    id = str(id)
    with open('json_files/profile.json', 'r') as f:
        a = json.load(f)
    tarif = a[id]['tarif']
    time = a[id]['time']
    all_filter = a[id]['all_filters']

    return tarif, time, all_filter


def change_profile(id: int, data: str):
    next_month = date.today() + relativedelta(months=1)

    if data == 'button5_click':
        with open('json_files/profile.json', 'w') as f:
            a = {id: {"tarif": "Plus",
                      "time": f"{next_month}",
                      "all_filters": "Среднее"}}
            json.dump(a, f, indent=2)
    elif data == 'button6_click':
        with open('json_files/profile.json', 'w') as f:
            a = {id: {"tarif": "Pro",
                      "time": f"{next_month}",
                      "all_filters": "Нету"}}
            json.dump(a, f, indent=2)
    else:
        new_date = str(date.today() + relativedelta(month=6))
        with open('json_files/profile.json', 'r') as f:
            data = json.load(f)

        data[str(id)]['time'] = new_date

        with open('json_files/profile.json', 'w') as f:
            json.dump(data, f, indent=2)
