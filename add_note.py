def save_note(guide_file, new_note):
    with open(guide_file, 'a', encoding="utf-8") as file:
        file.write('\n{};{};{};{}'
                   .format(new_note[0], new_note[1], new_note[2], new_note[3]))
    print(f'Добавлена заметка: {new_note}')

    # file.write(', '.join([name, surname, telephone, description]) + \n) - вариант записи в файл