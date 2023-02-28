def check(sensor):
    while True:
        while sensor.isdecimal() == False:
            sensor = input('Для поиска заметки нажмите 1\n'
                           'Для добавления заметки нажмите 2\n'
                           'Для показа всех заметок нажмите 3\n'
                           ': ')
        if 0 <= int(sensor) <= 3:
            break
        else:
            sensor = input('Для поиска заметки нажмите 1\n'
                           'Для добавления заметки нажмите 2\n'
                           'Для показа всех заметок нажмите 3\n'
                           ': ')
    return int(sensor)