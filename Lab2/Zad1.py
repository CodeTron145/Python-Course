import sys
import os

def parser(argv):
    reader = open(argv);
    for amount_lines, line in enumerate(reader):
        continue;
    print("Amount of lines: ", amount_lines)
    print("Amount of bytes: ", os.path.getsize(argv))

    num_words = 0;
    with open(argv, 'r') as f:
        for line in f:
            words = line.split();
            num_words += len(words)
    print("Number of words: ", num_words)
    print("Amount of letters in longest word: ", len(max(open(argv), key=len)))

if sys.argv[1]:
    parser(sys.argv[1]);
else:
    print("You forgot to type filename!");