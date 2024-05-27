import json
from datetime import datetime
from operator import itemgetter


def load_operations():
    """получение списка операций из json файла"""
    with open("operations.json", encoding="utf-8") as file_operations:
        return json.load(file_operations)


def execeted_operation():
    """выбираем только проведенные операции"""
    exe_operation = []
    for i in load_operations():
        for val in i.values():
            if val == 'EXECUTED':
                exe_operation.append(i)
    return exe_operation


def sorted_date():
    """создаем список из последних пяти проведенных операций"""
    date_operation = []
    for i in execeted_operation():
        for key in i.keys():
            if key == 'date':
                i[key] = datetime.fromisoformat(i[key]) #переводим строку в формат даты
                date_operation.append(i) #формируем новый список
    return sorted(date_operation, key=itemgetter('date'), reverse=True)[:5] #сортируем список по дате и оставляем 5 первых


def hiding_list():
    """Скрытие номера карты и счёта"""
    hidding_list = sorted_date()
    for i in range(5):
        if 'from' in hidding_list[i]:
            list_card = hidding_list[i]['from'].split(" ")
            for element in range(len(list_card)):
                #шифруем карту в from
                if len(list_card[element]) == 16:
                    list_card[element] = (f' {"".join(list_card[element][:5])} {"".join(list_card[element][5:7])}** **** {"".join(list_card[element][-4:])}')
                    hidding_list[i]['from'] = " ".join(list_card)
                #шифруем счет в from
                elif len(list_card[element]) == 20:
                    list_card[element] = (f'**{"".join(list_card[element][-4:])}')
                    hidding_list[i]['from'] = " ".join(list_card)
        hidding_list[i]['to'] = (f'**{"".join(hidding_list[i]["to"])[-4:]}') #шифруем счет
    return hidding_list


def latest_operation():
    """итоговый вывод информации"""
    latest_operation = ""
    for i in hiding_list():
        #дата и тип операции
        latest_operation = latest_operation + (f'{i["date"].strftime("%d.%m.%Y")} {i["description"]}\n')
        #откуда (при наличии) и куда
        if 'from' in i:
            latest_operation = latest_operation + (f'{i["from"]} -> Счет {i["to"]}\n')
        else:
            latest_operation = latest_operation + (f'Счет {i["to"]}\n')
        #сумма перевода
        latest_operation = latest_operation + (f'{i["operationAmount"]["amount"]} {i["operationAmount"]["currency"]["name"]}\n\n')
    return latest_operation












