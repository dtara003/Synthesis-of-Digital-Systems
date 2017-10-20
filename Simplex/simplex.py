import sys

# get input data from file
inputFile = sys.argv[1]
file = open(inputFile, "r")
a = []
for line in file:
    temp = line.split()
    values = [float(i) for i in temp]
    a.append(values)
file.close()

# parse data
m = int(a[0][0])
n = int(a[0][1])
b = [a[1][i] for i in range(m)]
c = [a[2][i] for i in range(n)]
del a[0:3]

# set up matrix tableau
tableau = [[0.0 for i in range(m + n + 1)] for j in range(m + 1)]
for i in range(m):
    for j in range(n):
        tableau[i][j] = a[i][j]
for i in range(m):
    tableau[i][-1] = b[i]
for i in range(n):
    tableau[-1][i] = -1.0 * c[i]
for i in range(m):
    tableau[i][n + i] = 1.0

# verify optimization
lowestVal = tableau[-1][0]
lowestIndex = 0
for i in range(m + n):
    if tableau[-1][i] < lowestVal:
        lowestVal = tableau[-1][i]
        lowestIndex = i

# perform pivots
while lowestVal < 0.0:
    # find lowest ratio and pivot point
    lowestRatio = float("inf")
    pivotRow = 0
    pivotVal = 0.0
    for i in range(m):
        # skip b values with negative corresponding element
        if tableau[i][lowestIndex] >= 0.0:
            ratio = tableau[i][-1] / tableau[i][lowestIndex]
            if ratio < lowestRatio:
                lowestRatio = ratio
                pivotRow = i
                pivotVal = tableau[i][lowestIndex]

    # adjust pivot row
    for i in range(m + n + 1):
        tableau[pivotRow][i] = tableau[pivotRow][i] / pivotVal

    # perform arithmetic on non-pivot rows
    tempTab = [[0.0 for i in range(m + n + 1)] for j in range(m + 1)]
    for i in range(m + 1):
        if i != pivotRow:
            for j in range(m + n + 1):
                tempTab[i][j] = tableau[i][j] - tableau[i][lowestIndex] * tableau[pivotRow][j]
        else:
            for j in range(m + n + 1):
                # pivot row already adjusted
                tempTab[i][j] = tableau[i][j]

    tableau = tempTab
    del tempTab

    # verify optimization
    lowestVal = tableau[-1][0]
    lowestIndex = 0
    for i in range(m + n):
        if tableau[-1][i] < lowestVal:
            lowestVal = tableau[-1][i]
            lowestIndex = i

# output solution to file
file = open("simplex.out", "w")

for i in range(m):
    if tableau[i][-1] < 0:
        file.write("bounded-infeasable")
        file.close()
        sys.exit()

file.write(str(tableau[-1][-1]))
file.write("\n")
for i in range(n):
    for j in range(m):
        if tableau[j][i] == 1.0:
            file.write(str(tableau[j][-1]))
            file.write("\n")
file.close()
