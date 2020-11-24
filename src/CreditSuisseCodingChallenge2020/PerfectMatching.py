# You may change this function parameters
def calculateMinimumSession(numOfBankers, numOfParticipants, bankersPreferences, participantsPreferences):
    for j in range(numOfParticipants):
        for i in participantsPreferences[j]:
            if j+1 in bankersPreferences[i-1]:
                continue
            else:
                bankersPreferences[i-1].append(j+1)
    ppreferences = [[] for i in range(numOfParticipants)]
    for i in range(numOfBankers):
        for j in bankersPreferences[i]:
            ppreferences[j].append(i + 1)
    return max(max([len(i) for i in bankersPreferences]), max([len(i) for i in ppreferences]))


def main():
    firstLine = input().split(" ")
    secondLine = input().split(" ")
    # Sample input:
    # 3 1,1,1&2
    # 3 3&2,1,1
    numOfBankers = int(firstLine[0])
    numOfParticipants = int(secondLine[0])
    bankersPreferences = firstLine[1].split(",")
    participantsPreferences = secondLine[1].split(",")

    bankersPreferencesListOfList = parsePreferences(bankersPreferences)
    participantsPreferencesListOfList = parsePreferences(participantsPreferences)

    answer = calculateMinimumSession(
        numOfBankers,
        numOfParticipants,
        bankersPreferencesListOfList,
        participantsPreferencesListOfList
    )

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line


def parsePreferences(preferences):
    preferenceListOfList = []
    for index in range(0, len(preferences)):
        preferenceArr = preferences[index].split("&")
        preferenceListOfList.append([int(p) for p in preferenceArr])
    return preferenceListOfList


if __name__ == '__main__':
    main()


"""
2 1,2&3
3 1,2,2

3 1,1,1
3 3,1,1
"""