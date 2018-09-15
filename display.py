import file_handler
from prettytable import PrettyTable


def display_the_menu_options():
    print("Press '1' to view all albums")
    print("Press '2' to find an album by genre")
    print("Press '3' to find an album by length")
    print("Press '4' to find an album by artist")
    print("Press '5' to find an album by name")
    print("Press '6' to find the longest album")
    print("Press '7' to find the shortest album")
    print("Press '8' to add new album")
    print("Press '9' to view albums from a certain year")
    print("Press '10' to view albums to a certain year")
    print("Press '11' to save all albums to external file")
    print("Press '12' to delete number")
    print("Press '13' to organise")
    print("Press '14' to change record")
    print("Press '0' to quit")


def display(new_list_of_lines=file_handler.file_read()):  # 1. view_all_albums
    table_for_display = PrettyTable()
    table_for_display.field_names = ["ID", "Artist", "Album", "Year", "Genre", "Length"]
    table_for_display.align["Artist"] = "l"
    table_for_display.align["Album"] = "l"
    table_for_display.align["Year"] = "l"
    table_for_display.align["Year"] = "l"
    table_for_display.align["Genre"] = "l"
    table_for_display.align["Length"] = "l"
    n = 1
    for artist, album, year, genre, length in new_list_of_lines:
        table_for_display.add_row([n, artist, album, year, genre, length])
        n += 1
    print(table_for_display.get_string(title="Music Library"))
