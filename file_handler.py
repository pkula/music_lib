def file_read(filename = 'text_albums_data.txt'):
    with open(filename , 'r') as file:
        list_of_lines = file.readlines()
        new_list_of_lines = []
        for list in list_of_lines:
            list = list[0:-1]
            list = list.split(',')
            new_list_of_lines = new_list_of_lines + [list]            
    return new_list_of_lines



