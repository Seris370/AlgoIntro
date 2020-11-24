def organizingContainers(container):
    # Participants code will be here
    if len(container) == 0:
        return "Possible"
    r = len(container)
    for i in range(r - 1):
        x = i + 1
        y = i + 1
        while x < r and y < r:
            if container[i][x] > 0 and container[y][i] > 0:
                diff = min(container[i][x], container[y][i])
                container[i][x] -= diff
                container[y][x] += diff
                container[y][i] -= diff
                container[i][i] += diff
            elif container[i][x] == 0:
                x += 1
            else:
                y += 1
            print(container)
        if any(container[i][x:]):
            return "Impossible"
        if any(container[y][i] for y in range(y, r)):
            return "Impossible"
    return "Possible"


if __name__ == "__main__":
    q = int(input().strip())
    answer=""
    for a0 in range(q):
        n = int(input().strip())
        container = []
        for container_i in range(n):
            container_t = [int(container_temp) for container_temp in input().strip().split(' ')]
            container.append(container_t)
        result = organizingContainers(container)
        if(answer == ""):
             answer = str(result)
        else:
            answer = answer +  "," +str(result)
    # Do not remove below line
    print(answer)
    # Do not print anything after this line


"""
2
3
2 4 0
3 0 1
1 0 0
2
1 4
5 4
"""