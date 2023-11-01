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

    if ex == "":
        file = input("Welcome to KozaJudge!\nPlease insert the name of the exercise: ")
    else:
        file = ex
    if os.path.exists(os.getcwd() + "/Testcases"):
        if os.path.exists(os.getcwd() + "/Exercises"):
            startJudging(file)
        else:
            print("Exercises not found. Please check the folders")
    else:
        print("Testcases were not found. Please check the folders")


def main() -> None:
    if len(sys.argv) > 1:
        startProgram(sys.argv[1])
    else:
        startProgram()


main()
