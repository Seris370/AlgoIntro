import sys
# You may change this function parameters
def findMaxProfit(numOfPredictedDay, predictedSharePrices):
    # Participants code will be here
    if numOfPredictedDay < 2:
        return 0
    res = predictedSharePrices[1] - predictedSharePrices[0]
    min = predictedSharePrices[0]
    for i in range(1, numOfPredictedDay):
        if predictedSharePrices[i] - min > res:
            res = predictedSharePrices[i] - min
        if predictedSharePrices[i] < min:
            min = predictedSharePrices[i]
    return res


def main():
    line = input().split()
    numOfPredictedDay = int(line[0])
    predictedSharePrices = list(map(int, line[1:]))

    answer = findMaxProfit(numOfPredictedDay, predictedSharePrices)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()
