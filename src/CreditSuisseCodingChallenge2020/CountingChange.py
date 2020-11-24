# Participants may update the following function parameters
def countNumberOfWays(numOfUnits, numOfCoinTypes, coins):
    dp = [[0 for x in range(numOfCoinTypes)] for x in range(numOfUnits + 1)]
    for i in range(numOfCoinTypes):
        dp[0][i] = 1
    coins.sort()

    for unit in range(1, numOfUnits + 1):
        for i in range(numOfCoinTypes):
            pick = dp[unit - coins[i]][i] if unit - coins[i] >= 0 else 0
            unpick = dp[unit][i - 1] if i >= 1 else 0
            dp[unit][i] = pick + unpick

    return dp[numOfUnits][numOfCoinTypes - 1]


def main():
    firstLine = input().split(" ")
    secondLine = input().split(" ")

    numOfUnits = int(firstLine[0])
    numOfCoinTypes = int(firstLine[1])
    coins = list(map(int, secondLine))

    # Participants may update the following function parameters
    answer = countNumberOfWays(numOfUnits, numOfCoinTypes, coins)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()


"""
12 4
2 3 4 5

"""