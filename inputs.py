def get_lenght():
    while True:
        try:
            min = int(input('Enter minutes\n'))
            break
        except ValueError:
            print("Some bad input in here")
    while True:
        try:
            sec = int(input('Enter seconds\n'))
            break
        except ValueError:
            print("Nope, try again")
    min = str(min + sec//59)
    sec = str(sec % 60)
    time = min + ':' + (2-len(sec))*'0' + sec
    return time


def get_artist():
    artist_input = input("What artist?\n").title()
    return artist_input


def get_album():
    album_input = input("What album?\n").title()
    return album_input


def get_year():
    while 1:
        try:
            year = int(input('Enter a year\n'))
            return year
        except ValueError:
            print("It's a very bad year")


def get_genre():
    genre_input = input("What genre?\n").lower()
    return genre_input



def get_number():
    while 1:
        try:
            number = int(input('Enter a number\n'))
            return number
        except ValueError:
            print("It's not a number")
