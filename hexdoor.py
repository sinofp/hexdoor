#!/usr/bin/env python
import fire
import string
from colorama import Fore, Style 

HEADER = '┌────────┬─────────────────────────┬─────────────────────────┬────────┬────────┐'
FOOTER = '└────────┴─────────────────────────┴─────────────────────────┴────────┴────────┘'
LINE_FORMATTER = '│' + Style.DIM + '{:08x}' + Style.RESET_ALL + '│ {}' + Style.RESET_ALL + '│{}' + Style.RESET_ALL + '│'

def hexstr2chr(s: str) -> chr:
    return chr(int(s, 16))

def hexstr2int(s: str) -> int:
    if '  ' == s:
        return 256
    else:
        return int(s, 16)

def stripandrjust(s: str) -> str:
    return s[2:].rjust(2, '0')

def colored(s: str) -> str:
    ch = hexstr2chr(s)
    if '\x00' == ch:
        # NULL bytes
        return Fore.RESET + Style.DIM + stripandrjust(s) + Style.RESET_ALL, Fore.RESET + Style.DIM + '0' + Style.RESET_ALL
    elif ch in string.ascii_letters + string.digits + string.punctuation:
        # printable ASCII characters
        return Fore.CYAN + stripandrjust(s), Fore.CYAN + ch
    elif ch in string.whitespace:
        # ASCII whitespace characters
        return Fore.GREEN + stripandrjust(s), ' ' if ' ' == ch else Fore.GREEN + '_'
    elif int(s, 16) in range(128):
        # other ASCII characters
        return Fore.MAGENTA + stripandrjust(s), Fore.MAGENTA + '•'
    else:
        # non-ASCII characters
        return Fore.YELLOW + stripandrjust(s), Fore.YELLOW + '×'

def hexhandle(file_name):
    '''print hex-string and ascii characters of given file'''
    
    cache = [colored(str(hex(b))) for b in range(256)] #0x00 - 0xff
    cache.append(('  ', ' ')) # padding for the last line

    print(HEADER)
    with open(file_name, 'rb') as f_obj:
        row = 0
        line = f_obj.read(16)
        while line:
            line_hex = line.hex().ljust(32)

            hexbytes = ''
            printable = ''
            for i in range(0, len(line_hex), 2):
                hbyte, abyte = cache[hexstr2int(line_hex[i:i+2])]
                hexbytes += hbyte + ' ' if i != 14 else hbyte + Style.RESET_ALL + ' ┊ '
                printable += abyte if i != 14 else abyte + Style.RESET_ALL + '┊'

            print(LINE_FORMATTER.format(row, hexbytes, printable))
            
            row += 0x10
            line = f_obj.read(16)
    print(FOOTER)

if __name__ == '__main__':
    fire.Fire(hexhandle)