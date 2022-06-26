"""
28. Write a Python program to clear the screen or terminal.
"""
"""
solved by : Zeeshan Sarwar
"""
import os
import time


def clear_scr():
    """
    Function To Clear the screen or terminal in windows
    :return: clear the screen
    """
    return os.system('cls')


def clear_screen():
    """
        Function To Clear the screen or terminal for multiple platforms
        :return: clear the screen
        """
    # for windows
    if os.name == 'nt':
        _ = os.system('cls')

    # for mac and linux
    else:
        _ = os.system('clear')


print("Hello, World!!\n"*5)

time.sleep(5)

clear_scr()
