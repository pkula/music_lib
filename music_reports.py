import display
import file_handler
import inputs


def find_shortest_album(list_with_records):
    shortest = [[1000000000000, 0]]                               # i zwraca najkrocej trwajacy record
    new_list_with_records = []
    try:
        for album in list_with_records:
            new_list_with_records = new_list_with_records+[album+[[int(album[4][:-3]), int(album[4][-2:])]]]
    except ValueError:
        for time in new_list_with_records:
            if time[-1][0] < shortest[-1][0]:
                shortest = time
            elif time[-1][0] == shortest[-1][0]:
                if time[-1][1] < shortest[-1][1]:
                    shortest = time
        return(shortest[:-1])


def find_longest_album(list_with_records):          # ta funkcja przyjmuje tablice z recordami
    longest = [[0, 0]]                               # i zwraca najdluzej trwajacy record
    new_list_with_records = []
    try:
        for album in list_with_records:
            new_list_with_records = new_list_with_records+[album+[[int(album[4][:-3]), int(album[4][-2:])]]]
    except ValueError:
        for time in new_list_with_records:
            if time[-1][0] > longest[-1][0]:
                longest = time
            elif time[-1][0] == longest[-1][0]:
                if time[-1][1] > longest[-1][1]:
                    longest = time
        return(longest[:-1])


def from_time(list_with_records, time):
    new_list_with_records = []
    for album in list_with_records:
        new_list_with_records = new_list_with_records+[album+[[int(album[4][:-3]), int(album[4][-2:])]]]
    x = []
    for record in new_list_with_records:
        if record[-1][0] > time[0] or record[-1][0] == time[0] and record[-1][1] >= time[1]:
            x = x + [record[:-1]]
    return(x)


def to_time(list_with_records, time):
    new_list_with_records = []
    for album in list_with_records:
        new_list_with_records = new_list_with_records+[album+[[int(album[4][:-3]), int(album[4][-2:])]]]
    x = []
    for record in new_list_with_records:
        if record[-1][0] < time[0] or record[-1][0] == time[0] and record[-1][1] <= time[1]:
            x = x + [record[:-1]]
    return(x)


def from_date(list, year_int):
        from_date_records = []
        for i in list:
            if year_int >= int(i[-3]):
                from_date_records = from_date_records + [i]
        return from_date_records


def to_date(list, year_int):
        to_date_records = []
        for i in list:
            if year_int <= int(i[-3]):
                to_date_records = to_date_records + [i]
        return to_date_records


def find_by_genre(genre, table_by_genre):
    genre_records = []
    for i in table_by_genre:
        if genre == i[-2]:
            genre_records = genre_records + [i]
    return genre_records


def display_by_length(length, table_by_length):  # 4. find_by_length
    albums_by_length = []
    for i in table_by_length:
        if length == i[-1]:
            albums_by_length = albums_by_length + [i]
    return albums_by_length


def display_by_artist(artist, table_by_artist):  # 5. find_by_artist
    albums_by_artist = []
    for i in table_by_artist:
        if artist == i[0]:
            albums_by_artist = albums_by_artist + [i]
    return albums_by_artist


def display_by_album_name(name_of_album, table_by_name):  # 6. find_by_album_name
    albums_by_name = []
    for i in table_by_name:
        if name_of_album == i[1]:
            albums_by_name = albums_by_name + [i]
    return albums_by_name


def wait():
    input("Press 'Enter' to continue\n")


def define_user_input(user_input):
    if user_input == "1":
        display.display(file_handler.file_read())
        wait()


def delete_record(list,number_of_list):
    new_list = list[:number_of_list] + list[number_of_list +1:]
    return new_list
























def define_user_input(user_input):
    if user_input == "1":
        display.display(file_handler.file_read())
        wait()



    elif user_input == "2":
        genre = inputs.get_genre()
        display.display(find_by_genre(genre, file_handler.file_read()))
        wait()

    elif user_input == "3":
        time = inputs.get_lenght()
        display.display(display_by_length(time, file_handler.file_read()))
        wait()

    elif user_input == "4":
        artist = inputs.get_artist()
        display.display(display_by_artist(artist, file_handler.file_read()))
        wait()

    elif user_input == "5":
        album = inputs.get_album()
        display.display(display_by_album_name(album, file_handler.file_read()))
        wait()

    elif user_input == "6":
        display.display([find_longest_album(file_handler.file_read())])
        wait()

    elif user_input == "7":
        display.display([find_shortest_album(file_handler.file_read())])
        wait()

    elif user_input == "8":
        artist_name = inputs.get_artist()
        album_name = inputs.get_album()
        release_year = inputs.get_year()
        release_year = str(release_year)
        genre = inputs.get_genre()
        length = inputs.get_lenght()
        record = [artist_name, album_name, release_year, genre, length]
        print(record)
        file_handler.write_new_record(record)
        wait()

    elif user_input == "9":
        year = inputs.get_year()
        display.display(to_date(file_handler.file_read(), year))
        wait()

    elif user_input == "10":
        year = inputs.get_year()
        display.display(from_date(file_handler.file_read(), year))
        wait()

    elif user_input == "11":
        file_name = input('Enter the name of your file:\n')
        file = file_handler.file_read()
        file_handler.write_all(file, file_name)
        print("\nSuccessfully created.\n")
        wait()

    elif user_input == "12":      
        display.display(file_handler.file_read())
        print('Wich number of list do you like to delete')
        number_to_delete = inputs.get_number() - 1
        file = file_handler.file_read('text_albums_data.txt')
        file = delete_record(file,number_to_delete)
        file_handler.write_all(file, filename='text_albums_data.txt')
        print("\nSuccessfully delete.\n")
        wait()
