import math
# You may change this function parameters
def encrypt(words):
    # Participants code will be here
    size = len(words.replace(" ", ""))
    floor = math.floor(math.sqrt(size))
    ceil = math.ceil(math.sqrt(size))
    r, c = 0, 0
    if floor ** 2 >= size:
        r = c = floor
    elif floor * ceil >= size:
        r = floor
        c = ceil
    else:
        r = c = ceil
    res = []
    text = words.replace(" ", "") + " " * (r * c - size)
    for j in range(c):
        s = ""
        for i in range(r):
            s += text[c * i + j]
        res.append(s.strip())
    return " ".join(res)


def main():
    words = input()

    answer = encrypt(words)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line

if __name__ == '__main__':
    main()