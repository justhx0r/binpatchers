#!/usr/bin/env python3
import argparse
import random
import string
import os

def patch_upx(file_path):
    with open(file_path, 'rb') as file:
        content = file.read()

    strings_to_patch = [
        b'$Info: This file is packed with the UPX executable packer http://upx.sf.net $',
        b'$Id: UPX 4.30 Copyright (C) 1996-2023 the UPX Team. All Rights Reserved. $',
        b'UPX!',
        b'UPX0',
        b'UPX1',
        b'UPX2',
        b'UPX3',
        b"UPX"
    ]

    for string_to_patch in strings_to_patch:
        replacement = bytes(''.join(random.choice(string.ascii_letters) for _ in range(len(string_to_patch))), 'utf-8')
        content = content.replace(string_to_patch, replacement)

    with open(file_path, 'wb') as file:
        file.write(content)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Patch out references to UPX in a binary file.')
    parser.add_argument('-i', '--input', help='Path to the input binary file', required=True)
    args = parser.parse_args()

    patch_upx(args.input)
