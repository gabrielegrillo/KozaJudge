# KozaJudge

<!--- ![Logo](/multimedia/LOGO.png) --->
<img src="multimedia/LOGO.png" width=60% >

Wait... what is a Koza? It is a sheep in [Polish](https://en.wiktionary.org/wiki/koza#Polish).

KozaJudge is a basic (also probably stupid) solutions checker for Python excerises. Made by :heart: for [Unical](https://www.unical.it) first year [Computer Science](https://informatica.unical.it/) students. 

## [PER IL README IN ITALIANO, CLICCA QUI!](/README_it-IT.md)

## Prerequisites

Clone the repository with
```
$ git clone https://github.com/gabrielegrillo/KozaJudge.git
```

Create the exercises and solutions folders in the KozaJudge folder. 
One folder is for the exercises and the second one is for the solutions.

The final structure of the folder should be like this:
```
Testcases/
├── exercise1/
│   ├── exercise1_1.in
│   ├── exercise1_1.out
│   ├── exercise1_2.in
│   └── exercise1_2.out
├── exercise2/
│   ├── exercise2_1.in
│   ├── exercise2_1.out
├── exercise3/
│   ├── exercise3_1.in
│   ├── exercise3_1.out

Exercises/
├── exercise1.py
├── exercise2.py
├── exercise3.py

kozajudge.py
TestFile.py
...
```
For each testcase there is a file with `{name_exercise}_{testcase_number}.in` and `{name_exercise}_{testcase_number}.out`


## How to use it

Open a terminal from the folder where the release is located. 

Execute the following command as shown: 
<img src="multimedia/gifs/k2.gif">


or you can put the Exercise in the parameters of the command.
<img src="multimedia/gifs/k1.gif">

There are also two optional parameters:

- `--show-input` or `-i`  for displaing the input in case of wrong answer

- `--small` or `-s` (to be used with `-i`)  for displaing the input in case of wrong answer, but removing newlines for clarity

Examples (for exercise Lab2Set):

```
python3 kozajudge.py Lab2Set
```
```
python3 kozajudge.py Lab2Set --show-input
```
```
python3 kozajudge.py Lab2Set --show-input --small
```

## Contributors
<a href="https://github.com/gabrielegrillo/KozaJudge/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=gabrielegrillo/KozaJudge" height="50"/>
</a>

## To do List: 

If you would like to contribute to this project, here there is a list of things to do.

- [X] Translate the readme in italian.

- [X] Test it on windows.
      
- [ ] Deploy it as a Python Package or make a GUI.

- [ ] Insert a sort of guide before entering the paths in the setup. 

- [ ] Create a sort of debug mode for us

- [ ] Make a decent logo.

- [ ] Add license

