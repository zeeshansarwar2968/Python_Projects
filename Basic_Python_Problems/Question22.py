import os
import time

def clear_scr():
    """
    Function To Clear the screen or terminal
    :return: clear the screen
    """
    return os.system('cls')


def clear1():
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = os.system('clear')

print("Hello, World!!\n"*5)

time.sleep(2)


os.system('clear')
