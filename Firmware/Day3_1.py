import numpy as np

inputFile = open("input/Day3_test.txt")
"""
467..114..
...*......
..3...633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""


def createDataMatrix(aFile):
    iDataMatrix = []
    for row, cLine in enumerate(aFile):
        dataRow = []
        for col, char in enumerate(cLine):
            dataRow.append(char)
        iDataMatrix.append(dataRow[:-1])
    return iDataMatrix


def createSubMatrix(aMatrix, aIndex):
    iSubMatrix = np.zeros((3, 3), dtype=str)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                iSubMatrix[i][j] = " "
                continue
            iSubMatrix[i][j] = aMatrix[aIndex[0]-1+i][aIndex[1]-1+j]
    return iSubMatrix


def subMatrixToStr(aMatrix):
    iStr = ""
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                iStr += ""
                continue
            iStr += str(aMatrix[i][j])
    return iStr


def symbolInNeighbour(aMatrix):
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            if not aMatrix[i][j].isalnum() and aMatrix[i][j] != ".":
                return True
    return False


def main():
    dataMatrix = createDataMatrix(inputFile)
    subMatrix = []
    sameNumber = False

    print(dataMatrix)

    for row in range(len(dataMatrix)):
        for col in range(len(dataMatrix[row])):
            if 0 < row < len(dataMatrix)-1 and 0 < col < len(dataMatrix[row]):  # Prochází vše kromě hranice matice
                if "0" < dataMatrix[row][col] < "9":    # narazil na číslo
                    validNumber = False
                    subMatrix = createSubMatrix(dataMatrix, [row, col]) # vytvoří 3x3 submatici kolem čísla

                    # zjistí jestli je na řádku soused taky číslice = je to pokračování stejného čísla
                    if subMatrix[1][0].isdigit() or subMatrix[1][2].isdigit():
                        sameNumber = True

                    # vypíše všechny sousedy
                    neighbours = subMatrixToStr(subMatrix)
                    if symbolInNeighbour(subMatrix):
                        validNumber = True
                    print(f"znak: {dataMatrix[row][col]} = Pokračování čísla: {sameNumber} --> sousedé: {neighbours} - Platné číslo: {validNumber}")
                    print(f"{subMatrix}\n")









main()
