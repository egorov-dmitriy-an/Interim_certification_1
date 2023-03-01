import checking_file as check_fl

def show_0():
    print('Спасибо, до свидания!')

def show_1(note):
    notes_list = check_fl.check_file('guide.txt', note)
    if len(notes_list) == 0:
        print('')
    else:
        print()
        print('Результат поиска: ')
        print('id' + "\t" + 'Заголовок')
        print('--' + "\t" + '---------')

        for i in range(0, len(notes_list)):
            temp = notes_list[i].split(';')
            print(temp[0] + "\t" + temp[1])
        print()

def show_3():
    with open('guide.txt', 'r', encoding="utf-8") as file:
        print('Все заметки')
        print('id' + "\t" + 'Заголовок')
        print('--' + "\t" + '---------')
        while True:
            line = file.readline()
            if not line:
                break
            else:
                arr_line = line.split(';')
                print(arr_line[0] + "\t" + arr_line[1])

def show_note_id(id_num):
    with open('guide.txt', 'r', encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            else:
                arr_line = line.split(';')
                if (id_num == arr_line[0]):
                    print("Id: " + arr_line[0] + "\n" +
                          "Заголовок: " + arr_line[1] + "\n" +
                          "Тело: " + arr_line[2] + "\n" +
                          "Дата изменения: " + arr_line[3] + "\n")