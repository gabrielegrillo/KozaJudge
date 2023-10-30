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

    def testExercise(self):
        execString = [self.pythonDir, os.path.join(self.exPath, f"{self.name}.py")]  # Windows Default

        if self.currentOs == "Windows":
            pass
        elif self.currentOs == "Mac":
            execString = [self.pythonDir, os.path.join(self.exPath, f"{self.name}.py")]
        elif self.currentOs == "Linux":
            pass

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
                    print(
                        f"Testcase: {i+1}, - ERROR ❌ \nExpected output: {_output} Actual output: {str(stdout)} \nError: {stderr}")
                else:
                    if _output == stdout:
                        print(f"Testcase: {i+1} - CORRECT ✅")
                    elif (_output + "\n") == stdout:
                        self.error = True
                        print(f"Testcase: {i+1} - SEMI-CORRECT ⚠️ Check for the end = \"\" in the print")
                    else:
                        print(
                            f"Testcase: {i+1}, - WRONG ❌ \nExpected output: {_output} Actual output: {str(stdout)}")
            except subprocess.TimeoutExpired:
                p.kill()
                self.error = True
                print(f"Testcase: {i+1} - TIMEOUT EXPIRED ⏰")

        if not self.error:
            print("ALL TESTCASE PASSED! 🥳")
        else:
            print("NOT ALL TESTCASE PASSED! 😱")

    # Windows, Linux or Mac
    def whatOs(self):
        currentOs = os.environ['OS'].lower()
        if currentOs in "windows":
            return "Windows"
        elif currentOs in "mac":
            return "Mac"
        else:
            return "Linux"

    def getTestcase(self, name: str) -> dict:
        Testcases = {}

        ain = []
        aout = []

        for file in glob.glob(os.getcwd() + f"\\Testcases\\{name}\\*.in"):
            ain.append(file)

        for file in glob.glob(os.getcwd() + f"\\Testcases\\{name}\\*.out"):
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
        else:
            self.timeout = 45.0



def prova():
    ciao = Test("esercizio1")
    ciao.testExercise()


if __name__ == "__main__":
    if _DEBUG:
        prova()
    else:
        pass
