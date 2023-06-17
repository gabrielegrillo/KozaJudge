import subprocess, os, glob, configparser

pathEx = ''
pathSol = ''
timeLimit = 60

def makeConfig(pathExercises: str, pathSolutions: str) -> None:
    
    config = configparser.ConfigParser()
    config['PATHS'] = {'exercises': pathExercises, 'solutions': pathSolutions}

    with open('config.ini', 'w') as configfile:
        configfile.write(config)

def loadTestCases(exercise: str) -> list[str]:
    Testcases = []
    os.chdir(f"/Users/gabrielegrillo/Documents/Università/Primo Semestre/Fondamenti di Programmazione/Esercizi DomJudge/Testcase/{exercise}")
    for file in glob.glob(f"{exercise}_*.in"):
        Testcases.append(file)
    return Testcases

def startJudging(exercise, tc):
    for i in range(len(tc)):
        file_in = f'/Users/gabrielegrillo/Documents/Università/Primo Semestre/Fondamenti di Programmazione/Esercizi DomJudge/Testcase/{exercise.upper()}/{tc[i]}'
        file_out = file_in[:-2] + "out"

        with open(file_in) as f1:
            inn = f1.readlines()

        innt = ""
        for j in range(len(inn)):
            innt += inn[j] 

        timeoutted = False
        p = subprocess.Popen(['python3', f'/Users/gabrielegrillo/Documents/Università/Primo Semestre/Fondamenti di Programmazione/Esercizi DomJudge/{exercise}.py'], 
                            stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        try:
            stdout, stderr = p.communicate(input=innt, timeout=timeLimit)
        except TimeoutExpired:
            p.kill()
            timeoutted = True
        
        with open(file_out) as f2:
            out = f2.readlines()

        outt = ""
        for j in range(len(out)):
            outt += out[j] 
        
        if (stdout == outt):
            print("Testcase:",tc[i], "CORRECT ✅ ")
        elif (timeoutted):
            print(f"Testcase: {tc[i]} TIMEOUT EXPIRED")
        else:
            print("Testcase:",tc[i], "WRONG ❌ \n", "Expected output:", str(stdout), "Actual output:", str(outt))
        #print("Testcase:",tc[j], stdout == outt)

def main():
    # Check if it exist a configuration file. Otherwise, create it.
    if (checkConfig()):
        loadConfig()
        file = input("Ciao\nInserisci il numero dell'exercise: ")
        testcase = loadTestCases(file)
        startJudging(file,testcase)
    else:
        pathEx = input("Please insert the path where your exercises are located: ")
        pathSol = input("Please insert the path where your solutions are located: ")

        makeConfig(pathEx, pathSol)

    


main()
