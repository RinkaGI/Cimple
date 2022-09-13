import re
from error import Error

class Parser:
    def __init__(self, code: str):
        #Pass in code
        self.code = code
        #Parse code
        self.code = self.Parse(self.code)

    def Parse(self, code: str) -> str:
        #Parse code into normal python
        code = self.ParseStartEnd(code)
        code = self.ParseStartLibrary(code)
        code = self.ParseFunctions(code)
        code = self.parseInputVariables(code)

        #Dump code to file
        with open("output.c", "w") as f:
            f.write(code)
        return code

    def ParseStartLibrary(self, code: str) -> str:
        for line in code.splitlines():
            if "start IO;" in line:
                if not self.IsInString('start IO;', line):
                    code = code.replace('start IO;', '#include <stdio.h>')
        return code

    def ParseStartEnd(self, code: str) -> str:
        for line in code.splitlines():
            if "startMain();" in line:
                if not self.IsInString('startMain();', line):
                    code = code.replace('startMain();', 'int main(){')
        for line in code.splitlines():
            if "endMain();" in line:
                if not self.IsInString('endMain();', line):
                    code = code.replace('endMain();', 'return 0; }')
        return code

    def ParseFunctions(self, code: str) -> str:
        for line in code.splitlines():
            if "print" in line and not self.IsInString('print', line):
                code = code.replace('print', 'printf')

        for line in code.splitlines():
            if "system: pause" in line and not self.IsInString('system: pause', line):
                code = code.replace('system: pause', 'system("pause");')

        for line in code.splitlines():
            if "input" in line and not self.IsInString('input', line):
                code = code.replace('input', 'scanf')

        return code

    def parseInputVariables(self, code: str) -> str:
        for line in code.splitlines():
            if "inputInteger" in line and not self.IsInString('inputInteger', line):
                code = code.replace("inputInteger", "%i")
            if "inputString" in line and not self.IsInString('inputString', line):
                code = code.replace("inputString", "%s")
            if "inputDouble" in line and not self.IsInString('inputDouble', line):
                code = code.replace("inputDouble", "%lf")
            if "inputFloat" in line and not self.IsInString('inputFloat', line):
                code = code.replace("inputFloat", "%f")

        return code

    def IsInString(self, phrase : str, line : str, returnIfMultiple = False) -> bool:
        if not phrase in line:
            return False
        if line.count(phrase) > 1:
            return returnIfMultiple
        leftSide = line.partition(phrase)[0]
        if leftSide.count("\"") > 0:
            if leftSide.count("\"") % 2 == 0:
                return False
            else:
                return True
        if leftSide.count("\'") > 0:
            if leftSide.count("\'") % 2 == 0:
                return False
            else:
                return True