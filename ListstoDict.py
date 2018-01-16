name = ["Anna", "Eli", "Pariece", "Brendan", "Amy", "Shane"]
favorite_animal = ["horse", "cat", "spider", "giraffe", "ticks", "dolphins", "llamas"]

def makeDict(list1, list2):
    newDict = {}
    if len(list1) >= len(list2):
        for i in range(0, len(list1)):
            try:
                newDict[list1[i]] = list2[i]
            except IndexError:
                newDict[list1[i]] = None
    else:
        for i in range(0, len(list1)):
            try:
                newDict[list2[i]] = list1[i]
            except IndexError:
                newDict[list2[i]] = None
    return newDict

print makeDict(name, favorite_animal)