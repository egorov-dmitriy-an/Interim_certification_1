def save_note(guide_file, new_note):
    with open(guide_file, 'a', encoding="utf-8") as file:
        file.write('\n{};{};{};{}'
                   .format(new_note[0], new_note[1], new_note[2], new_note[3]))
    print(f'Добавлена заметка: {new_note}')


def del_note(guide_file, number_line):
    with open(guide_file, 'r', encoding="utf-8") as file:
        del_line = file.readlines()

    with open(guide_file, 'r', encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            else:
                arr_line = line.split(';')
                if (number_line == arr_line[0]):
                    del_li = line
                    break
    with open(guide_file, 'w', encoding="utf-8") as file:
        for line_note in del_line:
            if line_note != del_li:
                file.write(line_note)
        arr_line = del_li.split(';')
        print("Удалена заметка: ")
        print("Id: " + arr_line[0] + "\n" +
              "Заголовок: " + arr_line[1] + "\n" +
              "Тело: " + arr_line[2] + "\n" +
              "Дата изменения: " + arr_line[3] + "\n")