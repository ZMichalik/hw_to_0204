#!/usr/local/bin/python
# coding: latin-1

"""
Task 1
You have two text files. Find out if their lines match. If
they don?t, print the mismatched line from each file.
"""

def get_lines(name_file):
    with open(name_file) as f_handl:
        radky = f_handl.readlines()
        #print(radky)

    return radky

lines_file1 = get_lines("text1.txt")
lines_file2 = get_lines("text2.txt")

if lines_file1 == lines_file2:
    print("Textove soubory jsou shodne.")

else:
    print("textove soubory jsou odlisne")
    f_handl = open("text3.txt", "w+")
    f_handl.writelines(lines_file1)
    f_handl.writelines(lines_file2)
    print(f_handl)
    f_handl.close()





"""

lines_file1 = get_lines("text1.txt")
lines_file2 = get_lines("text2.txt")
lines_file3 = get_lines("text1.txt")
lines_file4 = get_lines("text2.txt")

"""
