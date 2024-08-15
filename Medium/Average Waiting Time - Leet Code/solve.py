example1 = [[5,2],[5,4],[10,3],[20,1]]

def averageWaitingTime(customers: list[list[int]]) -> float:
    averageTime = []
    waintingTime = 0
    currentTime = 0
    for i in range(len(customers)):
        if currentTime < customers[i][0]:
            currentTime = 0
            
        if currentTime == 0:
            waintingTime = (customers[i][0] + customers[i][1]) - customers[i][0]
            averageTime.append(waintingTime)
            currentTime = customers[i][0] + customers[i][1]
        else:
            waintingTime = (currentTime + customers[i][1]) - customers[i][0]
            averageTime.append(waintingTime)
            currentTime = currentTime + customers[i][1]
    
    waintingTime = 0
    
    for i in range(len(averageTime)):
        waintingTime += averageTime[i]

    waintingTime = waintingTime / len(averageTime)

    return waintingTime
    
print(averageWaitingTime(example1))
