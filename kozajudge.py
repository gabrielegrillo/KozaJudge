import os
import sys
import TestFile
import argparse

banner = """ 
██╗░░██╗░█████╗░███████╗░█████╗░░░░░░██╗██╗░░░██╗██████╗░░██████╗░███████╗
██║░██╔╝██╔══██╗╚════██║██╔══██╗░░░░░██║██║░░░██║██╔══██╗██╔════╝░██╔════╝
█████═╝░██║░░██║░░███╔═╝███████║░░░░░██║██║░░░██║██║░░██║██║░░██╗░█████╗░░
██╔═██╗░██║░░██║██╔══╝░░██╔══██║██╗░░██║██║░░░██║██║░░██║██║░░╚██╗██╔══╝░░
██║░╚██╗╚█████╔╝███████╗██║░░██║╚█████╔╝╚██████╔╝██████╔╝╚██████╔╝███████╗
╚═╝░░╚═╝░╚════╝░╚══════╝╚═╝░░╚═╝░╚════╝░░╚═════╝░╚═════╝░░╚═════╝░╚══════╝\n"""

def confArgs(): # codice relativo ai parametri a riga di comando e alla guida
    parser = argparse.ArgumentParser(description='Controlla un esercizio di domjudge')
    parser.add_argument('filename', help='nome del file senza .py', nargs='?', default=None)
    parser.add_argument('-i','--show_input',help="mostra anche l'input dei testcase sbagliati", action="store_true")
    parser.add_argument('-s','--small',help="mostra anche l'input senza andare a capo, da usare con -i o --show_input", action="store_true")
    
    return parser.parse_args()

def startJudging(exercise: str,args):
    file = TestFile.Test(exercise)
    file.testExercise(args)

def startProgram(args) -> None:
    
    print(banner)

    real_path = os.path.realpath(os.path.dirname(__file__))
    
    file = args.filename
    
    if file == None:
        file = input("Welcome to KozaJudge!\nPlease insert the name of the exercise: ")
        
    if os.path.exists(real_path + "/Testcases"):
        if os.path.exists(real_path + "/Exercises"):
            startJudging(file.upper(),args)
        else:
            print("Exercises not found. Please check the folders")
            exit(1)
    else:
        print("Testcases were not found. Please check the folders")
        exit(1)

def main() -> None:
    args = confArgs() #restituisce un oggetto che contiene gli args
    startProgram(args)

main()
