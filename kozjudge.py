import subprocess, os, glob, configparser

pathEx = ''
pathSol = '' # Testcases
timeLimit = 60

def makeConfig(pathExercises: str, pathSolutions: str) -> None:
    config = configparser.ConfigParser()
    config['PATHS'] = {'exercises': f"{pathExercises}", 'solutions': f"{pathSolutions}"}

    with open('config.ini', 'w') as configfile:
        config.write(configfile)

def loadConfig():
    config = configparser.ConfigParser()
    config.read('config.ini')
    if (os.path.exists(config['PATHS']['exercises']) and os.path.exists(config['PATHS']['solutions'])):
        global pathEx, pathSol
        pathEx = f"{config['PATHS']['exercises']}"
        pathSol = f"{config['PATHS']['solutions']}"
    else:
        print("Error! Check the config file")


def loadTestCases(exercise: str) -> list[str]:
    Testcases = []
    os.chdir(f"{pathSol}/{exercise}")
    for file in glob.glob(f"{exercise}_*.in"):
        Testcases.append(file)
    return Testcases

def startJudging(exercise, tc):
    count_tc_passed = 0 
    print("------------------------------------------------------------------")
    print("Testing:", exercise)
    for i in range(len(tc)):
        file_in = f'{pathSol}/{exercise.upper()}/{tc[i]}'
        file_out = file_in[:-2] + "out"

        with open(file_in) as f1:
            inn = f1.readlines()

        innt = ""
        for j in range(len(inn)):
            innt += inn[j] 

        p = subprocess.Popen(['python3', f'{pathEx}/{exercise}.py'], stdin=subprocess.PIPE, stdout=subprocess.PIPE, text=True)
        
        try:
            stdout, stderr = p.communicate(input=innt, timeout=timeLimit)
        except subprocess.TimeoutExpired:
            p.kill()
            print("Testcase:", tc[i], "- TIMEOUT EXPIRED ⏰")
            continue
        
        with open(file_out) as f2:
            out = f2.readlines()

        outt = ""
        for j in range(len(out)):
            outt += out[j] 
        
        if (stdout == outt):
            count_tc_passed += 1
            print("Testcase:",tc[i], "- CORRECT ✅ ")
        elif (stderr != ""):
            print("Testcase:",tc[i], "- ERROR ❗ \n", "Actual output:", str(outt), "Error raised: ", str(stderr))
        else:
            print("Testcase:",tc[i], "- WRONG ❌ \n", "Expected output:", str(stdout), "Actual output:", str(outt))
        #print("Testcase:",tc[j], stdout == outt)
    print("""------------------------------------------------------------------\n""")
    if (count_tc_passed == len(tc)):
        print("ALL TESTCASE PASSED! 🥳")
    else:
        print("NOT ALL TESTCASE PASSED! 😱")


def startProgram():
    print(""" 
    ██╗░░██╗░█████╗░███████╗░░░░░██╗██╗░░░██╗██████╗░░██████╗░███████╗
    ██║░██╔╝██╔══██╗╚════██║░░░░░██║██║░░░██║██╔══██╗██╔════╝░██╔════╝
    █████═╝░██║░░██║░░███╔═╝░░░░░██║██║░░░██║██║░░██║██║░░██╗░█████╗░░
    ██╔═██╗░██║░░██║██╔══╝░░██╗░░██║██║░░░██║██║░░██║██║░░╚██╗██╔══╝░░
    ██║░╚██╗╚█████╔╝███████╗╚█████╔╝╚██████╔╝██████╔╝╚██████╔╝███████╗
    ╚═╝░░╚═╝░╚════╝░╚══════╝░╚════╝░░╚═════╝░╚═════╝░░╚═════╝░╚══════╝\n""")
    
    file = input("Welcome to KòzJudge!\nPlease insert the name of the exercise: ")
    testcase = loadTestCases(file)
    startJudging(file,testcase)

def main():
    if (os.path.exists("config.ini")):
        loadConfig()
        startProgram()
    else:
        pathEx = input("Please insert the path where your exercises are located: ")
        pathSol = input("Please insert the path where your solutions are located: ")
        print()
        makeConfig(pathEx, pathSol)
        loadConfig()
        startProgram()


main()
