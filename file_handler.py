def file_read(filename = 'text_albums_data.txt'):
    with open(filename , 'r') as file:
        list_of_lines = file.readlines()
        new_list_of_lines = []
        for list in list_of_lines:
            list = list[0:-1]
            list = list.split(',')
            new_list_of_lines = new_list_of_lines + [list]            
    return new_list_of_lines



def write_new_record( new_record , filename = 'text_albums_data.tx'):
    # new record jest tablica
    string_new_record = ''
    for i in new_record:
        string_new_record = string_new_record + ',' + i
    string_new_record = string_new_record[1:]
    with open(filename , 'a+') as file:
        file.write('\n')
        file.write(string_new_record)
    return 0




def file_read_lines(filename = 'text_albums_data.txt'):
    with open(filename , 'r') as file:
        list_of_lines = file.readlines()
        new_list_of_lines = []
        for list in list_of_lines:
            list = list[0:-1]
            new_list_of_lines = new_list_of_lines + [list]            
    return new_list_of_lines
