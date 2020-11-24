def find_min_days(prices, profit):
    # Participants code will be here
    res = []
    preds = list(enumerate(prices))
    preds.sort(key=lambda x: x[1])
    size = len(preds)
    for target in profit:
        if size < 2 and target != 0:
            res.append("-1")
            continue
        i = 0
        j = 1
        min = (0, float('inf'))
        while i < size and j < size:
            if i != j and preds[j][1] - preds[i][1] == target:
                if preds[j][0] - preds[i][0] > 0:
                    if preds[j][0] < min[1] or (preds[j][0] == min[1] and preds[i][0] > min[0]):
                        min = (preds[i][0], preds[j][0])
                i += 1
            elif preds[j][1] - preds[i][1] < target:
                j += 1
            else:
                i += 1
        if min[1] == float('inf'):
            res.append("-1")
        else:
            min = [str(min[0] + 1), str(min[1] + 1)]
            res.append(" ".join(min))
    s = ",".join(res)
    return s

n, d = map(int, input().split())
prices = list(map(int, input().split()))
profit = list()
for i in range(d):
    profit.append(int(input().strip()))
answer = find_min_days(prices,profit)
# Do not remove below line
print(answer)
# Do not print anything after this line

"""
6 2
3 1 2 1 4 5
3
2

6 2
3 6 9 8 2 4
5
2
"""
