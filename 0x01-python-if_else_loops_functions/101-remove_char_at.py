#!/usr/bin/python3

def remove_char_at(str, n):
    if n < 0:
        return str
    x = 0
    str_copy = ""
    for element in str:
        if x == n:
            x += 1
            continue
        str_copy += str[x]
        x += 1
    return str_copy
