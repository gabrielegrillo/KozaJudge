import os
import sys
import TestFile
import argparse

def setArgs():
    parser = argparse.ArgumentParser(description='Controlla un esercizio di domjudge')
    parser.add_argument('filename', help='nome del file senza .py', nargs='?', default=None)
    parser.add_argument('-i','--show_input',help="mostra anche l'input dei testcase sbagliati", action="store_true")
    
    return parser.parse_args()

def startJudging(exercise: str,show: bool):
    file = TestFile.Test(exercise)
    file.testExercise(show)

def startProgram(ex="",show_input=False) -> None:
    

    print(""" 
██╗░░██╗░█████╗░███████╗░█████╗░░░░░░██╗██╗░░░██╗██████╗░░██████╗░███████╗
██║░██╔╝██╔══██╗╚════██║██╔══██╗░░░░░██║██║░░░██║██╔══██╗██╔════╝░██╔════╝
█████═╝░██║░░██║░░███╔═╝███████║░░░░░██║██║░░░██║██║░░██║██║░░██╗░█████╗░░
██╔═██╗░██║░░██║██╔══╝░░██╔══██║██╗░░██║██║░░░██║██║░░██║██║░░╚██╗██╔══╝░░
██║░╚██╗╚█████╔╝███████╗██║░░██║╚█████╔╝╚██████╔╝██████╔╝╚██████╔╝███████╗
╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═════╝░░╚═════╝░╚══════╝\n""")

    real_path = os.path.realpath(os.path.dirname(__file__))

    if ex == "":
        file = input("Welcome to KozaJudge!\nPlease insert the name of the exercise: ")
    else:
        file = ex
    if os.path.exists(real_path + "/Testcases"):
        if os.path.exists(real_path + "/Exercises"):
            startJudging(file,show_input)
        else:
            print("Exercises not found. Please check the folders")
            exit(1)
    else:
        print("Testcases were not found. Please check the folders")
        exit(1)


def main() -> None:
    args = setArgs()
    show_input = False

    if args.show_input:
        show_input=True

    if args.filename:
        startProgram(args.filename,show_input)
    else:
        startProgram()


main()
