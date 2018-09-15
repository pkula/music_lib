import display
import music_reports
import file_handler
import display
# zmienic nazwy funkcji pod if


def main():

    choice = None
    while choice != "0":
        display.display_the_menu_options()
        choice = input('Choose Option\n')
        music_reports.define_user_input(choice)


main()
