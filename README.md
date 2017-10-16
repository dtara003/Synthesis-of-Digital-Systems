# Synthesis-of-Digital-Systems
### Dharti Tarapara

## Simplex Method

The objective of the program is to implement the Simplex method to solve Linear Programs
(LPs). It is written in Python and is run with the Python 3.6.3 interpretor.

### Input File

The program takes in a text file with floating point numbers as input. The first line contains the maximization problem's m and n values.
```
m n
```
The second line contains all values in the vector b.
```
b0 b1 b2 ... bm
```
The thid line contains all values in the vector c.
```
c0 c1 c2 ... cn
```
The rest of the file contains an m x n matrix A.
```
a00 a01 a02 ... a0n
a10 a11 a12 ... a1n
a20 a21 a22 ... a2n
...
am0 am1 am2 ... amn
```
Do not include a blank newline at the end of the file.

### To Run

To run the program, download the .py file and type
```
simplex.py <inputFile>
```
into the command line. Replace <inputFile> with a .txt file containing floating point values.
