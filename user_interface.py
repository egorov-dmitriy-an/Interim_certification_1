import logger as log
import data_provider as dt_prov
import check_module as check_mod
import add_note as add_note
import print_note


def button_click():
    while True:
        number = check_mod.check_start()
        note = dt_prov.get_note(number)
        log.request_note_logger(number)
        if number == 0:
            print_note.show_0()
            break
        elif number == 1:
            print_note.show_1(note)
            number_info = (input('Введите id заметки: '))
            number2 = check_mod.check_actions(number_info)
            if number == 7:
                print_note.show_0()
                break
            elif number2 == 4:
                add_note.del_note('guide.txt', number_info)
            elif number2 == 5:
                print("Здесь будет редактирование")
            elif number2 == 6:
                print_note.show_note_id(number_info)

        elif number == 2:
            add_note.save_note('guide.txt', note)
        elif number == 3:
            print_note.show_3()
