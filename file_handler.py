def file_read(filename='text_albums_data.txt'):
    with open(filename, 'r') as file:
        list_of_lines = file.readlines()
        new_list_of_lines = []
        for list in list_of_lines:
            list = list[0:-1]
            list = list.split(',')
            new_list_of_lines = new_list_of_lines + [list]
    return new_list_of_lines


def write_new_record(new_record, filename='text_albums_data.txt'):
    string_new_record = ''
    for i in new_record:
        string_new_record = string_new_record + ',' + i
    string_new_record = string_new_record[1:]
    with open(filename, 'a+') as file:
        file.write("\n" + string_new_record)


def write_all(list_of_records, filename='plo.txt'):    # cos tu jest nie tak
    new_records = []
    for album in list_of_records:
        new_records = new_records + [album[0] + ',' + album[1] + ',' + album[2] + ',' + album[3] + ',' + album[4]]
    with open(filename, 'w+') as file:
        file.write(new_records[0])
    with open(filename, 'a+') as file:
        for album in range(1, len(new_records)):
            file.write('\n')
            file.write(new_records[album])
