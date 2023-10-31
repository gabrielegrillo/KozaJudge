import os
import sys
import subprocess
import json
import glob
import configparser

_DEBUG = False


class KozaError(Exception):
    def __init__(self, output, error):
        self.message = output
        self.error = error

    def __str__(self):
        return f"Output: {self.message} - Error: {self.error}"


class Test:
    pythonDir = sys.executable
    currentOs = ""
    testPath = os.getcwd() + "\\Testcases"
    exPath = os.getcwd() + "\\Exercises"
    timeout = 0

    # name = nome dell'esercizio
    # diffPath = "nomePath", se ha una path diversa dalla default 'Exercises'
    # samePath = True, se il .py si trova nella cartella dei Testcases, con lo stesso nome
    def __init__(self, name, type="py"):
        self.name = name
        self.type = type
        self.curPath = os.getcwd()
        self.getTimeout()
        self.currentOs = self.whatOs()
        self.testcase = self.getTestcase(name)
        self.error = False
        self.risultati = {} # Se si fa con i thread, per tenere traccia dei vari testcase
        self.title = name

        if self.currentOs == "Mac" or self.currentOs == "Linux":
            self.exPath = os.getcwd() + "/Exercises"
            self.testPath = os.getcwd() + "/Testcases"
    def testExercise(self):
        execString = [self.pythonDir, os.path.join(self.exPath, f"{self.name}.py")]  # Windows Default

        if self.currentOs == "Windows":
            pass
        elif self.currentOs == "Mac":
            execString = [self.pythonDir, os.path.join(self.exPath, f"{self.name}.py")]
        elif self.currentOs == "Linux":
            pass
        print(f"\t### TESTING {self.title} ###")
        print("------------------------------")
        for i, v in self.testcase.items():
            _input = v["input"]
            _output = v["output"]
            p = subprocess.Popen(execString, stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

            try:
                stdout, stderr = p.communicate(input=_input, timeout=self.timeout)
                if p.returncode != 0:  # Esercizio ha dato errore
                    # raise con i thread
                    # print(failed con i testcase passati)
                    # return normale con il for
                    # raise KozaError(stdout, stderr)
                    self.error = True
                    if i < 9:
                        print(
                            f"Testcase: 0{i + 1}, - ERROR ❌ \nExpected output: {_output} Actual output: {str(stdout)} \nError: {stderr}".ljust(30))
                    else:
                        print(
                            f"Testcase: {i + 1}, - ERROR ❌ \nExpected output: {_output} Actual output: {str(stdout)} \nError: {stderr}".ljust(30))
                else:
                    if _output == stdout:
                        if i < 9:
                            print(f"Testcase: 0{i + 1} - CORRECT ✅".ljust(30))
                        else:

                            print(f"Testcase: {i+1} - CORRECT ✅".ljust(30))
                    elif (_output + "\n") == stdout:
                        self.error = True
                        if i < 9:
                            print(f"Testcase: 0{i + 1} - SEMI-CORRECT ⚠️ Check for the end = \"\" in the print")
                        else:
                            print(f"Testcase: {i + 1} - SEMI-CORRECT ⚠️ Check for the end = \"\" in the print")
                    else:
                        if i < 9:
                            print(
                                f"Testcase: 0{i + 1} - WRONG ❌ \nExpected output: {_output} Actual output: {str(stdout)}".ljust(30))
                        else:
                            print(
                                f"Testcase: {i + 1} - WRONG ❌ \nExpected output: {_output} Actual output: {str(stdout)}".ljust(30))
            except subprocess.TimeoutExpired:
                p.kill()
                self.error = True
                if i < 9:
                    print(f"Testcase: 0{i + 1} - TIMEOUT EXPIRED ⏰".ljust(30))
                else:
                    print(f"Testcase: {i + 1} - TIMEOUT EXPIRED ⏰".ljust(30))

        if not self.error:
            print("------------------------------")
            print("\tALL TESTCASE PASSED! 🥳")
        else:
            print("------------------------------")
            print("\tNOT ALL TESTCASE PASSED! 😱")

    # Windows, Linux or Mac
    def whatOs(self):
        currentOs = os.environ['OS'].lower()
        windos = ["win32", "windows"]
        mec = ["darwin", "mac"]
        if currentOs in windos:
            return "Windows"
        elif currentOs in mec:
            return "Mac"
        else:
            return "Linux"

    def getTestcase(self, name: str) -> dict:
        Testcases = {}

        ain = []
        aout = []
        nomeIn = self.testPath + f"\\{name}\\*.in"
        nomeOut = self.testPath + f"\\{name}\\*.out"

        if self.currentOs == "Mac" or self.currentOs == "Linux":
            nomeIn = self.testPath + f"/{name}/*.in"
            nomeOut = self.testPath + f"/{name}/*.out"

        for file in glob.glob(nomeIn):
            ain.append(file)

        for file in glob.glob(nomeOut):
            aout.append(file)

        ain.sort()
        aout.sort()

        for i in range(len(ain)):
            innt = ""
            ouut = ""

            with open(ain[i]) as f:
                innt = "".join(f.readlines())

            with open(aout[i]) as f:
                ouut = "".join(f.readlines())

            Testcases[i] = {
                "input": innt,
                "output": ouut,
            }
        return Testcases

    def getTimeout(self):
        path = self.testPath + "\\" + self.name
        config = configparser.ConfigParser()
        if os.path.exists(os.path.join(path, "domjudge-problem.ini")):
            with open(os.path.join(path, "domjudge-problem.ini")) as stream:
                # Little trick to cheat the parser.
                config.read_string("[top]\n" + stream.read())
                self.timeout = float(config["top"]["timelimit"].rstrip("'").lstrip("'"))
                if len(config["top"]["name"].rstrip("'").lstrip("'")) >= 3:
                    self.title = config["top"]["name"].rstrip("'").lstrip("'")
        else:
            self.timeout = 45.0



def prova():
    ciao = Test("N56")
    ciao.testExercise()


if __name__ == "__main__":
    if _DEBUG:
        prova()
    else:
        pass
