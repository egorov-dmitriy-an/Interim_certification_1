from datetime import datetime as dt

def get_note(index):
    if index == 1:
        note = (input('Введите заголовок для поиска: '))
        return note
    elif index == 2:
        id_note = (input('Введите id: '))
        heading = (input('Введите заголовок: '))
        body = (input('Введите тело: '))
        change = dt.now().strftime('%d.%m.%y %H:%M:%S')
        note = (id_note, heading, body, change)
        return note
    elif index == 0:
        return 0


