# KAEL MURPHY
# CS1026 Lab 8

def makeDicts():
    incomeDict = dict()
    countryDict = dict()

    countryList = []
    gdpList = []
    initialList = []

    with open('lab8.txt', 'r') as fh:
        for line in fh:
            line = line.upper().strip().split(':')
            countryList.append(line[0])
            gdpList.append(line[1])
            initial = line[0][0]
            initialList.append(initial)

    for i in range(len(countryList)):
        incomeDict[countryList[i]] = gdpList[i]
        if initialList[i] not in countryDict:
            countryDict[initialList[i]] = set()
        countryDict[initialList[i]].add(countryList[i])

    return incomeDict, countryDict


incomeDict, countryDict = makeDicts()

userInp = ''

while userInp != 'DONE':

    userInp = input('Enter the name of the country or an initial, or DONE to exit: ')
    userInp = userInp.upper()

    if userInp in incomeDict:
        print('{} has a per capita GDP of {}'.format(userInp, incomeDict[userInp]))
    elif userInp in countryDict:
        print('These countries start with {}: {}'.format(userInp, countryDict[userInp]))
    elif userInp != 'DONE':
        print('Please type in a valid input')
