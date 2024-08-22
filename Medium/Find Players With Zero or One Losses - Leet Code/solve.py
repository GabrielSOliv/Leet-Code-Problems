def findWinners(matches: list[list[int]]) -> list[list[int]]:
    hmWin = {}
    hmLost = {}
    hmLostOnce = {}

    for i in range(len(matches)):
        if matches[i][0] not in hmLost and matches[i][0] not in hmLostOnce:
            hmWin[matches[i][0]] = 1
        
        if matches[i][1] in hmWin:
            hmWin.pop(matches[i][1])

        if matches[i][1] not in hmLostOnce:
            if matches[i][1] not in hmLost:
                hmLostOnce[matches[i][1]] = 1
        else:
            hmLostOnce.pop(matches[i][1])
            hmLost[matches[i][1]] = 2

    return [sorted(list(hmWin.keys())), sorted(list(hmLostOnce.keys()))]


print(findWinners([[1,5],[2,5],[2,8],[2,9],[3,8],[4,7],[4,9],[5,7],[6,8]]))
