# Participants may update the following function parameters
def maximumExpectedMoney(noOfTradesAvailable, maximumTradesAllowed,p,x,y):
    ex = []
    for i in range(noOfTradesAvailable):
        expect = p[i] * x[i] - (1 - p[i]) * y[i]
        if expect > 0:
            ex.append(expect)
    ex.sort(reverse=True)
    res = 0
    for i in range(min(maximumTradesAllowed, len(ex))):
        res += ex[i]
    return round(res, 2)

def main():
    # This part may require participants to fill in as well.
    noOfTradesAvailable, maximumTradesAllowed = list(map(int, input().split()))
    p = list(map(float, input().split()))
    x = list(map(float, input().split()))
    y = list(map(float, input().split()))

    # Participants may update the following function parameters
    answer = maximumExpectedMoney(noOfTradesAvailable, maximumTradesAllowed,p,x,y)
    # Do not remove below line
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()