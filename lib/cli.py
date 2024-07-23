# lib/cli.py test2

import time

from helpers import (
    greeting,
    main_menu
)

def main():
    greeting()
    time.sleep(1)
    main_menu()

if __name__ == "__main__":
    main()
