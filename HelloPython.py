# CURRENT BUILD: 25/11/2020 @ 12:15PM

import datetime


def print_greeting():
    print("Hello world!")


def print_time():
    now = datetime.datetime.now()

    time = now.strftime("%A, %d-%m-%Y : %H:%M")

    print("Current date and time is", time)


def print_success():
    x = 1
    y = 2
    if x + y == 3:
        print("Success!")


def print_failure():
    rpint(test)


def main():
    print_greeting()
    print_time()
    print_success()
    print_failure()


main()