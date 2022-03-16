#!/usr/bin/env python3

import curses


def main(stdscr):
    mode = 0

    while True:
        char = stdscr.getch()
        if char == 58:  # ':' command mode
            mode = 0
        # elif char == 27:  # esc: exit insert mode
        #     mode = 0
        elif char == 105:  # enter: insert mode
            mode = 1

        if mode == 0:
            if char == 113:
                return 'quit'


if __name__ == "__main__":
    print(curses.wrapper(main))
