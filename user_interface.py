import logger as log
import data_provider as dt_prov
import check_module as check_mod
import checking_file as check_fl
import add_note as add_note
import check_print as check_pr

def button_click():
    print()
    number = (input('Для поиска заметки нажмите 1\n'
                    'Для добавления заметки нажмите 2\n'
                    'Для показа всех заметок нажмите 3\n'
                    ': '))
    number = check_mod.check(number)

    note = dt_prov.get_note(number)

    log.request_note_logger(note, number)

    if number == 1:
        notes_list = check_fl.check_file('guide.txt', note)
        if len(notes_list) == 0:
            print('Такой заметки нет')
        else:
            mod = (input('В каком формате вывести данные: 1 - столбец, 2 - строка: '))
            mod = check_pr.check(mod)
            
            print()
            print('Искомая заметка:')
            if mod == 1:
                for i in range(0, len(notes_list)):
                    temp = notes_list[i].split(';')
                    for j in range(0, 4):
                        print(temp[j])
                print()
            else:
                for i in range(0, len(notes_list)):
                    temp = notes_list[i].split(';')
                    for j in range(0, 4):
                        if j != 3:
                            print(temp[j], end = ', ')
                        else:
                            print(temp[j])
                print()
    elif number == 2:
        add_note.save_note('guide.txt', note)
    elif number == 3:
        with open('guide.txt', 'r') as file:
            while True:
                line = file.readline()
                if not line:
                    break
                else:
                    print(line)