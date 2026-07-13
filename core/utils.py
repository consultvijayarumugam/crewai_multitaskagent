from datetime import datetime


def current_time():

    return datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")


def separator(length=70):

    return "=" * length