import os
import time

def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')

def pause(seconds: float):
    time.sleep(seconds)