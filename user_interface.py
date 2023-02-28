import logger as log
import data_provider as dt_prov
import check_module as check_mod
import checking_file as check_fl
import add_note as add_note


def button_click():
    while True:
        print()
        number = (input('Для поиска заметки нажмите 1\n'
                        'Для добавления заметки нажмите 2\n'
                        'Для показа всех заметок нажмите 3\n'
                        'Для выхода нажмите 0\n'
                        ': '))
        number = check_mod.check(number)
        note = dt_prov.get_note(number)

        log.request_note_logger(note, number)

        if number == 0:
            print('Спасибо, до свидания!')
            break
        elif number == 1:
            notes_list = check_fl.check_file('guide.txt', note)
            if len(notes_list) == 0:
                print('Такой заметки нет')
            else:
                print()
                print('Результат поиска: ')
                print('id' + "\t" + 'Heading')

                for i in range(0, len(notes_list)):
                    temp = notes_list[i].split(';')
                    print(temp[0] + "\t" + temp[1])
                print()

        elif number == 2:
            add_note.save_note('guide.txt', note)
        elif number == 3:
            with open('guide.txt', 'r', encoding="utf-8") as file:
                print('Все заметки')
                print('id' + "\t" + 'Heading')
                while True:
                    line = file.readline()
                    if not line:
                        break
                    else:
                        arr_line = line.split(';')
                        print(arr_line[0] + "\t" + arr_line[1])
