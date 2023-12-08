#!/usr/bin/env python3
import re
import random
import string
import argparse

def generate_random_string(length):
    return ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))

def patch_out_nim(file_content):
    # Define a bytes regular expression pattern to match strings ending with b".nim" or containing @[whatever].nim
    pattern = re.compile(rb'(?<!\S)\w+\.nim\b|\b@[^\s]*\.nim\b|\b[Nn]im\w*\b')

    # Find all matches in the file content
    matches = pattern.findall(file_content)

    # Replace each match with a random string of the same length
    for match in set(matches):  # Using set to avoid replacing the same string with different random strings
        replacement = generate_random_string(len(match))
        file_content = re.sub(re.escape(match), replacement.encode(), file_content)

    return file_content

def patch_out_gcc(file_content):
    # Define a bytes regular expression pattern to match strings starting with b"GCC"
    pattern = re.compile(rb'\bGCC[^\n]*\n')

    # Find all matches in the file content
    matches = pattern.findall(file_content)

    # Replace each match with a random string of the same length
    for match in set(matches):  # Using set to avoid replacing the same string with different random strings
        replacement = generate_random_string(len(match))
        file_content = re.sub(re.escape(match), replacement.encode(), file_content)

    return file_content

def patch_out_upx(file_content):
    # Define a bytes regular expression pattern to match strings starting with b"UPX"
    pattern = re.compile(rb'\bUPX[^\n]*\n')

    # Find all matches in the file content
    matches = pattern.findall(file_content)

    # Replace each match with a random string of the same length
    for match in set(matches):  # Using set to avoid replacing the same string with different random strings
        replacement = generate_random_string(len(match))
        file_content = re.sub(re.escape(match), replacement.encode(), file_content)

    return file_content

def patch_out_at(file_content):
    # Define a bytes regular expression pattern to match strings starting with b"@"
    pattern = re.compile(rb'\b@[^\s]*\b')

    # Find all matches in the file content
    matches = pattern.findall(file_content)

    # Replace each match with a random string of the same length
    for match in set(matches):  # Using set to avoid replacing the same string with different random strings
        replacement = generate_random_string(len(match))
        file_content = re.sub(re.escape(match), replacement.encode(), file_content)

    return file_content

def patch_out_error(file_content):
    # Define a bytes regular expression pattern to match strings containing b"error"
    pattern = re.compile(rb'\b.*error.*\b')

    # Find all matches in the file content
    matches = pattern.findall(file_content)

    # Replace each match with a random string of the same length
    for match in set(matches):  # Using set to avoid replacing the same string with different random strings
        replacement = generate_random_string(len(match))
        file_content = re.sub(re.escape(match), replacement.encode(), file_content)

    return file_content

def main():
    p = argparse.ArgumentParser()
    p.add_argument("-i", "--input", help="Input file", required=True)
    a = p.parse_args()

    input_file_path = a.input  # Update with the actual path to your file

    with open(input_file_path, 'rb') as file:
        file_content = file.read()

    # Patch out Nim strings
    file_content = patch_out_nim(file_content)

    # Patch out GCC strings
    file_content = patch_out_gcc(file_content)

    # Patch out UPX strings
    file_content = patch_out_upx(file_content)

    # Patch out @ strings
    file_content = patch_out_at(file_content)

    # Patch out strings containing "error"
    file_content = patch_out_error(file_content)

    # Write the modified content back to the file
    with open(input_file_path, 'wb') as file:
        file.write(file_content)

if __name__ == "__main__":
    main()
