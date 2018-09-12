def file_read(filename = 'text_albums_data.txt'):
    with open(filename, 'r') as file:
        list_of_lines = file.readlines()
        print(list_of_lines)
    return 0


file_read()