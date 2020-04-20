# -*- coding: utf-8 -*

import os
import sys
import time
import subprocess


if __name__ == "__main__":
    encrypted_text = ''
    try:
        with open("encrypted.txt", "r") as f:
            encrypted_text = f.read()
            print(encrypted_text)
    except IOError, e:
        print("encrypted.txt doesn't exist")
        exit(-1)

    frequencies = [0] * 26
    a_ascii = ord('a')
    for c in encrypted_text:
        c = c.lower()
        index = ord(c) - a_ascii
        if index >= 0 and index <= 25:
            frequencies[index] += 1

    for i in range(26):
        cur_char = chr(a_ascii + i)
        print(cur_char, frequencies[i])


