from datetime import datetime as dt

def request_note_logger(data, sensor):
    time = dt.now().strftime('%H:%M')
    if sensor == 2:
        with open('log_seminar.csv', 'a') as file:
            file.write('{};Add note;{}\n'
                       .format(time, data))
    elif sensor == 1:
        with open('log_seminar.csv', 'a') as file:
            file.write('{};Find note;{}\n'
                       .format(time, data))