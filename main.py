from random import randint

def randomName():
    s = "a"
    for num in range(1, randint(2, 4)):
        s = s + "a"

    return s

def randomContent():
    s = "\""
    for num in range(1, randint(2, 2000)):
        s = s + "a"
    return s

def randomPath(maxDepth):
    s = "/"
    for num in range(1, randint(2, 2 + maxDepth)):
        s = s + randomName() + "/"

    s = s[0:-1]
    return s

def randomFunction(maxDepth):
    instruction = randint(0, 6)
    s = ""
    if instruction == 0:
        s = "create " + randomPath(maxDepth)
    if instruction == 1:
        s = "create_dir " + randomPath(maxDepth)
    if instruction == 2:
        s = "read " + randomPath(maxDepth)
    if instruction == 3:
        s = "write " + randomPath(maxDepth) + " " + randomContent()
    if instruction == 4:
        s = "delete " + randomPath(maxDepth)
    if instruction == 5:
        s = "delete_r " + randomPath(maxDepth)
    if instruction == 6:
        s = "find " + randomName()
    return s

def generateTestCase():
    for num in range(0, 100000000):
        print(randomFunction(int(100)))
    print("exit")

generateTestCase()