# You may change this function parameters
def findMaxProfit(numOfPredictedTimes, predictedSharePrices):
    # Participants code will be here
    if numOfPredictedTimes < 2:
        return 0
    res = 0
    min = predictedSharePrices[0]
    for i in range(1, numOfPredictedTimes):
        if predictedSharePrices[i] > min:
            res = res + predictedSharePrices[i] - min
            min = predictedSharePrices[i]

        if predictedSharePrices[i] < min:
            min = predictedSharePrices[i]
    return res

def main():
    line = input().split()
    numOfPredictedTimes = int(line[0])
    predictedSharePrices = list(map(int, line[1:]))

    answer = findMaxProfit(numOfPredictedTimes, predictedSharePrices)
    # Do not remove below line
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()