Name: Aman Hogan-Bailey
MavId: 1001830469
Date: 4/30/2023

Programming Language: 3.11.2 64 Python
Environement: VsCode and Microsoft CMD command line prompt


STRUCTURE ******************************************************************************************************************************************************************************
The driver code is specified in 'bnet.py'. This file is respinsible for  calculating any value in the JPD for this domain using conditional probabilty distributions calculated.
'bnet.py' needs the following invocation: <training_data> <Bt/Bf> <Gt/Gf> <Ct/Cf> <Ft/Ff>
The training_data is a text file where each column represents a truth value, (0 or 1)

Program Logic **************************************************************************************************************************************************************************
1) bnet calculates truth table from training data text file
2) bnet calculats conditional probabilty
3) bnet then calculates any jpd value using the conditional probabilty table using the cmd args

HOW TO RUN ******************************************************************************************************************************************************************************
There are two ways to run this program:

Windows CMD:
Unzip the downloaded file.
Open your Windows terminal.
Make sure you have python version 3 or higher installed.
Locate the directory the source code where 'bnet.py' is located: cd C:\Users\ .... \bnet.py
Then, from the command-line run: 'python bnet.py <training_data> <Bt/Bf> <Gt/Gf> <Ct/Cf> <Ft/Ff>'
The code should then output the reults

Vscode:
Unzip the downloaded file.
Open the folder in vscode and select 'trust this folder'
Set up your vscode to have a python Environement
    * Hold down SHIFT+CTRL+P and select 'Python:select interpter' and choose the path where python is installed on your system
Find the 'bnet.py' and right click and select 'Run python file in terminal'
    * This will open a terminal in Vscode using a python interpreter.
Now, with the terminal open, enter python bnet.py <training_data> <Bt/Bf> <Gt/Gf> <Ct/Cf> <Ft/Ff>
The program should then run and print the neccessary outputs


* NOTES ******************************************************************************************************************************************************************************
None