# BNet Program

This program, developed by Aman Hogan-Bailey, is written in Python 3.11.2 64-bit and designed to calculate values in the Joint Probability Distribution (JPD) for a specific domain using conditional probability distributions.

## Environment

The program was developed using Visual Studio Code (VsCode) and the Microsoft CMD command line prompt.

## Structure

The driver code for the program is located in the 'bnet.py' file. This file is responsible for performing calculations on the JPD based on conditional probability distributions that have been calculated.

To run the program, the 'bnet.py' file should be invoked with the following command line arguments: `<training_data> <Bt/Bf> <Gt/Gf> <Ct/Cf> <Ft/Ff>`

The `training_data` argument should be a text file where each column represents a truth value (0 or 1).

## Program Logic

The program follows the following logic:

1. Calculate the truth table from the provided training data text file.
2. Calculate the conditional probabilities.
3. Use the conditional probability table to calculate the desired JPD value based on the command line arguments.

## How to Run

There are two ways to run this program:

### Windows CMD

1. Unzip the downloaded file.
2. Open your Windows terminal.
3. Make sure you have Python version 3 or higher installed.
4. Navigate to the directory where the source code is located, using the command: `cd C:\path\to\bnet.py`
5. Run the program from the command line using the following command: `python bnet.py <training_data> <Bt/Bf> <Gt/Gf> <Ct/Cf> <Ft/Ff>`
6. The program will output the results.

### VsCode

1. Unzip the downloaded file.
2. Open the folder in VsCode and select "Trust this folder" if prompted.
3. Set up your VsCode to have a Python environment:
   - Hold down SHIFT+CTRL+P and select "Python: Select Interpreter"
   - Choose the path where Python is installed on your system.
4. Locate the 'bnet.py' file in VsCode.
5. Right-click on the 'bnet.py' file and select "Run Python File in Terminal".
   - This will open a terminal in VsCode using a Python interpreter.
6. With the terminal open, enter the following command: `python bnet.py <training_data> <Bt/Bf> <Gt/Gf> <Ct/Cf> <Ft/Ff>`
7. The program will run and print the necessary outputs.

## Notes

- None
