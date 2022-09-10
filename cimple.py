import sys
import os
from error import Error
from parse import Parser

def GetCode(filePath) -> str:
    if os.path.isfile(filePath):
        with open(filePath, 'r') as file:
            return file.read()
    else:
        Error("Input file not found")

def HandleArgs():
    if sys.argv[1] == '--help' or sys.argv[1] == '-h':
        Error(
            '''
            Command line arguments:
            --help -h: Prints this message
            --compile (file.cimple): Compiles Cimple to C
            '''
        )

    if sys.argv[1] == '--compile':
        if len(sys.argv) < 2:
            Error("Invalid number of arguments")
        else:
            if os.path.isfile(sys.argv[2]):
                parser = Parser(GetCode(sys.argv[2]))

if __name__ == '__main__':
    HandleArgs()