def find_text(text, heading):
    head = heading.split(';')
    if text in head[0]:
        return True