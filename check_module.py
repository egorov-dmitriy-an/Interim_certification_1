def check_start():
    while True:
        sensor = ''
        while sensor.isdecimal() == False:
            sensor = input('Для поиска заметки нажмите      - 1\n'
                           'Для добавления заметки нажмите  - 2\n'
                           'Для показа всех заметок нажмите - 3\n'
                           'Для выхода нажмите              - 0\n'
                           ': ')
        if 0 <= int(sensor) <= 3:
            break
        else:
            sensor = input('Для поиска заметки нажмите      - 1\n'
                           'Для добавления заметки нажмите  - 2\n'
                           'Для показа всех заметок нажмите - 3\n'
                           'Для выхода нажмите              - 0\n'
                           ': ')
    return int(sensor)

def check_actions():
    while True:
        sensor = ''
        while sensor.isdecimal() == False:
            sensor = input('Для удаления заметки нажмите        - 4\n'
                           'Для редактирования заметки нажмите  - 5\n'
                           'Для показа деталей заметки нажмите  - 6\n'
                           'Для выхода нажмите                  - 7\n'
                           ': ')
        if 4 <= int(sensor) <= 7:
            break
        else:
            sensor = input('Для удаления заметки нажмите        - 4\n'
                           'Для редактирования заметки нажмите  - 5\n'
                           'Для показа деталей заметки нажмите  - 6\n'
                           'Для выхода нажмите                  - 7\n'
                           ': ')
    return int(sensor)