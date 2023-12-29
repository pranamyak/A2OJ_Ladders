import sys
input = sys.stdin.readline

############ ---- Input Functions ---- ############
def inp():
    return(int(input()))
def inlt():
    return(list(map(int,input().split())))
def insr():
    s = input()
    return(list(s[:len(s) - 1]))
def invr():
    return(map(int,input().split()))
############ ---- Input Functions ---- ############

def Arrival_of_the_General():
    n = inp()
    sequence = inlt()
    max_ht = max(sequence)
    min_ht = min(sequence)

    max_ht_index = []
    min_ht_index = []

    for index,ht in enumerate(sequence):
        if ht == max_ht:
            max_ht_index.append(index) 
        if ht == min_ht:
            min_ht_index.append(index) 
    
    smallest_max_ht_index = min(max_ht_index)
    largest_min_ht_index = max(min_ht_index)

    if smallest_max_ht_index < largest_min_ht_index:
        steps = (smallest_max_ht_index) + (n-1-largest_min_ht_index)
    else:
        steps = (smallest_max_ht_index) + (n-1-largest_min_ht_index) - 1
    
    print(steps)
    return 

def Beautiful_Matrix():
    fullMatrix = []
    for i in range(5):
        fullMatrix.append(inlt())
    
    rowPos = -1
    colPos = -1

    for rowIndex in range(5):
        for colIndex in range(5):
            if fullMatrix[rowIndex][colIndex] == 1:
                rowPos = rowIndex + 1
                colPos = colIndex + 1
                break 

    stepsReqd = abs(3-rowPos) + abs(3-colPos)
    print(stepsReqd)
    return

def Ultra_Fast_Mathematician():
    num1_string = insr()
    num2_string = insr()

    num1 = [int(x) for x in num1_string]
    num2 = [int(x) for x in num2_string]
    # print(num1)
    # print(num2)

    new_string = ['1' if (x+y) == 1 else '0' for x,y in zip(num1,num2)]
    outputStr = ''.join(i for i in new_string)
    print(outputStr)
    return

def Blackjack():
    n = inp()
    possiblePoints = [x for x in range(1,12)]
    possiblePoints.remove(10)

    remainingPoints = n - 10

    if remainingPoints in possiblePoints:
        print(4)
    elif remainingPoints == 10:
        print(15)
    else:
        print(0)
    return 

def HQ9():
    inputList = insr()
    printCommand = ['H','Q','9']

    found = False
    for command in printCommand:
        if command in inputList:
            found = True
        if found:
            break
    
    if found:
        print("YES")
    else:
        print("NO")
    return

def Cookies():
    n = inp()
    bagList = inlt()

    num_odd = 0
    num_even = 0
    totalSum = sum(bagList)

    for cookie in bagList:
        if cookie % 2 == 0:
            num_even += 1
        else:
            num_odd += 1
    
    if totalSum%2 == 0:
        print(num_even)
    else:
        print(num_odd)
    return

def Candy_Bags():
    n = inp()

    bagsList = [x for x in range(1,(n*n)+1)]
    #print(bagsList)
    index_from_front = 0
    index_from_end = len(bagsList)-1

    stop_for_front = (len(bagsList)//2) - 1
    #print(stop_for_front)
    outputStr = ''

    while index_from_front <= stop_for_front:
        for i in range(n//2):
            outputStr += str(bagsList[index_from_front]) + ' '
            index_from_front += 1
        for i in range(n//2):
            outputStr += str(bagsList[index_from_end]) + ' '
            index_from_end -= 1
        outputStr += '\n'
    
    outputStr = outputStr.strip()
    print(outputStr)
    return

def Vasily_the_Bear_and_Triangle():
    x,y = invr()

    x_firstQuad = abs(x)
    y_firstQuad = abs(y)
    a = (x_firstQuad+y_firstQuad)

    if x > 0 and y > 0:
        x1 = 0 
        y1 = a 
        x2 = a
        y2 = 0
    elif x < 0 and y > 0:
        x1 = -a
        y1 = 0
        x2 = 0 
        y2 = a 
    elif x < 0 and y < 0:
        x1 = -a
        y1 = 0
        x2 = 0
        y2 = -a 
    else:
        x1 = 0
        y1 = -a
        x2 = a
        y2 = 0
    
    print(str(x1) + ' ' + str(y1) + ' ' + str(x2) + ' ' + str(y2))
    return

def Lunch_Rush():
    n,k = invr()
    f_values = []
    t_values = []
    joy_values = []

    for i in range(n):
        fi,ti = invr()
        f_values.append(fi)
        t_values.append(ti)
        
        if ti > k:
            joy = fi - (ti - k)
        else:
            joy = fi 
        
        joy_values.append(joy)
    
    joy_values_sorted = sorted(joy_values,reverse=True)
    print(joy_values_sorted[0])
    return
    
def Cakeminator():
    r,c = invr()
    Fullmatrix = []
    infectedRows = []
    infectedColumns = []
    
    rowIndex = 0
    for i in range(r):
        row = insr()
        Fullmatrix.append(row)
        colIndex = 0
        for content in row:
            if content == 'S':
                infectedRows.append(rowIndex)
                infectedColumns.append(colIndex)
            colIndex += 1
        rowIndex += 1
    
    uniqueInfectedRows = list(set(infectedRows))
    uniqueInfectedColumns = list(set(infectedColumns))

    cakeThroughRows = (r - len(uniqueInfectedRows))*c 
    cakeThroughCols = (c - len(uniqueInfectedColumns)) * len(uniqueInfectedRows)

    print(cakeThroughCols+cakeThroughRows)
    return

def Stones_on_the_Table():
    n = inp()
    stoneSequence = insr()
    
    currentPtr = 0
    checkPtr = 0 
    numStonesRemoved = 0

    while checkPtr <= (n-1):
        if checkPtr == currentPtr:
            checkPtr += 1
        
        elif stoneSequence[currentPtr] == stoneSequence[checkPtr]:
            numStonesRemoved += 1
            checkPtr += 1
        else:
            currentPtr = checkPtr

    print(numStonesRemoved)   

def Levko_and_Table():
    n,k = invr()

    outputStr = ''

    diagonalPos = 0
    for rowIndex in range(n):
        row = [0]*n 
        row[diagonalPos] = k 
        diagonalPos += 1 
        rowString = ' '.join(str(x) for x in row)
        outputStr += rowString + '\n'
    
    outputStr = outputStr.strip()
    print(outputStr)
    return

def Young_Physicist():
    n = inp()
    x_coordinate = []
    y_coordinate = []
    z_coordinate = []

    for force in range(n):
        x,y,z = invr()
        x_coordinate.append(x)
        y_coordinate.append(y)
        z_coordinate.append(z)
    
    if sum(x_coordinate) == 0 and sum(y_coordinate) == 0 and sum(z_coordinate) == 0:
        print("YES")
    else:
        print("NO")
    return

def Chips():
    n,m = invr()

    chipsForOneRound = (n*(n+1))//2
    numRounds = m//chipsForOneRound
    chipsForLastRound = m - (chipsForOneRound*numRounds)

    for walrusIndex in range(1,n+1):
        if walrusIndex > chipsForLastRound:
            break 
        else:
            chipsForLastRound -= walrusIndex
    
    print(chipsForLastRound)
    return

def Queue_at_the_School():
    n,t = invr()
    sequence = insr()
    
    for time in range(t):
        currentPtr = 0
        nextPtr = 1
        while nextPtr <= (n-1):
            
            if sequence[currentPtr] == 'B' and sequence[nextPtr] == 'G':
                sequence[currentPtr] = 'G'
                sequence[nextPtr] = 'B'
                currentPtr += 2
                nextPtr = currentPtr + 1
            else:
                currentPtr += 1
                nextPtr = currentPtr + 1

    outputStr = ''.join([x for x in sequence])
    print(outputStr)
    return 

def Slightly_Decreasing_Permutations():
    n,k = invr()

    sequence = [x for x in range(1,n+1)]
    index = n - k - 1 

    if sequence[index] == n:
        outputStr = ' '.join(str(x) for x in sequence)
    else:
        sequence[index] = n 
        decrement = 1 

        for i in range(index+1,n):
            sequence[i] = n - decrement
            decrement += 1
        
        outputStr = ' '.join(str(x) for x in sequence)

    print(outputStr)
    return

def Fancy_Fence():
    t = inp()
    outputStr = ''

    for i in range(t):
        a = inp()
        n = 360/(180-a)

        if n == int(n):
            outputStr += 'YES' + '\n'
        else:
            outputStr += 'NO' + '\n'
    
    outputStr = outputStr.strip()
    print(outputStr)
    
    return 

def Dragons():
    s,n = invr()

    dragonStrength = []
    dragonReward = []

    for i in range(n):
        x,y = invr()
        dragonStrength.append(x)
        dragonReward.append(y)
    
    dragonStrength_sorted = [x for x,y in sorted(zip(dragonStrength,dragonReward))]
    dragonReward_acc = [y for x,y in sorted(zip(dragonStrength,dragonReward))]

    strength = s
    numDefeated = 0
    alive = True
    index = 0
    while (alive) and (numDefeated < n):
        if strength > dragonStrength_sorted[index]:
            strength += dragonReward_acc[index]
            numDefeated += 1
        else:
            alive = False 
        index += 1
    
    if numDefeated == n:
        print("YES")
    else:
        print("NO")
    return
    
def Wizards_and_Demonstration():
    n,x,y = invr()

    c = ((n*y)/100) - x
    
    if c < 0 :
        print(0)
    elif int(c) == c:
        print(int(c))
    else:
        print(int(c)+1)
    return 

def Life_Without_Zeros():
    def stringToNum(stringList):
        num = 0
        power = 0
        for index in range(len(stringList)):
            index_from_behind = len(stringList) - index - 1
            num += int(stringList[index_from_behind])*(10**power)
            power += 1
        return num
    
    def numToStringList(num):
        stringList = []
        while num>0:
            lastDigit = num%10
            stringList.insert(0,str(lastDigit))
            num = num//10
        return(stringList)



    a_sr = insr()
    a_num = stringToNum(a_sr)
    b_sr = insr()
    b_num = stringToNum(b_sr)
    
    add_result_num = a_num + b_num
    add_result_sr = numToStringList(add_result_num)
    #print(a_sr,a_num,b_sr,b_num,add_result_sr,add_result_num)

    a_sr_new = []
    b_sr_new = []
    add_result_sr_new = []

    for digit in a_sr:
        if digit != '0':
            a_sr_new.append(digit)
    
    for digit in b_sr:
        if digit != '0':
            b_sr_new.append(digit)
    
    for digit in add_result_sr:
        if digit != '0':
            add_result_sr_new.append(digit)
    
    a_num_new = stringToNum(a_sr_new)
    b_num_new = stringToNum(b_sr_new)
    add_result_num_new = stringToNum(add_result_sr_new)

    actualNewResult = a_num_new + b_num_new
    if actualNewResult == add_result_num_new:
        print("YES")
    else:
        print("NO")
    return

def Lucky_Division():
    def stringListToNum(stringList):
        num = 0
        power = 0
        for index in range(len(stringList)):
            indexFromBack = len(stringList) - index - 1
            num += int(stringList[indexFromBack])*(10**power)
            power += 1
        return num 
    
    def isLucky(stringList):
        for digit in stringList:
            if digit == '4' or digit == '7':
                continue 
            else:
                return False 
        return True 

    
    num_sr = insr()
    num = stringListToNum(num_sr)

    allPossibleLucky = [4,7,44,77,47,74,444,447,474,744,477,747,774,777]

    if isLucky(num_sr):
        print("YES")
        return
    else:
        found = False 
        for luckyNum in allPossibleLucky:
            if num % luckyNum == 0:
                found = True 
                break 
        
        if found:
            print("YES")
        else:
            print("NO")
        return

def Array():
    n = inp()
    orgArray = inlt()

    set1 = []
    set2 = []
    set3 = []

    num_neg = 0
    num_pos = 0

    for num in orgArray:
        if num < 0 :
            num_neg += 1
        elif num > 0:
            num_pos += 1
    
    if num_pos == 0:
        required_neg_in_set2 = 2
    else:
        required_neg_in_set2 = 0

    required_neg_in_set1 = 1 

    for num in orgArray:
        if num < 0 :
            if required_neg_in_set1 != 0:
                set1.append(num)
                required_neg_in_set1 -= 1

            elif required_neg_in_set2 != 0: 
                set2.append(num)
                required_neg_in_set2 -= 1 

            else:
                set3.append(num) 

        elif num > 0:
            set2.append(num)
        else:
            set3.append(num)

    outputStr = ''

    outputStr += str(len(set1)) + ' '
    for num in set1:
        outputStr += str(num) + ' '
    outputStr += '\n'

    outputStr += str(len(set2)) + ' '
    for num in set2:
        outputStr += str(num) + ' '
    outputStr += '\n'

    outputStr += str(len(set3)) + ' '
    for num in set3: 
        outputStr += str(num) + ' ' 
    outputStr += '\n'

    outputStr = outputStr.strip()
    print(outputStr)
    return 
            
def Sum_of_Digits():
    def numSum(num):
        digit_sum = 0
        while num>0:
            #digit.append(num%10)
            digit_sum += num%10
            num = num//10
        return(digit_sum)
    
    n = inp()
    steps = 0 
    
    currentNum = n
    while currentNum != (currentNum%10):
        currentNum = numSum(currentNum)
        steps += 1
    print(steps)
    return

def Sum_of_Digits2():
    n = input()
    n = n.strip() #has an extra '\n' at the end
    
    steps = 0
    while int(n) >= 10:
        steps += 1
        sum = 0
        for digit in n:
            sum += int(digit)
        n = str(sum)
        n = n.strip()
    print(steps)
         
def k_String():
    k = inp()
    sequence = insr()

    uniqueCharacters = list(set(sequence))
    countDict = {}
    for letter in sequence:
        if letter in countDict.keys():
            countDict[letter] += 1
        else:
            countDict[letter] = 1

    possible = True
    for letter in uniqueCharacters:
        if countDict[letter] % k != 0:
            possible = False 
            break 
    

    if not possible:
        print(-1)
    else:
        onePartString = ''

        for letter in uniqueCharacters:
            numTimes = countDict[letter]//k 
            for i in range(numTimes):
                onePartString += letter
            
        outputStr = onePartString * k 
        print(outputStr)
    return

def Puzzles():
    n,m  = invr()
    pieceSequence = inlt()
    pieceSequence_sorted = sorted(pieceSequence)

    firstPtr = 0
    secondPtr = firstPtr + (n-1)
    smallestDiff = pieceSequence_sorted[secondPtr] - pieceSequence_sorted[firstPtr]
    # print(smallestDiff)
    # print(pieceSequence_sorted)

    while secondPtr <= (m-1):
        currentDiff = pieceSequence_sorted[secondPtr] - pieceSequence_sorted[firstPtr]
        if currentDiff < smallestDiff:
            smallestDiff = currentDiff
        firstPtr += 1
        secondPtr = firstPtr + (n-1) 
    
    print(smallestDiff)
    return

def Next_Test():
    n = inp()
    previousSequence = inlt()
    previousSequence_sorted = sorted(previousSequence)

    for index,value in enumerate(previousSequence_sorted):
        if value != (index + 1):
            print(index+1)
            return
    print(n+1)

def Laptops():
    n = inp()
    priceList = []
    qualityList = []

    for i in range(n):
        p,q  = invr()
        priceList.append(p)
        qualityList.append(q)
    
    priceList_sorted = sorted(priceList)
    qualityList_acc = [y for x,y in sorted(zip(priceList,qualityList))]
    qualityList_sorted = sorted(qualityList)

    if qualityList_sorted == qualityList_acc:
        print("Poor Alex")
    else:
        print("Happy Alex")
    return

def Pashmak_and_Garden():
    x1,y1,x2,y2 = invr()

    if x1 == x2:
        sideLength = y2 - y1
        x3 = x1 + sideLength
        y3 = y1 
        x4 = x2 + sideLength
        y4 = y2 
    elif y1 == y2:
        sideLength = x2 - x1 
        x3 = x1 
        y3 = y1 + sideLength
        x4 = x2 
        y4 = y2 + sideLength
    elif x2 - x1 == y2 - y1:
        sideLength = x2 - x1 
        x3 = x1 
        y3 = y1 + sideLength
        x4 = x2 
        y4 = y2 - sideLength
    elif x2 - x1 == -(y2 - y1):
        sideLength  = x2 - x1 
        x3 = x1 
        y3 = y1 - sideLength
        x4 = x2 
        y4 = y2 + sideLength
    else:
        print(-1)
        return 
    
    print(str(x3) + ' ' + str(y3) + ' ' + str(x4) + ' ' + str(y4))
    return 

def Lucky_Sum():
    import time
    l,r = invr()

    luckyNum = [4,7]

    startLuckyNum = -1 
    if luckyNum[0] >= l and startLuckyNum == -1:
        startLuckyNum = luckyNum[0] 
    if luckyNum[1] >= l and startLuckyNum == -1:
        startLuckyNum = luckyNum[1]

    index = 0
    
    start = time.time()
    while True:        
        num1 = (luckyNum[index]*10)+4
        num2 = (luckyNum[index]*10)+7

        if num1 >= l and startLuckyNum == -1:
            startLuckyNum = num1 
        if num2 >= l and startLuckyNum == -1:
            startLuckyNum = num2 

        if num1 >= r :
            luckyNum.append(num1)
            break  
        else:
            luckyNum.append(num1)
        if num2 >= r:
            luckyNum.append(num2)
            break 
        else:
            luckyNum.append(num2)

        index += 1
    end = time.time()
    print("While loop time:", (end-start))
    
    start = time.time()
    movingIndex = luckyNum.index(startLuckyNum)
    end = time.time()
    print("Indexing time:", end - start)
    
    sum = 0 
    start = time.time() 
    for i in range(l,r+1):
        while luckyNum[movingIndex] < i:
            movingIndex += 1

        sum += luckyNum[movingIndex]
    end = time.time()
    print("For loop time:", end - start)
    print(sum)
    return

def Lucky_Sum2():
    l,r = invr()

    luckyNum = [4,7]

    startLuckyNum = -1 
    if luckyNum[0] >= l and startLuckyNum == -1:
        startLuckyNum = luckyNum[0] 
    if luckyNum[1] >= l and startLuckyNum == -1:
        startLuckyNum = luckyNum[1]

    index = 0
    
    found = False 

    if luckyNum[0] >= r:
        luckyNum.remove(7)
        found = True
    elif luckyNum[1] >= r:
        found = True


    while True:   
        if found:
            break     
        num1 = (luckyNum[index]*10)+4
        num2 = (luckyNum[index]*10)+7

        if num1 >= l and startLuckyNum == -1:
            startLuckyNum = num1 
        elif num2 >= l and startLuckyNum == -1:
            startLuckyNum = num2 

        if num1 >= r :
            luckyNum.append(num1)
            break  
        else:
            luckyNum.append(num1)

        if num2 >= r:
            luckyNum.append(num2)
            break 
        else:
            luckyNum.append(num2)

        index += 1   
    
    # print(len(luckyNum))
    # print(luckyNum)
    # print(startLuckyNum)
    startIndex = luckyNum.index(startLuckyNum)
    # print("start index:", startIndex)
    
    sum = 0 

    if startIndex == len(luckyNum)-1:
        num = luckyNum[startIndex]
        numTimesRepeated = r - l + 1
        sum += num * numTimesRepeated
    else:   
        for movingIndex in range(startIndex,len(luckyNum)):

            num = luckyNum[movingIndex]

            if movingIndex  == startIndex:
                numTimesRepeated = (num - l) + 1 

            elif movingIndex == len(luckyNum)-1:
                prevNum = luckyNum[movingIndex-1]
                numTimesRepeated = (r - (prevNum+1)) + 1
            else:
                prevNum = luckyNum[movingIndex-1]
                numTimesRepeated = (num - (prevNum+1)) + 1
            
            sum += (num*numTimesRepeated)

    print(sum)
    
    return

def Lucky_Sum3():
    l,r = invr()

    luckyNum = [4,7]
    if (luckyNum[0] - l) >= 0 :
        startLuckyNum = luckyNum[0]
    elif (luckyNum[1] - l) >= 0:
        startLuckyNum = luckyNum[1]
    else:
        startLuckyNum = -1 

    index = 0
    while (luckyNum[index] - r) < 0:
        num1 = (luckyNum[index]*10)+4
        num2 = (luckyNum[index]*10)+7

        if (num1 - l) >= 0  and startLuckyNum == -1:
            startLuckyNum = num1 
        elif (num2 - l) >= 0 and startLuckyNum == -1:
            startLuckyNum = num2

        luckyNum.append(num1)
        luckyNum.append(num2)
        index += 1

    startIndex = luckyNum.index(startLuckyNum)
    movingIndex = startIndex

    found_next_r = False
    found_next_l = False
    sum = 0 
    # print(luckyNum, startIndex,startLuckyNum)

    while not found_next_r:
        num = luckyNum[movingIndex] 
        if (num -r) >= 0 and not found_next_l:  #the condtion where r and l fall in the same gap
            numTimesRepeated = r - l + 1
            found_next_r = True

        elif num == startLuckyNum:  
            numTimesRepeated = num - l + 1
            found_next_l = True

        elif (num-r) >= 0:
            found_next_r = True
            prevNum = luckyNum[movingIndex-1] 
            numTimesRepeated = r - prevNum
        else:
            prevNum = luckyNum[movingIndex-1]
            numTimesRepeated = num - prevNum
        
        sum += (num*numTimesRepeated)
        # print(num,numTimesRepeated)
        movingIndex += 1
    
    print(sum)
    return  
         
def Kuriyama_Mirais_Stones():
    n = inp()
    stoneSequence = inlt()
    stoneSequence_sorted = sorted(stoneSequence)

    stoneSequenceSum = []
    stoneSequence_sorted_sum = []

    runningSum = 0
    for stone in stoneSequence:
        runningSum += stone 
        stoneSequenceSum.append(runningSum)

    runningSum = 0
    for stone in stoneSequence_sorted:
        runningSum += stone 
        stoneSequence_sorted_sum.append(runningSum)

    m = inp()
    # print(stoneSequence_sorted_sum)
    # print(stoneSequenceSum)

    outputStr = ''
    for ques in range(m):
        type_of_ques,l,r = invr()

        if type_of_ques == 1:
            if l == 1:
                ans = stoneSequenceSum[r-1]
            else:
                ans = stoneSequenceSum[r-1] - stoneSequenceSum[l-2]
        else:
            if l == 1:
                ans = stoneSequence_sorted_sum[r-1]
            else:
                ans = stoneSequence_sorted_sum[r-1] - stoneSequence_sorted_sum[l-2]
        
        outputStr += str(ans) + '\n'

    outputStr = outputStr.strip()
    print(outputStr)
    return 

def Kitahara_Harukis_Gift():
    n = inp()
    appleList = inlt()

    num100 = appleList.count(100)
    num200 = appleList.count(200)

    if num100 % 2 == 0 and num200 % 2 == 0: #even 100s even 200s case
        print("YES")
    elif num100 % 2 != 0:  #odd 100s even 200s and odd 100s odd 200s case
        print("NO")
    elif num200 % 2 != 0: #even 100s odd 200s case
        if num100 >= 2:
            print("YES")
        else:
            print("NO")
    return

def The_Fibonacci_Segment():
    n = inp()
    integerSequence = inlt()

    largestLength = 0
    currentLength = 0

    ptr1 = 1
    ptr2 = 2
    ptr3 = 3

    while ptr3 <= (n):
        if integerSequence[ptr3-1] == (integerSequence[ptr1-1] + integerSequence[ptr2-1]):
            currentLength += 1
        else:
            currentLength = 0 
        
        if currentLength >= largestLength:
            largestLength = currentLength
        
        ptr1 += 1
        ptr2 += 1
        ptr3 += 1
    
    if largestLength == 0:
        if n == 1:
            print(1)
        else:
            print(2)
    else:
        print(largestLength + 2)
    return

def Difference_Row():
    n = inp()
    sequence = inlt()
    sequence_sorted = sorted(sequence)

    smallest = sequence_sorted[0]
    largest = sequence_sorted[n-1]
    sequence_sorted[0] = largest
    sequence_sorted[n-1] = smallest
    
    outputStr = ''
    for term in sequence_sorted:
        outputStr += str(term) + ' '
    
    outputStr = outputStr.strip()
    print(outputStr)
    return

def Little_Pigs_and_Wolves():
    n,m = invr()
    bigMatrix = []

    for r in range(n):
        row = insr()
        bigMatrix.append(row)
    
    pigsEaten = 0

    for rowIndex in range(n):
        for colIndex in range(m):
            #print(bigMatrix)

            if bigMatrix[rowIndex][colIndex] == 'P':
                foundWolf = False

                if (colIndex-1) >= 0 and not foundWolf:
                    if bigMatrix[rowIndex][colIndex-1] == 'W':
                        foundWolf = True 
                        pigsEaten += 1
                        bigMatrix[rowIndex][colIndex-1] = '.'

                if (colIndex+1) <= (m-1) and not foundWolf:
                    if bigMatrix[rowIndex][colIndex+1] == 'W':
                        foundWolf = True 
                        pigsEaten += 1 
                        bigMatrix[rowIndex][colIndex+1] = '.'
                
                if (rowIndex-1) >= 0 and not foundWolf:
                    if bigMatrix[rowIndex-1][colIndex] == 'W':
                        foundWolf = True 
                        pigsEaten += 1
                        bigMatrix[rowIndex-1][colIndex] = '.'
                
                if (rowIndex+1) <= (n-1) and not foundWolf:
                    if bigMatrix[rowIndex+1][colIndex] == 'W':
                        foundWolf = True 
                        pigsEaten += 1 
                        bigMatrix[rowIndex+1][colIndex] = '.'
    
    print(pigsEaten)
    return

def T_primes():
    import math
    def isprime(num):
        for n in range(2,int(num**0.5)+1):
            if num%n==0:
                return False
        return True
 
    n = inp()
    integerList = inlt()

    for num in integerList:
        sqrt_num = math.sqrt(num)

        if int(sqrt_num) == sqrt_num and (sqrt_num != 1):
            if isprime(int(sqrt_num)):
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    
    return 

def T_primes2():
    import math
    n = inp()
    integerList = inlt()

    maxNum = 10**6
    
    divisorDictCount = {}
    for num in range(1,maxNum+1):
        divisorDictCount[num] = 0 

    for num in range(1,maxNum+1):        
        currentMultiple = num 
        while currentMultiple <= maxNum:
            divisorDictCount[currentMultiple] += 1 
            currentMultiple += num 
    
    for num in integerList:
        sqrt_num = math.sqrt(num)

        if int(sqrt_num) == sqrt_num and sqrt_num != 1:
            if divisorDictCount[int(sqrt_num)] == 2:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    
    return

def T_primes3():
    import math
    import time 
    n = inp()
    integerList = inlt()

    maxNum = 10**6
    divsiorListCount = [1]*maxNum
    
    #start = time.time()
    for num in range(2,maxNum+1):
        if divsiorListCount[num-1] >= 2:  #Already 2 divisors present when itself the num is still not added
            divsiorListCount[num-1] += 1  #Add the num itself as a divisor
            continue                      #No need to update furthur eg 4 will not be prime, so will not be 8,12,16,20,....        
        
        currentMultiple = num
        while currentMultiple <= maxNum:
            divsiorListCount[currentMultiple-1] += 1 
            currentMultiple += num 

    # end = time.time()
    # print("Time for loop:", end-start)
    
    for num in integerList:
        sqrt_num = math.sqrt(num)

        if int(sqrt_num) == sqrt_num and sqrt_num != 1:
            if divsiorListCount[int(sqrt_num)-1] == 2:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
    
    return

def Learning_Languages():

    def dfs(startNode):
        visited[startNode] = True 
        for neighbour in neighbours[startNode]:
            if visited[neighbour] == False:
                dfs(neighbour)
        return 
    
    n,m = invr()
    languageDict = {}
    uniqueLang = set()

    at_least_one_lang_known = False 

    for employee in range(n):
        list1 = inlt()
        list1.pop(0)

        for language in list1:
            at_least_one_lang_known = True 
            uniqueLang.add(language)
            if language not in languageDict.keys():
                languageDict[language] = []
            languageDict[language].append(employee)
    
    uniqueLang = list(uniqueLang)
    #print(languageDict)
    #print(uniqueLang)

    neighbours = {}
    for employee in range(n):
        neighbours[employee] = []

    for language in uniqueLang:
        if len(languageDict[language]) >= 2:
            currentMarker = 0
            nextMarker = 1

            while nextMarker <= (len(languageDict[language]) -1 ):
                node1 = languageDict[language][currentMarker]
                node2 = languageDict[language][nextMarker]

                if node1 not in neighbours.keys():
                    neighbours[node1] = []
                if node2 not in neighbours.keys():
                    neighbours[node2] = []
                
                neighbours[node1].append(node2)
                neighbours[node2].append(node1)

                currentMarker += 1
                nextMarker += 1
    #print(neighbours)
    
    employee_list = [x for x in range(n)]
    visited = [False]*n
    
    connected_components = 0 

    while visited.count(False) != 0:
        startNode = visited.index(False)
        dfs(startNode)
        connected_components += 1
    
    if not at_least_one_lang_known:
        print(n)
    else:
        print(connected_components-1)
    return

def The_Child_and_Toy():
    n,m = invr()
    nodeEnergies = inlt()
    
    neighbours = {}
    for edge in range(m):
        node1,node2 = invr()
        if node1 not in neighbours.keys():
            neighbours[node1-1] = []         #we are indexing the nodes from 0 to n-1 and not from 1 to n
        if node2 not in neighbours.keys():
            neighbours[node2-1] = []
        neighbours[node1-1].append(node2-1)
        neighbours[node2-1].append(node1-1)
    
    cost_of_removal = []
    for node in range(n):
        cost = 0
        for neighbour in neighbours[node]:
            cost += nodeEnergies[neighbour]
        cost_of_removal.append(cost)

    nodesRemoved = 0
    while nodesRemoved <= (n-2):
        minimum = min(cost_of_removal)
        

def The_Child_and_Toy2():
    def remove_node(node):

        visited[node] = True
        cost = 0 

        for neighbor in neighbors_dict[node]:
            if visited[neighbor] == False:
                cost += nodeCost_dict[neighbor]
        
        return cost


    n,m = invr()
    nodeCost = inlt()

    nodeCost_dict = {}

    for i,c in enumerate(nodeCost):
        nodeCost_dict[i+1] = c 

    nodeList = [i for i in range(1,n+1)]

    sorted_data = sorted(zip(nodeCost,nodeList), reverse=True)
    nodeCost_sorted,nodeList_acc = zip(*(sorted_data))
    nodeCost_sorted = list(nodeCost_sorted)
    nodeList_acc = list(nodeList_acc)

    neighbors_dict = {}
    for i in range(1,n+1):
        neighbors_dict[i] = []
    
    for edge in range(m):
        node1,node2 = invr()
        neighbors_dict[node1].append(node2)
        neighbors_dict[node2].append(node1)
    
    visited = [False]*(n+1)

    total_cost = 0

    for node in nodeList_acc:
        cost = remove_node(node)
        total_cost += cost 
    
    print(total_cost)
    return 



def Find_Marble():
    n,s,t = invr()
    swapSequence = inlt()

    steps = 0 
    initialPos = s
    currentPos = s 
    while currentPos != t:
        currentPos = swapSequence[currentPos-1]
        if currentPos == initialPos:
            break 
        steps += 1 
    
    if currentPos == t:
        print(steps)
    else:
        print(-1)

def Free_Cash():
    n = inp()
    
    timeH = []
    timeM = []

    for i in range(n):
        h,m = invr()
        timeH.append(h)
        timeM.append(m)
    
    currentPtr = 0 
    checkPtr = 0
    
    longestSameTime = 0 

    while checkPtr <= (n-1):
        if currentPtr == checkPtr:
            checkPtr += 1 
            currentSameTime = 0

        elif timeH[currentPtr] == timeH[checkPtr] and timeM[currentPtr] == timeM[checkPtr]:
            checkPtr += 1
            currentSameTime += 1
            if currentSameTime > longestSameTime:
                longestSameTime = currentSameTime
        else:
            currentPtr = checkPtr

    print(longestSameTime+1)
    return 

def Roma_and_Changing_Signs():
    n,k = invr()
    seqence = inlt()

    num_pos = []
    num_zero = []
    num_neg = []


    for x in seqence:
        if x>0 :
            num_pos.append(x)
        elif x < 0 :
            num_neg.append(x)
        else:
            num_zero.append(x)

    num_neg_sorted = sorted(num_neg)
    number_of_negatives = len(num_neg)
    
    index = 0
    while (k>=1) and index <= (number_of_negatives-1):
        removedNum = num_neg_sorted.pop(0)
        converted_pos_num = -removedNum
        num_pos.append(converted_pos_num)
        index += 1
        k -= 1
    
    num_pos_sorted = sorted(num_pos)
    # print(num_pos_sorted)
    # print(num_neg_sorted)

    if k >= 1:
        if k % 2 != 0:
            if len(num_zero) == 0:               
                removedNum = num_pos_sorted.pop(0)
                converted_neg_num = -removedNum
                num_neg_sorted.append(converted_neg_num)
    
    # print(num_pos_sorted)
    # print(num_neg_sorted)
    
    totalMaxSum = sum(num_pos_sorted) + sum(num_neg_sorted)
    print(totalMaxSum)
    return

def Roma_and_Changing_Signs2(): 
    n,k = invr()
    sequence = inlt()
    sequence_sorted = sorted(sequence)
    
    index = 0
    while index <= (n-1) and (k >= 1):
        if sequence_sorted[index] > 0 :
            break 
        else:
            sequence_sorted[index] = -sequence_sorted[index]
            k -= 1
            index += 1
    
    if k >= 1:
        if k % 2 != 0:
            sequence_sorted  = sorted(sequence_sorted)
            sequence_sorted[0] = -sequence_sorted[0]
    
    print(sum(sequence_sorted))
    return

def Dreamoon_and_WiFi():
    import math

    actualString = insr()
    receivedString = insr()

    actual_plus_count = 0
    actual_min_count = 0
    received_plus_count = 0
    received_min_count = 0
    received_q_count = 0

    for letter1,letter2 in zip(actualString,receivedString):
        if letter1 == '+':
            actual_plus_count += 1
        else:
            actual_min_count += 1
        if letter2 == '+':
            received_plus_count += 1
        elif letter2 == '-':
            received_min_count += 1
        else:
            received_q_count += 1
    
    remaining_plus_count = actual_plus_count - received_plus_count
    remaining_min_count = actual_min_count - received_min_count

    if remaining_plus_count < 0 or remaining_min_count < 0:
        print(0)
    elif remaining_plus_count == 0 and remaining_min_count == 0:
        print(1)
    else:
        totalPossibilities = 2**received_q_count
        favourablePossibilities = math.comb(received_q_count,remaining_plus_count)
        print(favourablePossibilities/totalPossibilities)
    
    return

def Dima_and_Staircase():
    n = inp()
    current_max_ht = inlt()

    m = inp()
    widths = []
    heights = []
    for i in range(m):
        w,h = invr()
        widths.append(w)
        heights.append(h)
    
    outputStr = ''
    for boxWidth,boxHeight in zip(widths,heights):
        firstPart = current_max_ht[:boxWidth]
        num_stairs_affected = len(firstPart)
        secondPart = current_max_ht[boxWidth:]

        max_of_first_part = max(firstPart)
        
        outputStr += str(max_of_first_part) + '\n'
        new_max = max_of_first_part + boxHeight
        newFirstPart = [new_max]*num_stairs_affected

        current_max_ht = newFirstPart + secondPart
    
    outputStr = outputStr.strip()
    print(outputStr)
    return

def Dima_and_Staircase2():
    n = inp()
    current_stair_ht = inlt()

    m = inp()    
    outputStr=  ''

    for i in range(m):
        boxWidth,boxHeight = invr()

        firstStair_ht = current_stair_ht[0]
        lastStair_ht = current_stair_ht[boxWidth-1]
        max_of_first_part = max(firstStair_ht,lastStair_ht)

        outputStr += str(max_of_first_part) + '\n'
        current_stair_ht[0] = max_of_first_part + boxHeight
    
    outputStr = outputStr.strip()
    print(outputStr)
    return   

def Comparing_Strings():
    string1 = insr()
    string2 = insr()

    string1_unmatched = []
    string2_unmatched = []

    if len(string1) != len(string2):
        print("NO")
    else:
        
        for s1_char,s2_char in zip(string1,string2):
            if s1_char != s2_char:
                string1_unmatched.append(s1_char)
                string2_unmatched.append(s2_char)
        
        if len(string1_unmatched) != 2: 
            print("NO")
        else:
            if string1_unmatched[0] == string2_unmatched[1] and string1_unmatched[1] == string2_unmatched[0]:
                print("YES")
            else:
                print("NO")
    
    return

def Sereja_and_Array():
    n,m = invr()
    array = inlt()
    
    outputStr = ''
    for i in range(m):
        instructions = inlt()

        if instructions[0] == 1:
            array[instructions[1]-1] = instructions[2]
        elif instructions[0] == 2:
            num = instructions[1]
            array = [(x+num) for x in array]
        else:
            outputStr += str(array[instructions[1]-1]) + '\n'
    
    outputStr = outputStr.strip()
    print(outputStr)
    return

def Sereja_and_Array2():
    n,m = invr()
    array = inlt()
    increment = 0
    
    outputStr = ''
    for i in range(m):
        instructions = inlt()

        if instructions[0] == 1:
            array[instructions[1]-1] = instructions[2] - increment    

        elif instructions[0] == 2:
            num = instructions[1]
            increment += num
        else:
            result = array[instructions[1]-1] + increment
            outputStr += str(result) + '\n'
    
    outputStr = outputStr.strip()
    print(outputStr)
    return

def Sereja_and_Suffixes():
    n,m = invr()
    sequence = inlt()
    
    uniqueElementsCount = [0]*n
    uniqueElementsSet = set()
    index_from_back = n-1 

    while index_from_back >= 0:
        uniqueElementsSet.add(sequence[index_from_back])
        uniqueElementsCount[index_from_back] = len(uniqueElementsSet)
        index_from_back -= 1

    outputStr= ''
    for i in range(m):
        li = inp()
        outputStr += str(uniqueElementsCount[li-1]) + '\n'

    outputStr = outputStr.strip()
    print(outputStr)
    return

def Pashmak_and_Flowers():
    import math 
    n = inp()
    flowerBeauty = inlt()
    flowerBeauty_sorted = sorted(flowerBeauty)

    minBeauty = flowerBeauty_sorted[0]
    maxBeauty = flowerBeauty_sorted[n-1]

    flowers_with_minBeauty = flowerBeauty_sorted.count(minBeauty)
    flowers_with_maxBeauty = flowerBeauty_sorted.count(maxBeauty)

    if minBeauty == maxBeauty:
        diff = maxBeauty - minBeauty
        ways = math.comb(n,2)
        print(str(diff) + ' ' + str(ways))
    else:
        diff = maxBeauty - minBeauty
        ways = flowers_with_maxBeauty * flowers_with_minBeauty
        print(str(diff) + ' ' + str(ways))

    return 

def Simple_Molecules():
    a,b,c = invr()
    
    num_of_edges = (a+b+c)/2

    if num_of_edges != int(num_of_edges):
        print("Impossible")
    else:
        x = ((a+b+c)/2) - c 
        y = ((a+b+c)/2) - a 
        z = ((a+b+c)/2) - b  
        
        if x < 0 or y < 0 or z < 0:
            print("Impossible") 
        else:
            print(str(int(x)) + ' ' + str(int(y)) + ' ' + str(int(z)))
    
    return

def Fixed_Points():
    n = inp()
    sequence = inlt()
    
    fixedPoints = 0
    swapFound = False 

    for index in range(n):
        if sequence[index] == index:
            fixedPoints += 1

        elif not swapFound:
            num  = sequence[index]
            if sequence[num] == index:
                swapFound = True 
    
    if swapFound:
        fixedPoints += 2 
    elif fixedPoints != n:
        fixedPoints += 1 
    
    print(fixedPoints)
    return 

def Road_Construction():
    n,m = invr()

    all_cities_count = [0]*n

    for edge_restriction in range(m):
        city1,city2 = invr()
        all_cities_count[city1-1] += 1
        all_cities_count[city2-1] += 1

    city_with_zero_count = all_cities_count.index(0) + 1

    outputStr = ''
    num_roads = 0
    for city in range(1,n+1):
        if city == city_with_zero_count:
            continue 
        else:
            num_roads += 1
            res = str(city) + ' ' + str(city_with_zero_count) + '\n'
            outputStr += res 
    
    startStr= str(num_roads) + '\n'
    outputStr = outputStr.strip()
    outputStr = startStr + outputStr
    print(outputStr)
    return

def Flipping_Game():
    n = inp()
    sequence = inlt()

    currentGain = 0
    maxGainReached = 0
    gains = []

    for index in range(len(sequence)):
        num = sequence[index]
        if num == 0:
            currentGain += 1
            if currentGain > maxGainReached:
                maxGainReached = currentGain

        elif num == 1:

            currentGain -= 1

            if currentGain < 0 : 
                gains.append(maxGainReached)
                currentGain = 0
                maxGainReached = 0
                
    gains.append(maxGainReached)
    print(gains)

def Flipping_Game2():
    n = inp()
    sequence = inlt()

    max_ones = -1
    for i in range(n):
        for j in range(i,n):
            sliced_sequence = sequence[i:j+1]
            before_sequence = sequence[0:i]
            after_sequence = sequence[j+1:]    
            total_ones_after_flipping = sliced_sequence.count(0) + before_sequence.count(1) + after_sequence.count(1)
            if total_ones_after_flipping > max_ones:
                max_ones = total_ones_after_flipping
    
    print(max_ones)
    return

def Flipping_Game3():
    n = inp()
    sequence = inlt()
    gain_sequence = []

    for num in sequence:
        if num == 0 :
            gain_sequence.append(1)
        else:
            gain_sequence.append(-1)
    
    maximalSum_till_that_index = gain_sequence[0] 
    startIndex = 0
    endIndex = 0 
    info_at_that_index = {}

    for index,num in enumerate(gain_sequence):
        if index == 0:
            info_at_that_index[index] = [maximalSum_till_that_index,startIndex,endIndex]
            continue
        else: 
            if maximalSum_till_that_index + num > num:
                maximalSum_till_that_index = maximalSum_till_that_index + num 
                endIndex = index 
                info_at_that_index[index] = [maximalSum_till_that_index,startIndex,endIndex]
            else:
                maximalSum_till_that_index = num 
                startIndex = index 
                endIndex = index 
                info_at_that_index[index] = [maximalSum_till_that_index,startIndex,endIndex]
   
    gloabalMax = gain_sequence[0]
    for index in info_at_that_index.keys():
        if info_at_that_index[index][0]> gloabalMax:
            gloabalMax = info_at_that_index[index][0]
    
    #print(info_at_that_index)
    totalOnes = sequence.count(1)
    resulting_ones_after_flipping = totalOnes + gloabalMax
    print(resulting_ones_after_flipping)
    return

def Ilya_and_Queries():
    string1 = insr()
    n = len(string1)
    binary_converted = []

    for char in string1:
        if char == '.':
            binary_converted.append(0)
        else:
            binary_converted.append(1)
    
    diff = []
    index = 0
    while index <= (n-2):
        diff.append(binary_converted[index] - binary_converted[index+1])
        index += 1
    
    m = inp()
    outputStr = ''
    for i in range(m):
        li,ri = invr()
        sliced_diff = diff[(li-1):(ri-1)]
        res = str(sliced_diff.count(0))
        outputStr += res + '\n'

    outputStr = outputStr.strip() 
    print(outputStr)    
    return

def Ilya_and_Queries2():
    string1 = insr()
    n = len(string1)

    count = []
    index = 0
    while index <= (n-2):
        if string1[index] == string1[index+1]:
            count.append(1)
        else:
            count.append(0)
        index += 1
    
    succesive_sum_of_count = []
    runningSum = 0 
    for c in count:
        runningSum += c 
        succesive_sum_of_count.append(runningSum)
    
    m = inp()
    outputStr = ''
    #print(succesive_sum_of_count)
    for i in range(m):
        li,ri = invr()
        index1 = li - 1 
        index2 = ri - 1 
        
        if index1 == 0:
            res = succesive_sum_of_count[index2-1]
        else:
            res = succesive_sum_of_count[index2-1] - succesive_sum_of_count[index1-1] 

        outputStr += str(res) + '\n'
    
    outputStr = outputStr.strip()
    print(outputStr)
    return

def Little_Dima_and_Equation():
    def convertToDigits(num):
        digits = []

        while num > 0 :
            digit = num % 10
            num = num // 10
            digits.append(digit)
        return digits
        
    a,b,c = invr()
    
    solutions = []
    max_sum = 81
    
    for digits_sum in range(1,max_sum+1):
        
        x =b*(digits_sum**a) + c

        if x > 0 and x < 10**9:
            
            digits = convertToDigits(x)
            if sum(digits) == digits_sum:
                solutions.append(x)

    solutions_sorted = sorted(solutions)
    print(len(solutions_sorted))
    #print(solutions_sorted)
    outputStr = ' '.join(str(x) for x in solutions_sorted)
    print(outputStr)
    return

def George_and_Job():
    def modified_knapsack(sum_of_m_consective,current_index,remaining_weight,memoization_matrix):
        if remaining_weight == 0:
            return 0 
        if current_index >= len(sum_of_m_consective):
            return 0
        
        if memoization_matrix[remaining_weight][current_index] != -1:
            return memoization_matrix[remaining_weight][current_index]
        
        profit1 = modified_knapsack(sum_of_m_consective,current_index+1,remaining_weight,memoization_matrix)
        profit2 = sum_of_m_consecutive[current_index] + modified_knapsack(sum_of_m_consective,current_index+m,remaining_weight-1,memoization_matrix)
        result = max(profit1,profit2)
        memoization_matrix[remaining_weight][current_index] = result
        return result
    
    n,m,k = invr()
    sequence = inlt()
 
    sum_of_m_consecutive = []
 
    first_sum = 0
    for index in range(0,m):
        first_sum += sequence[index]
    sum_of_m_consecutive.append(first_sum)
 
    changing_sum = first_sum
    window_start_index = 0 + (1)
    window_end_index = m-1 + (1)
 
    while window_end_index <= (n-1):
        changing_sum  = changing_sum - sequence[window_start_index-1] + sequence[window_end_index]
        sum_of_m_consecutive.append(changing_sum)
        window_start_index += 1
        window_end_index += 1 
    
    #print(sum_of_m_consecutive)
 
    memoization_matrix = []
    for i in range(k+1):
        list1 = [-1]*len(sum_of_m_consecutive) 
        memoization_matrix.append(list1)
    answer = modified_knapsack(sum_of_m_consecutive,0,k,memoization_matrix)
    print(answer)
    return 

def George_and_Job2():
    from types import GeneratorType
    def bootstrap(f, stack=[]):
        def wrappedfunc(*args, **kwargs):
            if stack:
                return f(*args, **kwargs)
            else:
                to = f(*args, **kwargs)
                while True:
                    if type(to) is GeneratorType:
                        stack.append(to)
                        to = next(to)
                    else:
                        stack.pop()
                        if not stack:
                            break
                        to = stack[-1].send(to)
                return to
        return wrappedfunc

    @bootstrap
    def modified_knapsack(sum_of_m_consective,current_index,remaining_weight,memoization_matrix):
        if remaining_weight == 0:
            yield 0 
        if current_index >= len(sum_of_m_consective):
            yield 0
        
        if memoization_matrix[remaining_weight][current_index] != -1:
            yield memoization_matrix[remaining_weight][current_index]
        
        profit1 = yield modified_knapsack(sum_of_m_consective,current_index+1,remaining_weight,memoization_matrix)
        profit2 = sum_of_m_consecutive[current_index] + (yield modified_knapsack(sum_of_m_consective,current_index+m,remaining_weight-1,memoization_matrix))
        result = max(profit1,profit2)
        memoization_matrix[remaining_weight][current_index] = result
        yield result
    
    n,m,k = invr()
    sequence = inlt()

    sum_of_m_consecutive = []
 
    first_sum = 0
    for index in range(0,m):
        first_sum += sequence[index]
    sum_of_m_consecutive.append(first_sum)

    changing_sum = first_sum
    window_start_index = 0 + (1)
    window_end_index = m-1 + (1)

    while window_end_index <= (n-1):
        changing_sum  = changing_sum - sequence[window_start_index-1] + sequence[window_end_index]
        sum_of_m_consecutive.append(changing_sum)
        window_start_index += 1
        window_end_index += 1 
    
    #print(sum_of_m_consecutive)

    memoization_matrix = []
    for i in range(k+1):
        list1 = [-1]*len(sum_of_m_consecutive) 
        memoization_matrix.append(list1)
    answer = modified_knapsack(sum_of_m_consecutive,0,k,memoization_matrix)
    print(answer)
    return 

def George_and_Job3():
    n,m,k = invr()
    sequence = inlt()

    sum_of_m_consecutive = []
 
    first_sum = 0
    for index in range(0,m):
        first_sum += sequence[index]
    sum_of_m_consecutive.append(first_sum)
 
    changing_sum = first_sum
    window_start_index = 0 + (1)
    window_end_index = m-1 + (1)
 
    while window_end_index <= (n-1):
        changing_sum  = changing_sum - sequence[window_start_index-1] + sequence[window_end_index]
        sum_of_m_consecutive.append(changing_sum)
        window_start_index += 1
        window_end_index += 1
        
    number_of_windows = len(sum_of_m_consecutive) #number_of_windows mean number_of_items
    weight_list = [1]*number_of_windows

    dp_matrix = []
    for row_index in range(number_of_windows+1):
        row = [-1]*(k+1)
        dp_matrix.append(row)
    
    for row_index in range(number_of_windows+1):
        for col_index in range(k+1):
            if row_index == 0 or col_index == 0:
                dp_matrix[row_index][col_index] = 0 
            else:
                if weight_list[row_index-1] > col_index:
                    dp_matrix[row_index][col_index] = dp_matrix[row_index-1][col_index]
                else:
                    profit1 = dp_matrix[row_index-1][col_index]
                    if row_index - m < 0 :
                        profit2 = sum_of_m_consecutive[row_index-1]
                    else:
                        profit2 = sum_of_m_consecutive[row_index-1] + dp_matrix[row_index-m][col_index-weight_list[row_index-1]]                   

                    dp_matrix[row_index][col_index] = max(profit1,profit2)

    
    print(dp_matrix[number_of_windows][k])
    return

def George_and_Job4():
    n,m,k = invr()
    sequence = inlt()

    sum_of_m_consecutive = []
 
    first_sum = 0
    for index in range(0,m):
        first_sum += sequence[index]
    sum_of_m_consecutive.append(first_sum)
 
    changing_sum = first_sum
    window_start_index = 0 + (1)
    window_end_index = m-1 + (1)
 
    while window_end_index <= (n-1):
        changing_sum  = changing_sum - sequence[window_start_index-1] + sequence[window_end_index]
        sum_of_m_consecutive.append(changing_sum)
        window_start_index += 1
        window_end_index += 1
        
    number_of_windows = len(sum_of_m_consecutive) #number_of_windows mean number_of_items
    weight_list = [1]*number_of_windows

    dp_matrix_mrows = []
    for row_index in range(m+1):
        row = [-1]*(k+1)
        dp_matrix_mrows.append(row)
    
    for row_index in range(number_of_windows+1):
        for col_index in range(k+1):
            if row_index == 0 :
                dp_matrix_mrows[(row_index)][col_index] = 0 
            elif col_index == 0:
                dp_matrix_mrows[((row_index)%(m+1))][col_index] = 0 
            else:
                if weight_list[row_index-1] > col_index:
                    dp_matrix_mrows[(row_index % (m+1))][col_index] = dp_matrix_mrows[((row_index-1)%(m+1))][col_index]
                else:
                    profit1 = dp_matrix_mrows[((row_index-1)%(m+1))][col_index]
                    if row_index - m < 0 :
                        profit2 = sum_of_m_consecutive[(row_index-1)]
                    else:
                        profit2 = sum_of_m_consecutive[row_index-1] + dp_matrix_mrows[((row_index-m)%(m+1))][col_index-weight_list[row_index-1]]                   

                    dp_matrix_mrows[(row_index%(m+1))][col_index] = max(profit1,profit2)

    
    print(dp_matrix_mrows[(number_of_windows%(m+1))][k])
    return

def Sereja_and_Bottles():
    n = inp()
    a = []
    b = []
    dict_b_count = {}

    for i in range(n):
        ai,bi = invr()
        a.append(ai)
        b.append(bi)

        if bi not in dict_b_count.keys():
            dict_b_count[bi] = 0 
        
        dict_b_count[bi] += 1 

    unique_bi = list(set(b))

    notOpened = 0
    for index,ai in enumerate(a):
        if ai in unique_bi:
            if dict_b_count[ai] == 1:
                if ai == b[index]:
                    notOpened += 1
        else:
            notOpened += 1 
    
    print(notOpened)
    return

def Routine_Problem():
    #import time 
    def compute_hcf(num1,num2):
        if num1 == 0:
            return num2 
        if num2 == 0:
            return num1
        smaller_num = min(num1,num2)
        hcf = 1

        for i in range(1,smaller_num+1):
            if num1 % i == 0 and num2 % i == 0:
                hcf = i 
        return hcf
   
    a,b,c,d = invr()
    
    emptySpace1 = (a*b) - ((b*b*c)/d)
    emptySpace2 = (a*b) - ((a*a*d)/c)

    if emptySpace2 < 0 :
        Nr = (a*b*d) - (b*b*c)
        Dr = (a*b*d)
        hcf_2nums = compute_hcf(Nr,Dr)
        Nr_new = Nr//hcf_2nums
        Dr_new = Dr//hcf_2nums

    elif emptySpace1 < 0: 
        Nr = (a*b*c) - (a*a*d)
        Dr = (a*b*c)
        #start = time.time()
        hcf_2nums = compute_hcf(Nr,Dr)
        #end = time.time() 
        #print(end-start)
        Nr_new = Nr//hcf_2nums
        Dr_new = Dr//hcf_2nums
    
    elif emptySpace1 < emptySpace2:
        Nr = (a*b*d) - (b*b*c)
        Dr = (a*b*d)
        hcf_2nums = compute_hcf(Nr,Dr)
        Nr_new = Nr//hcf_2nums
        Dr_new = Dr//hcf_2nums

    elif (emptySpace2 <= emptySpace1):
        Nr = (a*b*c) - (a*a*d)
        Dr = (a*b*c)
        hcf_2nums = compute_hcf(Nr,Dr)
        Nr_new = Nr//hcf_2nums
        Dr_new = Dr//hcf_2nums


    print(str(Nr_new)+'/'+str(Dr_new))
    return 

def Routine_Problem2():
    def compute_hcf(num1,num2):
        if num1 == 0:
            return num2 
        if num2 == 0:
            return num1
        
        if num1 < num2:
            x = num2 
            y = num1 
        else:
            x = num1 
            y = num2 
        
        while(y):
            x, y = y, x % y
        return x    

    a,b,c,d = invr()
    
    emptySpace1 = (a*b) - ((b*b*c)/d)
    emptySpace2 = (a*b) - ((a*a*d)/c)

    if emptySpace2 < 0 :
        Nr = (a*b*d) - (b*b*c)
        Dr = (a*b*d)
        hcf_2nums = compute_hcf(Nr,Dr)
        Nr_new = Nr//hcf_2nums
        Dr_new = Dr//hcf_2nums

    elif emptySpace1 < 0: 
        Nr = (a*b*c) - (a*a*d)
        Dr = (a*b*c)
        #start = time.time()
        hcf_2nums = compute_hcf(Nr,Dr)
        #end = time.time() 
        #print(end-start)
        Nr_new = Nr//hcf_2nums
        Dr_new = Dr//hcf_2nums
    
    elif emptySpace1 < emptySpace2:
        Nr = (a*b*d) - (b*b*c)
        Dr = (a*b*d)
        hcf_2nums = compute_hcf(Nr,Dr)
        Nr_new = Nr//hcf_2nums
        Dr_new = Dr//hcf_2nums

    elif (emptySpace2 <= emptySpace1):
        Nr = (a*b*c) - (a*a*d)
        Dr = (a*b*c)
        hcf_2nums = compute_hcf(Nr,Dr)
        Nr_new = Nr//hcf_2nums
        Dr_new = Dr//hcf_2nums


    print(str(Nr_new)+'/'+str(Dr_new))
    return 

def Hamburgers():
    def possible(num_hamburgers,num_B,num_S,num_C,nb,ns,nc,pb,ps,pc,r):
        extra_B_required = (num_hamburgers*num_B) - nb
        extra_S_required = (num_hamburgers*num_S) - ns
        extra_C_required = (num_hamburgers*num_C) - nc 

        if extra_B_required < 0 :
            extra_B_required = 0
        if extra_S_required < 0:
            extra_S_required = 0
        if extra_C_required < 0:
            extra_C_required = 0
        
        money_required = (extra_B_required*pb) + (extra_C_required*pc) + (extra_S_required*ps)
        if money_required > r:
            return False 
        else:
            return True 

    string_list = insr()
    num_B = string_list.count('B')
    num_S = string_list.count('S')
    num_C = string_list.count('C')

    nb,ns,nc = invr()
    pb,ps,pc = invr()
    r = inp()

    max_humbergers = 10**13

    left_index = 1
    right_index = max_humbergers

    while left_index <= right_index:
        mid = (left_index + right_index)//2

        if possible(mid,num_B,num_S,num_C,nb,ns,nc,pb,ps,pc,r):
            left_index = mid + 1
        else:
            right_index = mid - 1
    
    if possible(mid,num_B,num_S,num_C,nb,ns,nc,pb,ps,pc,r):
        print(mid)
    else:
        print(mid-1)

def Jzzhu_and_Sequences():
    x,y = invr()
    n = inp()

    if n%3 == 0:
        if (n//3) % 2 == 0:
            ans = -(y-x)
        else:
            ans = (y-x)
    else:
        if (n//3) % 2 == 0:
            if n%3 == 1:
                ans = x 
            else:
                ans = y 
        else:
            if n%3 == 1:
                ans = -x 
            else:
                ans = -y 

    modulo = (10**9) + 7 
    print(ans%modulo)
    return

def Flag_Day():
    n,m = invr()
    dress_code = [-1]*n

    for i in range(m):
        d1,d2,d3 = invr()
        available_dresses = [1,2,3]

        if dress_code[d1-1] == -1 and dress_code[d2-1] == -1 and dress_code[d3-1] == -1:
            dress_code[d1-1] = available_dresses[0]
            dress_code[d2-1] = available_dresses[1]
            dress_code[d3-1] = available_dresses[2]

        elif dress_code[d1-1] != -1 :
            available_dresses.remove(dress_code[d1-1])
            dress_code[d2-1] = available_dresses[0]
            dress_code[d3-1] = available_dresses[1]
        
        elif dress_code[d2-1] != -1:
            available_dresses.remove(dress_code[d2-1])
            dress_code[d1-1] = ava

def Valera_and_Fruits():
    n,v = invr()
    
    num_fruits_acc_to_day_dict = {}

    for i in range(n):
        ai,bi = invr()
        if ai not in num_fruits_acc_to_day_dict.keys():
            num_fruits_acc_to_day_dict[ai] = bi
        else:
            num_fruits_acc_to_day_dict[ai] += bi 

    prev_day_remaining_fruits = 0
    total_collection = 0

    for day in range(1,3002):   #day can go from 1 to 3001 and on 3001, 3000th remaining fruits can be collected
        if day not in num_fruits_acc_to_day_dict.keys():
            space_in_bag = v 
            
            if prev_day_remaining_fruits <= space_in_bag:
                fruits_collected = prev_day_remaining_fruits
                space_in_bag -= fruits_collected
            
            else:
                fruits_collected = space_in_bag
                space_in_bag = 0
                
            prev_day_remaining_fruits = 0
            total_collection += fruits_collected
        
        else:
            fruits = num_fruits_acc_to_day_dict[day]
            space_in_bag = v

            if prev_day_remaining_fruits <= space_in_bag: 
                fruits_collected = prev_day_remaining_fruits
                space_in_bag -= fruits_collected

            else:
                fruits_collected = space_in_bag
                space_in_bag = 0 

            if fruits <= space_in_bag:
                fruits_collected += fruits
                prev_day_remaining_fruits = 0
            else:
                fruits_collected += space_in_bag
                prev_day_remaining_fruits = fruits - space_in_bag
        
            total_collection += fruits_collected

    
    print(total_collection)
    return

def Fox_Dividing_Cheese():
    def power_of_2(num):
        power = 0

        while num % 2 == 0:
            power += 1
            num = num//2 
        
        return power
    
    def power_of_3(num):
        power = 0 
        
        while num % 3 == 0:
            power += 1 
            num = num//3

        return power 
    
    def power_of_5(num):
        power = 0 

        while num % 5 == 0:
            power += 1 
            num = num//5 
        
        return power 
    
    a,b = invr()
    a1 = power_of_2(a)
    a2 = power_of_3(a)
    a3 = power_of_5(a)
    b1 = power_of_2(b)
    b2 = power_of_3(b)
    b3 = power_of_5(b)
    
    #print(a1,a2,a3,b1,b2,b3)
    partial_num_a = (2**a1)*(3**a2)*(5**a3)
    partial_num_b = (2**b1)*(3**b2)*(5**b3)
    x = a//partial_num_a
    y = b//partial_num_b

    if x != y:
        print(-1)
        return 
    else:
        power_of_2_dist = abs(a1-b1)
        power_of_3_dist = abs(a2-b2)
        power_of_5_dist = abs(a3-b3)
        print(power_of_2_dist + power_of_3_dist + power_of_5_dist)
        return

def Dima_and_Continuous_Line():
    n = inp()
    points_sequence = inlt()

    prev_point = 0 
    semicircle_endPoint1 = []
    semicircle_endPoint2 = []

    for i in range(n):
        xi = points_sequence[i]
        if i == 0 :
            prev_point = xi 
        else:
            if xi < prev_point:
                semicircle_endPoint1.append(xi)
                semicircle_endPoint2.append(prev_point)
            else:
                semicircle_endPoint1.append(prev_point)
                semicircle_endPoint2.append(xi)
            
            prev_point = xi 
    
    semicircle_index = len(semicircle_endPoint1)

    for i in range(semicircle_index):
        for j in range(i+1,semicircle_index):
            
            x1 = semicircle_endPoint1[i]
            x2 = semicircle_endPoint2[i]
            x3 = semicircle_endPoint1[j]
            x4 = semicircle_endPoint2[j]

            if (x1<x3) and (x3<x2) and (x2<x4):
                print("yes")
                return 
            if (x3<x1) and (x1<x4) and (x4<x2):
                print("yes")
                return 
    
    print("no")
    return

def Lucky_Numbers_easy():
    def superLucky(luckyNum):
        num_4 = 0
        num_7 = 0
        while luckyNum > 0:

            digit = luckyNum % 10
            if digit == 4:
                num_4 += 1
            elif digit == 7:
                num_7 += 1

            luckyNum = luckyNum//10
        
        if num_4 == num_7:
            return(True)
        else:
            return(False)


    n = inp()
    lucky_nums = [4,7]

    pointer = 0 
    while(True): 
        newNum1 = (lucky_nums[pointer]*10)+4
        if newNum1 >= n and superLucky(newNum1):
            print(newNum1)
            return 
        
        newNum2 = (lucky_nums[pointer]*10)+7
        if newNum2 >= n and superLucky(newNum2):
            print(newNum2)
            return 
        
        pointer += 1
        lucky_nums.append(newNum1)
        lucky_nums.append(newNum2)

def Coach():
    def do_dfs(startNode,path):
        visited[startNode-1] = True 
        path.append(startNode)
        
        if startNode in neighbours.keys():
            for node in neighbours[startNode]:
                if visited[node-1] == False:
                    do_dfs(node,path)
        
        return path

    n,m = invr()
    
    neighbours = {}
    for i in range(m):
        node1,node2 = invr()
        if node1 not in neighbours.keys():
            neighbours[node1] = []
        if node2 not in neighbours.keys():
            neighbours[node2] = []
        
        neighbours[node1].append(node2)
        neighbours[node2].append(node1)

    visited = [False]*n
    distict_nodes = [x for x in range(1,n+1)]  #1 to n

    three_nodes = []
    two_nodes = []
    one_node = []

    while(True):
        if False in visited:
            unvisited_node = visited.index(False) + 1 
            path = []
            path_obtained = do_dfs(unvisited_node,path)

            if len(path_obtained) > 3:
                print(-1)
                return 
            elif len(path_obtained) == 3:
                three_nodes.append(path_obtained)
            elif len(path_obtained) == 2:
                two_nodes.append(path_obtained)
            else:
                one_node.append(path_obtained)

        else:
            break
    
    if len(two_nodes) > len(one_node):
        print(-1)
        return 
    else:
        outputStr = ''
        for i in three_nodes:
            outputStr += str(i[0]) + ' ' + str(i[1]) + ' ' + str(i[2]) +'\n'

        index = 0
        while index <= len(two_nodes)-1:
            outputStr += str(two_nodes[index][0]) + ' ' + str(two_nodes[index][1]) + ' ' + str(one_node[index][0]) + '\n'
            index += 1 
        
        while index <= len(one_node)-1:
            outputStr += str(one_node[index][0]) + ' ' + str(one_node[index+1][0]) + ' ' + str(one_node[index+2][0]) + '\n'
            index += 3
        
        outputStr = outputStr.strip()
        print(outputStr)
        return

def Ciel_and_Flowers():
    r,g,b = invr()
    minimum_flowers = min(r,g,b)

    zero_mixing_count = (r//3) + (g//3) + (b//3)
    one_mixing_count = 0 
    two_mixing_count = 0

    if minimum_flowers >= 1:
        one_mixing_count = 1 + ((r-1)//3) + ((g-1)//3) + ((b-1)//3)
    
    if minimum_flowers >= 2:
        two_mixing_count = 2 + ((r-2)//3) + ((g-2)//3) + ((b-2)//3)
    
    print(max(zero_mixing_count,one_mixing_count,two_mixing_count))
    return 

def k_Tree():
    def num_paths(remaining_sum, traversed,d,k):
        
        if remaining_sum < 0:
            return 0 
        elif remaining_sum < d and not traversed:
            return 0  
        elif remaining_sum == 0 and traversed:
            return 1 
        elif dp_matrix[remaining_sum][traversed] != -1:
            return dp_matrix[remaining_sum][traversed]
        else:
            total_paths = 0
            for i in range(1,k+1):

                traversed_condition = traversed or (i>=d)
                paths_added = num_paths(remaining_sum-i, traversed_condition,d,k)

                if (remaining_sum - i) >= 0 and (remaining_sum-i) <= n:
                    dp_matrix[remaining_sum-i][traversed_condition] = paths_added

                total_paths += paths_added
            #print(total_paths)
            return total_paths

    n,k,d = invr()
    dp_matrix = []
    for i in range(n+1):
        row = [-1,-1]
        dp_matrix.append(row)

    total_paths = num_paths(n,False,d,k)
    print(total_paths%1000000007)
    return

def Maximum_Absurdity():
    print(1)
    return

def Fixing_Typos():
    stringList = insr()

    answerList = []

    for char in stringList:
        if len(answerList) <= 1:
            answerList.append(char)
        else:
            current_answer_length = len(answerList)
            typoFound = False 

            if answerList[current_answer_length-1] == answerList[current_answer_length-2] and char == answerList[current_answer_length-1]:
                typoFound = True 
            
            if current_answer_length >= 3:
                if answerList[current_answer_length-2] == answerList[current_answer_length-3] and char == answerList[current_answer_length-1]:
                    typoFound = True 

            if not typoFound:
                answerList.append(char)


    outputStr = ''.join(i for i in answerList)
    print(outputStr)
    return 

def Exams():
    n = inp()

    a = []
    b = []
    for i in range(n):
        ai,bi = invr()
        a.append(ai)
        b.append(bi)
    
    a_sorted = [x for x,y in sorted(zip(a,b))]
    b_acc = [y for x,y in sorted(zip(a,b))]

    current_day = -1 

    for a,b in zip(a_sorted,b_acc):
        least_day_at_which_exam_can_be_taken = min(a,b)

        if least_day_at_which_exam_can_be_taken >= current_day:
            current_day = least_day_at_which_exam_can_be_taken
        else:
            if least_day_at_which_exam_can_be_taken == a:
                current_day = b 
            else:
                current_day = a 
    
    print(current_day)
    return 

def Boredom():
    n = inp()
    sequence = inlt()
    max_element = max(sequence)

    count_dict = {}
    for num in sequence:
        if num not in count_dict.keys():
            count_dict[num] = 0
        count_dict[num] += 1
    
    profit = [-1]*(max_element+1)
    profit[0] = 0 
    
    if 1 in count_dict.keys():
        profit[1] = 1*count_dict[1]
    else:
        profit[1] = 0 
    
    for item in range(2,max_element+1):
        if item in count_dict.keys():
            item_not_considered = profit[item-2] + (count_dict[item]*item)
        else:
            item_not_considered = profit[item-2]
        
        item_considered = profit[item-1]
        profit[item] = max(item_not_considered,item_considered)
    
    print(profit[max_element])
    return         

def Prime_Matrix():
    max_num = 10**5
    divisorCountList = [1]*max_num

    for i in range(2,max_num+1):
        if divisorCountList[i-1] >= 2:
            divisorCountList[i-1] += 1
            continue
        
        currentNum = i
        while currentNum <= max_num:
            divisorCountList[currentNum-1] += 1
            currentNum += i
    
    n,m = invr()
    input_matrix = []
    add_matrix = []

    for i in range(n):

        row = inlt()
        input_matrix.append(row)
        add_row = []

        for num in row:
            addition = 0
            while(True):
                new_num = num + addition
                
                if (new_num) > (max_num-1):
                    add_row.append((10**5) + 1)
                 
                elif divisorCountList[new_num-1] == 2:
                    add_row.append(addition)
                    break
                
                addition += 1
        
        add_matrix.append(add_row)
    
    # print(input_matrix)
    # print(add_matrix)

    row_sum = []
    for row in add_matrix:
        row_sum.append(sum(row))
    
    col_sum = []
    for col_index in range(m):
        col = [row[col_index] for row in add_matrix]
        col_sum.append(sum(col))
    
    print(min(min(row_sum),min(col_sum)))
    return

def Books():
    n,t = invr()
    timeSequence = inlt()

    booksRead = []

    startIndex = 0
    stopIndex = startIndex

    totalTime = 0

    exceeded = False
    while stopIndex <= (n-1):
        totalTime += timeSequence[stopIndex]
        if totalTime > t:
            exceeded = True
            break 
        stopIndex += 1 
    
    if exceeded:
        totalTime -= timeSequence[stopIndex]
        stopIndex -= 1
    else:
        stopIndex -= 1

    booksRead.append(stopIndex - startIndex + 1)
    #print(booksRead)

    for startIndex in range(1,n):
        #print("-"*100)
        
        elementRemoved = timeSequence[startIndex-1]
        totalTime = totalTime - elementRemoved

        stopIndex += 1 

        exceeded = False
        while stopIndex <= (n-1):
            totalTime += timeSequence[stopIndex]
            if totalTime > t:
                exceeded = True
                break 
            stopIndex += 1
        
        if exceeded:
            totalTime -= timeSequence[stopIndex]
            stopIndex -= 1 
        else:
            stopIndex -= 1

        booksRead.append(stopIndex - startIndex + 1) 
        #print(booksRead)
    

    
    print(max(booksRead))   
    return

def Little_Girl_and_Maximum_Sum():
    n , q = invr()
    sequence = inlt()
    sequence_sorted = sorted(sequence, reverse=True)

    index_count = [0]*n

    for i in range(q):
        l,r = invr()

        for index in range(l-1,r):
            index_count[index] += 1
    
    index_count_sorted = sorted(index_count, reverse=True)

    totalSum = 0 
    for count,element in zip(index_count_sorted,sequence_sorted):
        totalSum += element*count 
    
    print(totalSum)
    return 

#Little_Girl_and_Maximum_Sum()
#Books()
#Prime_Matrix()                                #NOT COMPLETED - TIME LIMIT EXCEEDED
#Boredom()
#Exams()
#Fixing_Typos()
#Maximum_Absurdity()                            #NOT COMPLETED - SOME FORM OF KNAPSACK
#k_Tree()
#Ciel_and_Flowers()
#Coach()
#Lucky_Numbers_easy()
#Dima_and_Continuous_Line()
#Fox_Dividing_Cheese()
#Valera_and_Fruits()    
#Flag_Day()                                #NOT COMPLETED   
#Jzzhu_and_Sequences()
#Hamburgers()
#Routine_Problem2()
#Routine_Problem()                          #TIME LIMIT EXCEEDED, INEFFICEINT WAY TO GET HCF
#Sereja_and_Bottles()
#George_and_Job4()                            #Time limit exceeded, NOT SOLVED, ####IT HAS BEEN ACCEPETED BY HANDLING m=1 CASE SEPARATELY, SEE CODEFORCES ACCEPTED SOLUTION
#George_and_Job3()                           #memory limit exceeded, instead of matrix, use a row as we are accesing only the m prev rows everytime
#George_and_Job2()                           #gives time limit exceeded error
#George_and_Job()                            #Gives recursion depth error(run time error), used bootstrap and yield modifications in 2, ref: https://codeforces.com/blog/entry/80158
#Little_Dima_and_Equation()
#Ilya_and_Queries2()
#Ilya_and_Queries()
#Flipping_Game3()                           #O(n) time
#Flipping_Game2()                          #O(n^3) time   
#Flipping_Game()                          #Wrong Approach
#Road_Construction()    
#Fixed_Points()
#Simple_Molecules()
#Pashmak_and_Flowers()
#Sereja_and_Suffixes()
#Sereja_and_Array2()
#Sereja_and_Array()
#Comparing_Strings()
#Dima_and_Staircase2()
#Dima_and_Staircase()                       ##TIME LIMIT EXCEEDED
#Dreamoon_and_WiFi()
#Roma_and_Changing_Signs2()                 #COMPLETED IN 186ms
#Roma_and_Changing_Signs()                 #GETS SUBMITTED BUT TAKES A LARGER TIME 1808ms
#Free_Cash()    
#Find_Marble()
#The_Child_and_Toy()                       ##NOT COMPLETED  
The_Child_and_Toy2()      
#Learning_Languages()
#T_primes3()
#T_primes2()                                ##TIME LIMIT EXCEEDED  
#T_primes()                                 ##TIME LIMIT EXCEEDED  
#Little_Pigs_and_Wolves()
#Difference_Row()    
#The_Fibonacci_Segment()    
#Kitahara_Harukis_Gift()
#Kuriyama_Mirais_Stones()    
#Lucky_Sum3()   
#Lucky_Sum2()
#Lucky_Sum()
#Pashmak_and_Garden()  
#Laptops()
#Next_Test()
#Puzzles()
#k_String()
#Sum_of_Digits2()
#Sum_of_Digits()                      ##TIME LIMIT EXCEEDED  
#Array()
#Lucky_Division()
#Life_Without_Zeros()
#Wizards_and_Demonstration()
#Dragons()
#Fancy_Fence()
#Slightly_Decreasing_Permutations()     ##NOT COMPLETED --question not clear
#Queue_at_the_School()
#Chips()    
#Young_Physicist()
#Levko_and_Table()
#Bit++()                                ##present in L11, L11.py has function Bit()
#Stones_on_the_Table()
#Cakeminator()
#Lunch_Rush()
#Vasily_the_Bear_and_Triangle()
#Drinks()                                ##present in L11
#Candy_Bags()
#Cookies()
#Petya_and_Strings()                      ##present in L11
#I_love_\%username\%                      ##present in L11
#HQ9()
#Blackjack()
#Ultra_Fast_Mathematician()
#Beautiful_Matrix()
#Arrival_of_the_General()

#ctrl + k ctrl + j to expand the code fragments
#ctrl + k ctrl + 0 to collapse the code fragments