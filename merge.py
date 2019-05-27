import os
from os.path import isfile, join

current_path = os.path.dirname(os.path.abspath(__file__))
notes_path = current_path + '/notes'
final_path = current_path + '/notes/notes.md'

if os.path.isfile(final_path):
    os.remove(final_path)
files = [notes_path + "/" + f for f in os.listdir(notes_path) if isfile(join(notes_path, f))]

if files.__len__ != 0:
    last_file = files[files.__len__() - 1]
    with open(final_path, "w") as outfile:
        for fname in files:
            with open(fname) as infile: 
                for line in infile:
                    outfile.write(line)
                if fname != last_file:
                    outfile.write("\n\n")
