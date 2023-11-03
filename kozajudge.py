import os
import sys
import TestFile


def startJudging(exercise: str):
    file = TestFile.Test(exercise)
    file.testExercise()


def startProgram(ex="") -> None:
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
            startJudging(file)
        else:
            print("Exercises not found. Please check the folders")
            exit(1)
    else:
        print("Testcases were not found. Please check the folders")
        exit(1)


def main() -> None:
    if len(sys.argv) > 1:
        startProgram(sys.argv[1])
    else:
        startProgram()


main()
