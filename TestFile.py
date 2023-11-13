import os
import platform
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
    testPath = ''
    exPath = ''
    timeout = 0

    # name = nome dell'esercizio
    # diffPath = "nomePath", se ha una path diversa dalla default 'Exercises'
    # samePath = True, se il .py si trova nella cartella dei Testcases, con lo stesso nome
    def __init__(self, name, type="py"):

        self.name = name
        self.type = type

        self.curPath = os.path.realpath(os.path.dirname(__file__))
        self.exPath = os.path.join(self.curPath, "Exercises")
        self.testPath = os.path.join(self.curPath,  "Testcases")

        self.getTimeout()
        self.currentOs = self.whatOs()
        self.testcase = self.getTestcase(name)
        self.error = False
        self.risultati = {}  # Se si fa con i thread, per tenere traccia dei vari testcase
        self.title = name

        # if self.currentOs == "Mac" or self.currentOs == "Linux":
        #     self.exPath = os.getcwd() + "/Exercises"
        #     self.testPath = os.getcwd() + "/Testcases"

        self.exist = self.fileExists()

    def testExercise(self,show):
        if self.exist:
            execString = [self.pythonDir, os.path.join(self.exPath, f"{self.name}.py")] 
            print(f"\t### TESTING {self.title} ###")
            print("------------------------------------")
            for i, v in self.testcase.items():
                _namefile = v["namefile"]
                _input = v["input"]
                _output = v["output"]
                p = subprocess.Popen(execString, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                
                i_str = 'Input: \n'+_input
                if not show: i_str = ''

                try:
                    stdout, stderr = p.communicate(input=_input, timeout=self.timeout)
                    if p.returncode != 0:  # Esercizio ha dato errore
                        # raise con i thread
                        # print(failed con i testcase passati)
                        # return normale con il for
                        # raise KozaError(stdout, stderr)
                        self.error = True
                        print(f"Testcase: {str(i+1).zfill(2)}, File: {_namefile} - ERROR ❌ \n{i_str}Expected output: {_output} Actual output: {str(stdout)} \nError: {stderr}".ljust(30))
                    else:
                        if _output == stdout:
                            print(f"Testcase: {str(i+1).zfill(2)} - CORRECT ✅".ljust(30))
  
                        elif (_output + "\n") == stdout:
                            self.error = True
                            print(f"Testcase: {str(i+1).zfill(2)}, File: {_namefile} - SEMI-CORRECT ⚠️  Check for the end = \"\" in the print")
                        
                        else:
                            self. error = True
                            print(f"Testcase: {str(i+1).zfill(2)}, File: {_namefile} - WRONG ❌ \n{i_str}Expected output: {_output} Actual output: {str(stdout)}".ljust(30))
                            
                except subprocess.TimeoutExpired:
                    p.kill()
                    self.error = True
                    print(f"Testcase: {v[i]} - TIMEOUT EXPIRED ⏰".ljust(30))

            if not self.error and len(self.testcase) >= 1:
                print("------------------------------------")
                print("\tALL TESTCASES PASSED! 🥳")
            elif not self.error and len(self.testcase) == 0:
                print("------------------------------------")
                print("\tNO TESTCASE FOUND! ")
                exit(1)
            else:
                print("------------------------------------")
                print("\tNOT ALL TESTCASES PASSED! 😱")
                exit(1)
        else:
            print(f"Exercise with the name: {self.name} NOT FOUND!")
            exit(1)

    #  Windows, Linux or Mac
    def whatOs(self):
        currentOs = platform.system()
        windos = ["win32", "Windows"]
        mec = ["Darwin", "mac"]
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
        nomeIn = os.path.join(self.testPath, name, "*.in")
        nomeOut = os.path.join(self.testPath, name, "*.out")

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


            # Find name file testcase
            nomefile = ain[i]
            char = '/' if (self.currentOs == "Linux" or self.currentOs == "Mac") else '\\'
            nomefile = nomefile[nomefile.rindex(char)+1:]

            Testcases[i] = {
                "namefile": nomefile,
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

    def fileExists(self):
        esiste = False

        if os.path.exists(self.testPath) and os.path.exists(self.exPath):
            if os.path.exists(os.path.join(self.exPath, f"{self.name}.py")):
                esiste = True

        return esiste


def prova():
    ciao = Test("Lab2Set")
    ciao.testExercise()


if __name__ == "__main__":
    if _DEBUG:
        prova()
    else:
        pass
