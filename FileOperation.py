
def readFile(path):
    with open(path, 'r+', encoding="utf-8") as fp:
        allLines = fp.readlines()
    print(allLines)


readFile("C:\\Users\\GJLMoTea\\Desktop\\InverseRPG\\Question")
