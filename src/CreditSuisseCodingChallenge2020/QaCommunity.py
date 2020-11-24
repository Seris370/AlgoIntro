import collections
# Participants may update the following function parameters
def findSuspiciousUserId(numOfQuestions, questionAndAnswerListOfList):
    # Participants code will be here
    graph = [[0] for i in range(numOfQuestions + 1)]  # with dummy list at graph[0]
    queue = set()  # dynamic set of suspicious users
    degree = [-1 for i in range(numOfQuestions + 1)]
    res = []
    for question in questionAndAnswerListOfList:
        questioner = question[0]
        answerers = question[1:]
        for answerer in answerers:
            graph[answerer].append(questioner)
    # find mutual Q&A and insert into queue
    for a in range(1, numOfQuestions + 1):
        for q in graph[a]:
            if a in graph[q]:
                queue.add(q)
                queue.add(a)
                degree[q] = 1
                degree[a] = 1
    while queue:
        res.extend(list(queue))
        temp = set()
        for a in queue:
            for q in graph[a]:
                degree[q] += 1
                if degree[q] == 1:
                    temp.add(q)
        queue = temp

    res.sort()
    res = [str(x) for x in res if x != 0]

    return ",".join(res)


def main():
    firstLine = input().split(" ")
    secondLine = input()

    # Sample input:
    # 3
    # 1 2,2 1,3 1 2

    numOfQuestions = int(firstLine[0])
    questionAndAnswers = secondLine.split(",")
    questionAndAnswerListOfList = parseQuestionAndAnswer(questionAndAnswers)

    # Participants may update the following function parameters
    answer = findSuspiciousUserId(numOfQuestions, questionAndAnswerListOfList)

    # Please do not remove the below line.
    print(answer)
    # Do not print anything after this line


def parseQuestionAndAnswer(questionAndAnswers):
    questionAndAnswerListOfList = []
    for index in range(0, len(questionAndAnswers)):
        questionAndAnswerList = questionAndAnswers[index].split(" ")
        questionAndAnswerListOfList.append([int(x) for x in questionAndAnswerList])
    return questionAndAnswerListOfList


if __name__ == '__main__':
    main()


"""
3
1 2,2 1,3 1 2
4
1 2,2 1,3 1 4,4 1 2
4
1 3,3 2 4,4 2,2 4
"""