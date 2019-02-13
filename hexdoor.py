#!/usr/bin/env python
import fire
import string

HEADER = '┌────────┬─────────────────────────┬─────────────────────────┬────────┬────────┐'
FOOTER = '└────────┴─────────────────────────┴─────────────────────────┴────────┴────────┘'
LINE_FORMATTER = '│{:08x}│ {}┊ {}│{}│{}│'

def isprint(c: chr) -> bool:
    '''相当与C语言里的isprint'''
    return c in string.ascii_letters + string.digits + string.punctuation + ' '    

def hexhandle(file_name):
    '''打印指定文件的16进制、可打印字符'''
    print(HEADER)
    with open(file_name, 'rb') as f_obj:
        row = 0
        line = f_obj.read(16)
        while line:
            line_hex = line.hex().ljust(32)
            line_char = line.ljust(16)
            print(LINE_FORMATTER.format(
                row,
                ''.join([line_hex[i:i+2]+' ' for i in range(0, 16, 2)]),
                ''.join([line_hex[i:i+2]+' ' for i in range(16, 32, 2)]),
                ''.join([chr(i) if isprint(chr(i)) else '×' for i in line_char[:8]]),
                ''.join([chr(i) if isprint(chr(i)) else '×' for i in line_char[8:]])
                ))
            row += 0x10
            line = f_obj.read(16)
    print(FOOTER)

if __name__ == '__main__':
    fire.Fire(hexhandle)