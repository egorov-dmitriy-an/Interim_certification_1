def find_text(text, heading):
    head = heading.split(';')
    if text in head[1]:
        return True