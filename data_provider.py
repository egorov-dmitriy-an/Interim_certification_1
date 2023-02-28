from datetime import datetime as dt

def get_note(index):
    if index == 1:
        note = (input('Введите заголовок или его часть латиницей: '))
        return note
    elif index == 2:
        id = (input('Введите id: '))
        heading = (input('Введите заголовок: '))
        body = (input('Введите тело: '))
        change = dt.now().strftime('%d.%m.%y %H:%M:%S')
        note = (id, heading, body, change)
        return note
