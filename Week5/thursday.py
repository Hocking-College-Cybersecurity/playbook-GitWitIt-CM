import sys


people = {"Jerry": 15, "Tom":6, "Bob":12}

with open(example.txt) as text_stream:
    for my_line, next_line in zip(text_stream, text_stream):
        if my_line.startswith("Name: "):
            print(my_line.split()[-1])
            print(next_line.split()[-1])
            people(my_line.split()[-1]) = next_line.split()[-1]
            