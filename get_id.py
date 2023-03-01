def collecting_id(guide_base):
    with open(guide_base, 'r', encoding="utf-8") as file:
        id_list = []
        while True:
            line = file.readline()
            if not line:
                break
            else:
                temp_list = line.split(';')
                id_list.append(int(temp_list[0]))
    return id_list

def equating_id(coll_id):
    new_id = 1
    for i in range(0, len(coll_id)):
        if new_id in coll_id:
            new_id += 1
        else: break
    return new_id