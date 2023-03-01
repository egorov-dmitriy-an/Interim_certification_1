def save_note(guide_file, new_note):
    with open(guide_file, 'a', encoding="utf-8") as file:
        file.write('\n{};{};{};{}'
                   .format(new_note[0], new_note[1], new_note[2], new_note[3]))
    print(f'Добавлена заметка: {new_note}')


def del_note(guide_file, number_line):
    with open(guide_file, 'r', encoding="utf-8") as file:
        while True:
            line = file.readline()
            if not line:
                break
            else:
                arr_line = line.split(';')
                del_line = line
                if (number_line == arr_line[0]):
                    break
    return del_line

