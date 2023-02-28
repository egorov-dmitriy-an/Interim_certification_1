from datetime import datetime as dt

def request_note_logger(data, sensor):
    time = dt.now().strftime('%H:%M')
    if sensor == 2:
        with open('log_seminar.csv', 'a', encoding="utf-8") as file:
            file.write(time + ';Add note;\n')
    elif sensor == 1:
        with open('log_seminar.csv', 'a', encoding="utf-8") as file:
            file.write(time + ';Find note;\n')
    elif sensor == 3:
        with open('log_seminar.csv', 'a', encoding="utf-8") as file:
            file.write(time + ';Show all notes;\n')
