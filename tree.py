from pathlib import Path
from termcolor import cprint
import os

class Tree():
    """docstring for Tree."""

    def __init__(self):
        self.currPath = Path(os.getcwd());
        cprint((self.currPath.name), "blue")


    def print(self, indent = 4):
        allFiles = []
        for file in self.currPath.iterdir():
            if(file.is_dir()):
                spaces = ""
                for i in range(indent-4):
                    if(i % 4 == 0):
                        spaces += '|'
                    else:
                        spaces += ' '

                formatIndent = spaces + '\\' + '-' * 4

                cprint(formatIndent, "white", end='')
                cprint((file.name), "blue")

                self.currPath = file;
                self.print(indent + 4)
            else:
                allFiles.append(file.name)

        for file in allFiles:
            spaces = ""
            for i in range(indent-4):
                if(i % 4 == 0):
                    spaces += '|'
                else:
                    spaces += ' '

            formatIndent = spaces + '\\' + '-' * 2 + '>'

            cprint(formatIndent, "white", end='')
            cprint(file, "green")


def main():
    tree = Tree()
    tree.print()


if __name__ == '__main__':
    main()
