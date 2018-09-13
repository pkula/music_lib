def do_option(your_input):
    if your_input == '1':
        fun_1()                           # tylko wyswietla nazwy albumow

    elif your_input == '2':
        fun_2()

    elif your_input == '3':
        albums_from_given_time_range()   

    elif your_input == '4':
        find_shortest_or_longest_album(list_with_records)

    elif your_input == '5':
        fun_5()

    elif your_input == '6':
        fun_6()

    elif your_input == '7':
        fun_7()                         #tylko wyswietla tabele ze wszystkimi danymi

    elif your_input == '8':
        fun_4()

    elif your_input == '9':
        add_album()

    elif your_input == '10':
        edit_album()

    elif your_input == '11':
        fun_7()




def add_album():

    artist_name = get_artist_name()
    album_name = get_album_name()
    release_year = get_release_year()                 # te funkcje maja byc zdefiniowane w inputs
    genre = get_genre()
    length = get_length()
    new_record = [artist_name , album_name , release_year , genre , length]
    write_new_record(new_record)



def edit_album():
    pass






def find_shortest_album(list_with_records):
    shortest = [[1000000000000,0]]                               #i zwraca najkrocej trwajacy record
    new_list_with_records = []
    for album in list_with_records:
        new_list_with_records=new_list_with_records+[album+[[int(album[4][:-3]),int(album[4][-2:])]]]
    for time in new_list_with_records:
        if time[-1][0] < shortest[-1][0]:
            shortest = time
        elif time[-1][0] == shortest[-1][0]:
            if time[-1][1] < shortest[-1][1]:
                shortest = time
    return(shortest[:-1])

            
    



def find_longest_album(list_with_records):          #ta funkcja przyjmuje tablice z recordami
    longest = [[0,0]]                               #i zwraca najdluzej trwajacy record
    new_list_with_records = []
    for album in list_with_records:
        new_list_with_records=new_list_with_records+[album+[[int(album[4][:-3]),int(album[4][-2:])]]]
    for time in new_list_with_records:
        if time[-1][0] > longest[-1][0]:
            longest = time
        elif time[-1][0] == longest[-1][0]:
            if time[-1][1] > longest[-1][1]:
                longest = time
    return(longest[:-1])


















def from_time(list_with_records,time):          
    new_list_with_records = []
    for album in list_with_records:
        new_list_with_records=new_list_with_records+[album+[[int(album[4][:-3]),int(album[4][-2:])]]]
    x = []
    for record in new_list_with_records:
        if record[-1][0] > time[0] or record[-1][0] == time[0] and record[-1][1] >= time[1]:
            x = x + [record]
    return(x)


def to_time(list_with_records,time):             
    new_list_with_records = []
    for album in list_with_records:
        new_list_with_records=new_list_with_records+[album+[[int(album[4][:-3]),int(album[4][-2:])]]]
    x = []
    for record in new_list_with_records:
        if record[-1][0] < time[0] or record[-1][0] == time[0] and record[-1][1] <= time[1]:
            x = x + [record]
    return(x)


a = [['Pink Floyd','The Dark Side Of The Moon','1973','progressive rock','142:20'],['Britney Spears','Baby One More Time','1999','pop','43:20'],['The Beatles','Revolver','1966','rock','143:43']]
print(from_time(a,[142,20]))