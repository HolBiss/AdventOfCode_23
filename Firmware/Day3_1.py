import copy

import numpy as np

fileName = "input/Day3.txt"
"""
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def creatMatrixFromFile(aFileName: str):
    with open(aFileName, 'r') as file:
        lines = file.readlines()

    clearLines = [line.strip() for line in lines]

    iDataMatrix = np.array([list(line) for line in clearLines])
    return iDataMatrix


def createNeighbourhood(aMatrix, aIndex):
    lims = [-1, 1, -1, 1]   # +- indexy pro okolí

    # kontrola aby okolí nevylezlo ven z původní matice
    if aIndex[0] == 0:
        lims[0] = 0
    elif aIndex[0] == aMatrix.shape[0]-1:
        lims[1] = 0

    if aIndex[1] == 0:
        lims[2] = 0
    elif aIndex[1] == aMatrix.shape[1]-1:
        lims[3] = 0

    subMatrixIndex = [aIndex[0]+lims[0], aIndex[0]+lims[1]+1, aIndex[1]+lims[2], aIndex[1]+lims[3]+1]   # +1 protože 1:3 vrátí řádky  1, 2

    subMatrix = aMatrix[subMatrixIndex[0]:subMatrixIndex[1], subMatrixIndex[2]:subMatrixIndex[3]]

    return subMatrix


def matrixToLineStr(aMatrix):
    iStr = ""
    for i in np.nditer(aMatrix):    # iterátor přes n rozměrné pole (matici)
        iStr += i
    return iStr


def symbolInNeighbourStr(aStr: str):
    for char in aStr:
        if not char.isalnum() and char != ".":
            return True
    return False


class Number:
    def __init__(self, val, startI, endI):
        self.val = val
        self.startI = startI
        self.endI = endI

    def __str__(self):
        return f"Val: {self.val}, Index: <{self.startI}; {self.endI}>"

    def reset(self):
        self.val = 0
        self.startI = 0
        self.endI = 0


def getNumbersInLine(aRow):
    numbersInLine = []

    started = False
    i = 0
    rowLastIndex = len(aRow) - 1
    while i < rowLastIndex:
        num = Number(0, 0, 0)
        # první číslice v číslu
        if not started and aRow[i].isdigit():
            started = True
            num.val = num.val * 10 + int(aRow[i])
            num.startI = i
            i += 1

        if i >= rowLastIndex:
            break

        # prochází číslici
        while started and aRow[i].isdigit():
            num.val = num.val * 10 + int(aRow[i])
            i += 1
            if i > rowLastIndex:
                break

        # konec číslice
        if started:
            num.endI = i
            numbersInLine.append(num)
            started = False

        # nenašel číslici -> pokračuje se na další
        else:
            i += 1

    return numbersInLine


def main():
    dataMatrix = creatMatrixFromFile(fileName)
    finalParts = []
    for row in range(len(dataMatrix)):
        numbers = getNumbersInLine(dataMatrix[row])

        for num in numbers:
            numIsValid = False
            for i in range(num.startI, num.endI):
                neighbourhood = createNeighbourhood(dataMatrix, [row, i])
                neighbourhoodStr = matrixToLineStr(neighbourhood)
                if symbolInNeighbourStr(neighbourhoodStr):
                    numIsValid = True
                    break

            print(f"Číslo {num.val}\tna řádku {row} a indexu <{num.startI};{num.endI}> je validní: {numIsValid}")

            if numIsValid:
                finalParts.append(num.val)

    sumParts = 0
    for cPart in finalParts:
        sumParts += cPart

    print(f"Seznam součástek: {finalParts}. Jejich součet: {sumParts}")


main()
