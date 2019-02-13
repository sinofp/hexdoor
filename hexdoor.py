#!/usr/bin/env python
import fire
import string
from colorama import Fore, Style 

HEADER = '┌────────┬─────────────────────────┬─────────────────────────┬────────┬────────┐'
FOOTER = '└────────┴─────────────────────────┴─────────────────────────┴────────┴────────┘'
LINE_FORMATTER = '│' + Style.DIM + '{:08x}' + Style.RESET_ALL + '│ {}' + Style.RESET_ALL + '│{}' + Style.RESET_ALL + '│'

def hexstr2chr(s: str) -> chr:
    if '  ' == s:
        # is padding
        return '尾'
    else:
        return chr(int(s, 16))

def colored(s: str) -> str:
    ch = hexstr2chr(s)
    if '尾' == ch:
        # pad the last line
        return '  ', ' '
    elif '\x00' == ch:
        # NULL bytes
        return Fore.RESET + Style.DIM + s + Style.RESET_ALL, Fore.RESET + Style.DIM + '0' + Style.RESET_ALL
    elif ch in string.ascii_letters + string.digits + string.punctuation:
        # printable ASCII characters
        return Fore.CYAN + s, Fore.CYAN + ch
    elif ch in string.whitespace:
        # ASCII whitespace characters
        return Fore.GREEN + s, ' ' if ' ' == ch else Fore.GREEN + '_'
    elif int(s, 16) in range(128):
        # other ASCII characters
        return Fore.MAGENTA + s, Fore.MAGENTA + '•'
    else:
        # non-ASCII characters
        return Fore.YELLOW + s, Fore.YELLOW + '×'

def hexhandle(file_name):
    '''print hex-string and ascii characters of given file'''
    print(HEADER)
    with open(file_name, 'rb') as f_obj:
        row = 0
        line = f_obj.read(16)
        while line:
            line_hex = line.hex().ljust(32)

            hexbytes = ''
            printable = ''
            for i in range(0, len(line_hex), 2):
                hbyte, abyte = colored(line_hex[i:i+2])
                hexbytes += hbyte + ' ' if i != 14 else hbyte + Style.RESET_ALL + ' ┊ '
                printable += abyte if i != 14 else abyte + Style.RESET_ALL + '┊'

            print(LINE_FORMATTER.format(row, hexbytes, printable))
            
            row += 0x10
            line = f_obj.read(16)
    print(FOOTER)

if __name__ == '__main__':
    fire.Fire(hexhandle)