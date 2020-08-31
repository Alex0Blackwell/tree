#!/usr/bin/python3

from pathlib import Path
from termcolor import cprint
import os
import sys

class Tree():
    """docstring for Tree."""

    def __init__(self, showAll):
        self.currPath = Path(os.getcwd())
        self.showAll = showAll
        cprint((self.currPath.name), "blue")


    def print(self, indent = 4):
        allFiles = []
        for file in self.currPath.iterdir():
            if(file.is_dir()):
                if( not(file.name[0] == '.' and not self.showAll)):
                    spaces = ""
                    for i in range(indent-4):
                        if(i % 4 == 0):
                            spaces += '|'
                        else:
                            spaces += ' '

                    formatIndent = spaces + '\\' + '_' * 4

                    cprint(formatIndent, "white", end='')
                    cprint((file.name + '/'), "blue")

                    self.currPath = file;
                    self.print(indent + 4)
            elif( not(file.name[0] == '.' and not self.showAll)):
                allFiles.append(file.name)

        for file in allFiles:
            spaces = ""
            for i in range(indent-4):
                if(i % 4 == 0):
                    spaces += '|'
                else:
                    spaces += ' '

            formatIndent = spaces + '\\' + '__>'

            cprint(formatIndent, "white", end='')
            cprint(file, "green")


def main():
    showAll = False;
    if(len(sys.argv) > 1):
        if(sys.argv[1] == "-a" or sys.argv[1] == "--all"):
            showAll = True
        elif(sys.argv[1] == "-h" or sys.argv[1] == "--help"):
            print('''tree - v-0.0.1 (2020 Aug. 30)\n
Usage: tree [arguments] displays file structure.\n
Arguments:\n
-a  or  --all:    Include hidden files in tree visualization\n
-h  or  --help:   Print Help (this message) and exit''')
            sys.exit(1)
        else:
            print(f'''tree - v-0.0.1 (2020 Aug. 30)\n
Garbage after option argument: "{sys.argv[1]}"\n
More info with: "tree -h"''')
            sys.exit(1)

    tree = Tree(showAll)
    tree.print()


if __name__ == '__main__':
    main()
