#https://adventofcode.com/2023/day/2


inputFile = open("input/Day2.txt", "rt")
limit = [12, 13, 14]


def gameStrToListStr(aStr: str):
    """
    vstup: "Game 1: 3 green, 1 blue, 3 red; 3 blue, 1 green, 3 red; 2 red, 12 green, 7 blue; 1 red, 4 blue, 5 green; 7 green, 2 blue, 2 red"
    výstup: ['3 green, 1 blue, 3 red', '3 blue, 1 green, 3 red', '2 red, 12 green, 7 blue', '1 red, 4 blue, 5 green', '7 green, 2 blue, 2 red']
    """
    i = 0
    # přeskočí "Game #: "
    while aStr[i] != ":":
        i += 1
    i += 2

    if aStr[-1] == "\n":
        iSplit = aStr[i:-1].split("; ")  # rozdělí aStr bez "Game #: " a bez "\n"
    else:
        iSplit = aStr[i:].split("; ")  # rozdělí aStr bez "Game #: "
    return iSplit


def listStrToListRGB(aListStr):
    """
    vstup: ['3 green, 1 blue, 3 red', '3 blue, 1 green, 3 red', '2 red, 12 green, 7 blue', '1 red, 4 blue, 5 green', '7 green, 2 blue, 2 red']
    výstup: [[3, 3, 1], [3, 1, 3], [2, 12, 17], [1, 5, 3], [2, 7, 2]]
    """
    RGB = list
    retArr = []
    for cGameSet in aListStr:       # '3 green, 1 blue, 3 red'
        singleRetArr = [0, 0, 0]
        iSplit = cGameSet.split(", ")    # ['3 green', '1 blue', '3 red']
        for cPart in iSplit:    # '3 green'
            cPartSplit = cPart.split(" ")   # ['3', 'green']
            if "red" in cPart:
                singleRetArr[0] = int(cPartSplit[0])
            if "green" in cPart:
                singleRetArr[1] = int(cPartSplit[0])
            if "blue" in cPart:
                singleRetArr[2] = int(cPartSplit[0])
        retArr.append(singleRetArr)

    return retArr


def testGameLims(aRGB: list):
    for i in range(3):
        if aRGB[i] > limit[i]:
            return False
    return True


def main():
    sumID = 0
    validGame = [True] * 100
    for i, cSingleGameInput in enumerate(inputFile):
        singleGame = gameStrToListStr(cSingleGameInput)
        RGB = listStrToListRGB(singleGame)
        OK = bool
        for cSingleSet in RGB:
            OK = testGameLims(cSingleSet)
            if not OK:
                validGame[i] = False
                break

        print(f"GameNo: {i + 1}, GameInput: {cSingleGameInput[:-1]} \t--> RGB: {RGB}; OK: {OK}")

    for j in range(len(validGame)):
        if validGame[j]:
            sumID += j + 1
    print(f"Suma OK ID: {sumID}")
    inputFile.close()


main()
