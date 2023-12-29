# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


####################################################################
# Ladder 1 : Q1
# a = input()
#
# x_dir = []
# y_dir = []
# z_dir = []
# for i in range(int(a)):
#     cord = input()
#     cord = cord.split(' ')
#     x_dir.append(int(cord[0]))
#     y_dir.append(int(cord[1]))
#     z_dir.append(int(cord[2]))
#
# x_sum = sum(x_dir)
# y_sum = sum(y_dir)
# z_sum = sum(z_dir)
# if (x_sum==0) and (y_sum==0) and (z_sum==0):
#     print("YES")
# else:
#     print("NO")
############################################################################

# Ladder 2: Q2
# import numpy as np
# dimensions = (5,5)
# a = np.zeros(dimensions)
# rowi = 0
# columni = 0
#
# for i in range(5):
#     row = input()
#     row = row.split(' ')
#     for j in range(5):
#         if int(row[j]) == 1:
#             rowi = i+1
#             columni = j+1
#
#
# print((abs(3-rowi))+(abs(3-columni)))
###################################################

# Lights Out
# import numpy as np

# Lights Out
# import numpy as np
#
# inmat = []
# for i in range(3):
#   a = input()
#   l1 = list(a.split(" "))
#   l2 = []
#   for element in l1:
#     l2.append(int(element))
#   inmat.append(l2)
#
# instatus = np.ones((3,3))
#
# rows = len(inmat)
# columns = len(inmat[0])
#
# for i in range(rows):
#   for j in range(columns):
#
#     sum = inmat[i][j]
#
#     if (i-1) >= 0:
#       sum += inmat[i-1][j]
#     if (i+1) < rows :
#       sum += inmat[i+1][j]
#     if (j-1) >= 0:
#       sum += inmat[i][j-1]
#     if (j+1) < columns:
#       sum += inmat[i][j+1]
#
#     if (sum % 2) != 0 :
#       instatus[i][j] = 0
#
# for i in range(rows):
#   print("\n")
#   for j in range(columns):
#     print(int(instatus[i][j]) , end ="" )


# list1 = [2,3,4]
# list1.reverse()
# print(list1)

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

def Panoramixs_Prediction():
    def nextPrime(n):

        increment = 1
        while True:
            newNum = n + increment
            nextPrimeNum = newNum
            isPrime = True

            for i in range(2, newNum):
                if newNum % i == 0:
                    isPrime = False
                    break
            if isPrime:
                return (nextPrimeNum)
            else:
                increment += 1

    list_of_num = input()
    list_of_num = list_of_num.split(' ')
    firstPrimeNum = int(list_of_num[0])
    secondNum = int(list_of_num[1])
    nextPrimeNum = nextPrime(firstPrimeNum)

    if secondNum == nextPrimeNum:
        print("YES")
    else:
        print("NO")
    # print(firstPrimeNum,secondNum)
    # print(nextPrime(13))

def Ultra_Fast_Mathematician():
    def convert(string):
        list1 = []
        list1[:0] = string
        return list1

    BitString1 = input()
    BitString1 = convert(BitString1)
    BitString2 = input()
    BitString2 = convert(BitString2)

    stringOutput = ''
    for i in range(len(BitString1)):
        if BitString1[i] == BitString2[i]:
            stringOutput = stringOutput + '0'
        else:
            stringOutput = stringOutput + '1'

    print(stringOutput)

def Perfect_Permutation():
    permutLength = int(input())
    strOutput = ''
    listOutput = []
    if permutLength % 2 != 0:
        strOutput = strOutput + '-1'
    else:
        i = 0
        while i < permutLength:
            num = i + 1
            listOutput.append(num + 1)
            listOutput.append(num)
            i += 2
        for j in listOutput:
            strOutput = strOutput + str(j) + ' '

    print(strOutput)

def Arrival_of_the_General():
    totalSoldiers = int(input())
    sequenceSoldiers = input()
    sequenceSoldiers = sequenceSoldiers.split(' ')
    for i in range(len(sequenceSoldiers)):
        sequenceSoldiers[i] = int(sequenceSoldiers[i])

    minHeight = min(sequenceSoldiers)
    maxHeight = max(sequenceSoldiers)
    minIndices = [i for i, x in enumerate(sequenceSoldiers) if x == minHeight]
    maxIndices = [i for i, x in enumerate(sequenceSoldiers) if x == maxHeight]
    maxIndex_closest_to_start = min(maxIndices)
    minIndex_closest_to_end = max(minIndices)

    if maxIndex_closest_to_start > minIndex_closest_to_end:
        number_of_swaps = (maxIndex_closest_to_start - 0) + (len(sequenceSoldiers) - minIndex_closest_to_end - 1) - (1)
    else:
        number_of_swaps = (maxIndex_closest_to_start - 0) + (len(sequenceSoldiers) - minIndex_closest_to_end - 1)
    print(number_of_swaps)
    # print(minIndex_closest_to_end, maxIndex_closest_to_start)
    # print(sequenceSoldiers)

def Drinks():                              #suppose take x portion of each drink then orange juice portion: ((x*p1) + (x*p2) + ...) / ((x+x+...))
    number_of_drinks = int(input())
    volume_fraction_orange = input()
    volume_fraction_orange = volume_fraction_orange.split(' ')
    sum_of_fractions = 0
    for i in range(len(volume_fraction_orange)):
        volume_fraction_orange[i] = int(volume_fraction_orange[i]) / 100
        sum_of_fractions += volume_fraction_orange[i]

    final_volume_fraction = sum_of_fractions / number_of_drinks
    print(final_volume_fraction * 100)

def Insomnia_cure():
    k = int(input())
    l = int(input())
    m = int(input())
    n = int(input())
    d = int(input())

    affected_dragons = []
    dragon_start_count = 1
    if k == 1 or l == 1 or m == 1 or n == 1:
        print(d)
    else:
        for dragon_index in range(dragon_start_count, d + 1):
            # print(affected_dragons)
            if dragon_index not in affected_dragons:
                if ((dragon_index % k == 0) or (dragon_index % l == 0) or (dragon_index % m == 0) or (
                        dragon_index % n == 0)):
                    affected_dragons.append(dragon_index)
        print(len(affected_dragons))

def Cupboards():
    totalCupboards = int(input())
    left_door_position = []
    right_door_position = []

    for i in range(totalCupboards):
        cupboard_position = input()
        cupboard_position = cupboard_position.split(' ')
        left_door_position.append(int(cupboard_position[0]))
        right_door_position.append(int(cupboard_position[1]))

    left_door_open_count = 0
    for i in left_door_position:
        if i == 1:
            left_door_open_count += 1

    right_dor_open_count = 0
    for i in right_door_position:
        if i == 1:
            right_dor_open_count += 1

    left_door_time = min(left_door_open_count, totalCupboards - left_door_open_count)
    right_door_time = min(right_dor_open_count, totalCupboards - right_dor_open_count)
    print(left_door_time + right_door_time)

def I_love_username():
    total_contests = int(input())
    scoreSequence = input()
    scoreSequence = scoreSequence.split(' ')

    for i in range(len(scoreSequence)):
        scoreSequence[i] = int(scoreSequence[i])
    # print(scoreSequence)
    amazingPerformance = 0
    contest_number = 0
    scores_till_now = [scoreSequence[0]]
    for i in scoreSequence:
        # print(scores_till_now)
        if contest_number == 0:
            contest_number += 1
            continue
        else:
            minimum_till_now = min(scores_till_now)
            maximum_till_now = max(scores_till_now)
            scores_till_now.append(i)
            if (i > maximum_till_now) or (i < minimum_till_now):
                amazingPerformance += 1

    print(amazingPerformance)

def Tram():
    number_of_stops = int(input())

    enteringPassengers = []
    exitingPassengers = []
    for i in range(number_of_stops):
        enter_exit_info = input()
        enter_exit_info = enter_exit_info.split(' ')
        enteringPassengers.append(int(enter_exit_info[1]))
        exitingPassengers.append(int(enter_exit_info[0]))

    maxCapacity = 0
    current_capacity = 0
    for i in range(len(enteringPassengers)):
        current_capacity = current_capacity - exitingPassengers[i]
        current_capacity = current_capacity + enteringPassengers[i]
        if maxCapacity < current_capacity:
            maxCapacity = current_capacity

    print(maxCapacity)

def Helpful_Maths():
    question_string = input()
    numbers_in_question = question_string.split('+')
    for i in range(len(numbers_in_question)):
        numbers_in_question[i] = int(numbers_in_question[i])
    numbers_in_question.sort()

    strOutput = ''

    for i in numbers_in_question:
        strOutput = strOutput + str(i) + '+'

    strOutput = strOutput[:-1]
    print(strOutput)

def Is_your_horseshoe_on_the_other_hoof():
    horseshoe_color_index = input()
    horseshoe_color_index = horseshoe_color_index.split(' ')
    for i in range(len(horseshoe_color_index)):
        horseshoe_color_index[i] = int(horseshoe_color_index[i])

    all_different_colors = set(horseshoe_color_index)
    print(len(horseshoe_color_index) - len(all_different_colors))

def Way_Too_Long_Words():
    def convert(string):
        list1 = []
        list1[:0] = string
        return list1

    number_of_words = int(input())
    for i in range(number_of_words):
        word = input()
        list_word = convert(word)

        if len(list_word) > 10:
            strOutput = ''
            strOutput = strOutput + list_word[0] + str(len(list_word) - 2) + list_word[len(list_word) - 1]
            print(strOutput)
        else:
            print(word)

def Boy_or_Girl():
    def convert(string):
        list1 = []
        list1[:0] = string
        return list1

    username = input()
    list_username_letters = convert(username)
    distinct_letters = set(list_username_letters)

    if len(distinct_letters) % 2 == 0:
        print("CHAT WITH HER!")
    else:
        print("IGNORE HIM!")

def Amusing_Joke():
    def convert(string):
        list1 = []
        list1[:0] = string
        return list1

    guestName = input()
    residenceHost = input()
    jumbledSentence = input()
    guestName_list = convert(guestName)
    residenceHost_list = convert(residenceHost)
    jumbledSentence_list = convert(jumbledSentence)

    can_be_formed = True

    for i in guestName_list:
        if i not in jumbledSentence_list:
            can_be_formed = False
            break
        else:
            jumbledSentence_list.remove(i)

    for i in residenceHost_list:
        if i not in jumbledSentence_list:
            can_be_formed = False
            break
        else:
            jumbledSentence_list.remove(i)

    if (not can_be_formed) or (len(jumbledSentence_list) != 0):
        print("NO")
    else:
        print("YES")

def Soft_Drinking():
    n_k_l_c_d_p_nl_np = input()
    n_k_l_c_d_p_nl_np = n_k_l_c_d_p_nl_np.split(' ')
    totalFriends = int(n_k_l_c_d_p_nl_np[0])

    totalBottles = int(n_k_l_c_d_p_nl_np[1])
    mm_in_each_bottle = int(n_k_l_c_d_p_nl_np[2])
    total_mm = totalBottles * mm_in_each_bottle

    totalLimes = int(n_k_l_c_d_p_nl_np[3])
    pieces_of_each_lime = int(n_k_l_c_d_p_nl_np[4])
    totalPieces = totalLimes * pieces_of_each_lime

    totalSalt = int(n_k_l_c_d_p_nl_np[5])

    mm_required = int(n_k_l_c_d_p_nl_np[6])
    toast_by_mm = total_mm / mm_required

    limeSlice_required = 1
    toast_by_limeSlice = totalPieces / limeSlice_required

    saltGrams_required = int(n_k_l_c_d_p_nl_np[7])
    toast_by_salt = totalSalt / saltGrams_required

    minimum_toasts = min(toast_by_salt, toast_by_mm, toast_by_limeSlice)
    totalToasts = minimum_toasts // totalFriends
    print(int(totalToasts))

def HQ9():
    def convert(string):
        list1 = []
        list1[:0] = string
        return list1

    strInput = input()
    list_of_characters = convert(strInput)
    output_instruction_list = ["H", "Q", "9"]

    validInstruction = False
    for i in list_of_characters:
        if i in output_instruction_list:
            validInstruction = True
            break

    if validInstruction:
        print("YES")
    else:
        print("NO")

def Petya_and_Strings():
    strInput1 = input()
    strInput1_lower = strInput1.lower()
    strInput2 = input()
    strInput2_lower = strInput2.lower()

    if strInput1_lower > strInput2_lower:
        print("1")
    elif strInput1_lower < strInput2_lower:
        print("-1")
    else:
        print("0")

def Team():
    number_of_problems = int(input())
    solved_problems = 0
    for i in range(number_of_problems):
        surity_string = input()
        surity_string = surity_string.split(' ')

        count = 0
        for i in surity_string:
            if i == '1':
                count += 1

        if (count > 1):
            solved_problems += 1

    print(solved_problems)

def Bit():
    x = 0
    number_of_statements = int(input())
    for i in range(number_of_statements):
        statement = input()
        statement_operation = statement.split("X")
        if '++' in statement_operation:
            x += 1
        else:
            x -= 1
    print(x)

def Effective_Approach():  #This gives run time complexity, because linear search every query
    number_of_elements_in_array = int(input())
    array_input = input()
    array_input = array_input.split(' ')
    for i in range(len(array_input)):
        array_input[i] = int(array_input[i])

    number_of_queries = int(input())
    queryString = input()
    queryString = queryString.split(' ')
    for i in range(len(queryString)):
        queryString[i] = int(queryString[i])

    vasyaApproach = 0
    petyaApproach = 0
    #print(queryString)
    for query in queryString:
        index = array_input.index(query)
        #print(index)
        vasyaApproach += (index + 1)
        petyaApproach += number_of_elements_in_array - index

    print("{} {}".format(vasyaApproach,petyaApproach))

def Effective_Approach2(): #Imrpoved time efficiency by using a dictionary instead of linear search everytime
    number_of_elements_in_array = int(input())
    array_input = input()
    array_input = array_input.split(' ')

    value_to_index_dict = {}
    index_in_array = 0
    for i in range(len(array_input)):
        array_input[i] = int(array_input[i])
        value_to_index_dict[array_input[i]] = index_in_array
        index_in_array += 1

    number_of_queries = int(input())
    queryString = input()
    queryString = queryString.split(' ')
    for i in range(len(queryString)):
        queryString[i] = int(queryString[i])

    vasyaApproach = 0
    petyaApproach = 0
    #print(queryString)
    for query in queryString:

        postion_in_main_array = value_to_index_dict[query]
        vasyaApproach += (postion_in_main_array + 1)
        petyaApproach += number_of_elements_in_array - postion_in_main_array

    print("{} {}".format(vasyaApproach,petyaApproach))

def Dima_and_Friends():
    number_of_friends = int(input()) + 1
    finger_shown_list = input()
    finger_shown_list = finger_shown_list.split(' ')
    total_sum_of_fingers = 0
    for i in range(len(finger_shown_list)):
        finger_shown_list[i] = int(finger_shown_list[i])
        total_sum_of_fingers += finger_shown_list[i]

    Dima_fingers = []
    for i in range(1,6):
        if ((i+total_sum_of_fingers) % number_of_friends != 1):
            Dima_fingers.append(i)

    print(len(Dima_fingers))

def Jzzhu_and_Children():
    strInput1 = input()
    strInput1 = strInput1.split(' ')
    total_children = int(strInput1[0])
    candy_each_gets = int(strInput1[1])

    strInput2 = input()
    each_student_minimum = strInput2.split(' ')
    each_student_minimum = [eval(i) for i in each_student_minimum]

    index = 0

    while max(each_student_minimum) != 0:
        #print(each_student_minimum)
        if each_student_minimum[index] != 0:
            each_student_minimum[index] = max(0, (each_student_minimum[index]- candy_each_gets))
        index = (index + 1) % total_children

    if (index == 0):
        print(total_children)
    else:
        print(index)

def Supercentral_Point():
    number_of_points = int(input())
    x_coord = []
    y_coord = []
    for i in range(number_of_points):
        coordinates_input = input()
        coordinates_input = coordinates_input.split(' ')
        x_coord.append(int(coordinates_input[0]))
        y_coord.append(int(coordinates_input[1]))



    x_coord_count_dict = {}
    y_coord_count_dict = {}

    for i in x_coord:
        if i not in x_coord_count_dict.keys():
            x_coord_count_dict[i] = x_coord.count(i)

    for j in y_coord:
        if j not in y_coord_count_dict.keys():
            y_coord_count_dict[j] = y_coord.count(j)

    supercentralPoints = 0
    print(x_coord_count_dict)
    print(y_coord_count_dict)
    print(number_of_points)
    for i in range(number_of_points):
        if x_coord_count_dict[x_coord[i]] > 1 :
            supercentralPoints += 1
        elif y_coord_count_dict[y_coord[i]] > 1:
            supercentralPoints += 1

    print(supercentralPoints)

def Petr_and_Book():
    total_pages = int(input())
    pages_read_each_day = input().split(' ')
    pages_read_each_day = [eval(i) for i in pages_read_each_day]

    pages_read_in_one_week = sum(pages_read_each_day)
    last_week_pages = total_pages % pages_read_in_one_week

    last_non_zero_element = 7
    for i in range(7):
        i = 6 - i
        if pages_read_each_day[i] == 0:
            last_non_zero_element -= 1
        else:
            break

    for i in range(len(pages_read_each_day) + 1):
        if last_week_pages == 0:
            if i == 0 :
                print(last_non_zero_element)
            else:
                print(i)
            break
        else:

            last_week_pages = max(0,last_week_pages - pages_read_each_day[i])
            i += 1
            #print(last_week_pages, i)
            #print(i)

def Parallelepiped():
    import math
    area_of_3_sides = input().split(' ')
    area_of_3_sides = [eval(i) for i in area_of_3_sides]
    xy = area_of_3_sides[0]
    yz = area_of_3_sides[1]
    xz = area_of_3_sides[2]

    x = math.sqrt((xy*xz)/yz)
    y = math.sqrt((yz*xy)/xz)
    z = math.sqrt((yz*xz)/xy)

    sum_of_all_edges = (x+y+z)*4
    print(int(sum_of_all_edges))

def Reconnaissance_2():
    number_of_soldiers = int(input())
    height_of_soldiers = input().split(' ')
    height_of_soldiers = [eval(i) for i in height_of_soldiers]

    soldier1 = 0
    soldier2 = 1
    minimum_height = abs(height_of_soldiers[soldier1] - height_of_soldiers[soldier2])
    minimum_height_index = [soldier1, soldier2]

    soldier1 += 1
    soldier2 = (soldier2 + 1) % number_of_soldiers
    while soldier1 < number_of_soldiers:
        difference = abs(height_of_soldiers[soldier1] - height_of_soldiers[soldier2])
        if (difference < minimum_height):
            minimum_height = difference
            minimum_height_index[0] = soldier1
            minimum_height_index[1] = soldier2
        soldier1 += 1
        soldier2 = (soldier2 + 1) % number_of_soldiers

    print("{} {}".format(minimum_height_index[0]+1, minimum_height_index[1]+1))

def Even_Odds():
    strInput1 = input().split(' ')
    n = int(strInput1[0])
    k = int(strInput1[1])
    number_of_evens = n//2
    number_of_odds = n - (n//2)

    if k > number_of_odds:
        remaining_pos = k - number_of_odds
        required_num = 2*remaining_pos
    else:
        required_num = (2*k)-1
    print(required_num)

def Little_Elephant_and_Rozdil():
    number_of_cities = int(input())
    time_taken_for_each_city = input().split(' ')
    time_taken_for_each_city = [eval(i) for i in time_taken_for_each_city]

    minimum_time = min(time_taken_for_each_city)
    minimum_indexes = [i for i,x in enumerate(time_taken_for_each_city) if x == minimum_time]

    if len(minimum_indexes) > 1:
        print("Still Rozdil")
    else:
        print(minimum_indexes[0]+1)

def Hexadecimals_theorem():
    def create_fibonacci(max_element):
        prev = 0
        cur = 1
        fibonacci_sequence = []
        fibonacci_sequence.append(prev)
        fibonacci_sequence.append(cur)

        while cur < max_element:
            new = prev + cur
            fibonacci_sequence.append(new)
            prev = cur
            cur = new

        return fibonacci_sequence

    fibonacci_number = int(input())
    fibonacci_sequence = create_fibonacci(fibonacci_number)
    length = len(fibonacci_sequence)
    #print(fibonacci_sequence)
    if len(fibonacci_sequence) >= 5:
        print("{} {} {}".format(fibonacci_sequence[length-5],fibonacci_sequence[length-4], fibonacci_sequence[length-2]))
    else:
        required_numbers = []
        for i in range(fibonacci_number):
            required_numbers.append(1)
        while len(required_numbers) != 3:
            required_numbers.append(0)
        print("{} {} {}".format(required_numbers[0],required_numbers[1], required_numbers[2]))

def Jeff_and_Digits():
    number_of_cards = int(input())
    card_value = input().split(' ')
    card_value = [eval(i) for i in card_value]
    number_of_5 = card_value.count(5)
    number_of_0 = card_value.count(0)

    if number_of_0 == 0:
        print("-1")
    else:
        ending_of_number = ''
        for _ in range(number_of_0):
            ending_of_number = ending_of_number + '0'

        number_of_5_sum_divisible_by_9 = number_of_5 // 9
        start_of_number = ''
        for _ in range(number_of_5_sum_divisible_by_9):
            start_of_number = start_of_number + ('5'*9)

        if start_of_number == '':
            ending_of_number = '0'

        final_number = start_of_number + ending_of_number
        print(final_number)

def Xenia_and_Ringroad():
    strInput1 = input().split(' ')
    number_of_houses = int(strInput1[0])
    number_of_tasks = int(strInput1[1])

    house_order_for_tasks = input().split(' ')
    house_order_for_tasks = [eval(i) for i in house_order_for_tasks]

    time_to_reach_first_house = house_order_for_tasks[0] - 1
    total_time = time_to_reach_first_house
    i = 0
    j = 1
    while j < len(house_order_for_tasks):
        if house_order_for_tasks[j] < house_order_for_tasks[i]:
            time_to_move_to_next_house = (number_of_houses - (house_order_for_tasks[i]-1)) + (house_order_for_tasks[j]-1)
        else:
            time_to_move_to_next_house = house_order_for_tasks[j] - house_order_for_tasks[i]

        total_time += time_to_move_to_next_house
        i += 1
        j += 1

    print(total_time)

def Magic_Numbers():   
    def convert(string):
        list1 = []
        list1[:0] = string
        return list1
    number_check = input()
    number_list = convert(number_check)

    i = 0
    j = 0
    found = False

    while (j < len(number_list)) and (not found):
        if i == j and number_list[i] == '1':
            j = j + 1
        elif number_list[i] == '1' and number_list[j] == '4' and (j-i) <= 2:
            j = j + 1
        elif number_list[j] == '1':
            i = j
        else:
            found = True

    if (found):
        print("NO")
    else:
        print("YES")


    # number_check_split = number_check.split('1')
    #
    # needs_to_empty = [i for i in number_check_split if ((i != '') and (i != '4') and (i != '44'))]
    # #Point: .remove function only removes one instance of value in a list
    #
    # print(needs_to_empty)
    # if len(needs_to_empty) == 0:
    #     print("YES")
    # else:
    #     print("NO")

def Translation():
    def convert(string):
        list1 = []
        list1[:0] = string
        return list1

    strInput1 = input()
    word1_list = convert(strInput1)
    strInput2 = input()
    word2_list = convert(strInput2)

    word2_list.reverse()

    if word1_list == word2_list:
        print("YES")
    else:
        print("NO")

def Football():
    number_of_goals = int(input())

    goal_scoring_sequence = []
    for i in range(number_of_goals):
        goal_scoring_sequence.append(input())

    #print(goal_scoring_sequence)
    unique_teams = set(goal_scoring_sequence)
    count_of_goals = []
    for i in unique_teams:
        count_of_goals.append(goal_scoring_sequence.count(i))

    #print(unique_teams)
    if (len(unique_teams) > 1) and (count_of_goals[1] > count_of_goals[0]):
        print(list(unique_teams)[1])  ##ACCESING ELEMENTS WITHIN SET
    else:
        print(list(unique_teams)[0])

def Bicycle_Chain():
    stars_pedal = int(input())
    gears_pedal = input().split(' ')
    gears_pedal = [eval(i) for i in gears_pedal]
    stars_rear = int(input())
    gears_rear = input().split(' ')
    gears_rear = [eval(i) for i in gears_rear]


    max_ratio = -1
    count = -1
    for i in gears_rear:
        for j in gears_pedal:
            if i % j == 0:
                if (i/j) > max_ratio:
                    max_ratio = (i/j)
                    count = 1
                elif (i/j) == max_ratio:
                    count += 1

    print(count)

def Sale():
    strInput1 = input().split(' ')
    total_tvs = int(strInput1[0])
    max_carry_capacity = int(strInput1[1])
    price_each_tv = input().split(' ')
    price_each_tv = [eval(i) for i in price_each_tv]
    price_each_tv.sort()

    amount_earned = 0
    tvs_collected = 0
    for i in price_each_tv:
        if (i>0) or (tvs_collected == max_carry_capacity):
            break
        amount_earned += i
        tvs_collected += 1
    print(abs(amount_earned))

def System_of_Equations():
    import math
    strInput1 = input().split(' ')
    n = int(strInput1[0])
    m = int(strInput1[1])

    answer = 0
    for a in range(m+1):
        b_sqaure = m - a
        b = math.sqrt(b_sqaure)

        if (a*a) + b == n :
            answer += 1

    print(answer)

def Business_trip():
    minimum_height = int(input())
    height_growth_each_month = input().split(' ')
    height_growth_each_month = [eval(i) for i in height_growth_each_month]
    height_growth_each_month.sort()
    height_growth_each_month.reverse()

    remaining_height = minimum_height
    count = 0
    while (remaining_height>0) and (count<12):
        remaining_height = remaining_height - height_growth_each_month[count]
        count += 1

    if (count == 12) and (remaining_height>0):
        print(-1)
    else:
        print(count)

def Dubstep():
    dubsub_remix = input()
    dubsub_remix_separated_by_WUB = dubsub_remix.split('WUB')

    original_song = [i for i in dubsub_remix_separated_by_WUB if i!= '']
    song_string = ''
    for i in original_song:
        song_string += i + ' '

    print(song_string)

def k_String():
    def convert(string):
        list1 = []
        list1[:0] = string
        return list1

    number_k = int(input())
    strInput = input()
    string_list = convert(strInput)
    string_list.sort()
    unique_letters = list(set(string_list))

    possible = True
    count_of_letters = {}
    for i in unique_letters:
        count = string_list.count(i)
        count_of_letters[i] = count

        if count % number_k != 0:   #If it leaves a remainfer after dividing by k then k string can never be formed
            possible = False
            break

    if not possible:
        print(-1)
    else:
        output_string = ''
        for i in unique_letters:
            output_string = output_string + (i*(count_of_letters[i]//number_k))
        output_string = output_string*number_k
        print(output_string)

def The_number_of_positions():
    strInput = input().split(' ')
    totalPeople = int(strInput[0])
    a = int(strInput[1])
    b = int(strInput[2])

    #if position is p, then people in front are p -1 , thus p -1 >= a which gives p >= a + 1
    #if position is p, then people behind are n - p, thus n - p <= b which gives p >= n - b

    lower_limit_of_position = max(a+1, totalPeople - b)
    favorable_positons = totalPeople - lower_limit_of_position + 1
    print(favorable_positons)

def Football_52():
    def convert(string):
        list1 = []
        list1[:0] = string
        return list1
    currentPositions = input()
    position_list = convert(currentPositions)

    i = 0
    j = 0
    count = 0
    dangerous = False
    while (j < len(position_list)) and (not dangerous):
        if (i == j):
            j = j + 1
            count = 0
        elif position_list[i] == position_list[j]:
            count += 1
            j = j + 1
            if count == 6:
                dangerous = True
        else:
            i = j

    if (dangerous):
        print("YES")
    else:
        print("NO")

def String_Task():
    def convert(string):
        list1 = []
        list1[:0] = string
        return list1

    inputStr1 = input()
    lower_case_string = inputStr1.lower()
    lower_case_string_list = convert(lower_case_string)
    vowels = ['a','e','i','o','u','y']
    string_without_vowels = [i for i in lower_case_string_list if i not in vowels]
    outputStr = ''
    for i in string_without_vowels:
        outputStr = outputStr + '.' + i

    print(outputStr)

def Little_Elephant_and_Function():
    totalNumbers = int(input())
    #Input to the recursive the function is a1 a2 a3 a4 a5 then output will be a2 a3 a4 a5 a1
    #Input 4 1 2 3 then output will be 1 2 3 4
    sorted_sequence = []
    for i in range(1,totalNumbers):
        sorted_sequence.append(i)

    sorted_sequence.insert(0,totalNumbers)    #TO add element at the start of the list, append adds to the end
    outputStr = ''
    for i in sorted_sequence:
        outputStr = outputStr + str(i) + ' '
    print(outputStr)

def Present_from_Lena():
    number_n = int(input())

    upper_half = []   #Created only top half, bottom half repeated

    starting_space = number_n * 2 #First line has 6 spaces for n = 3, decreases by 2 for each subsequent line

    for i in range(number_n+1):  #For all lines in top half

         numbers_on_this_line = []

         for j in range(i+1):
             numbers_on_this_line.append(j)

         last_element = numbers_on_this_line[len(numbers_on_this_line)-1]
         palindrome_of_numbers = []

         for j in numbers_on_this_line:
             palindrome_of_numbers.append(j)

         for j in numbers_on_this_line:
             if j == last_element:
                 break
             else:
                 palindrome_of_numbers.append(last_element - j - 1)   #palindrome of numbers is all the numbers on that line

         outputStr = ' ' * starting_space

         for j in range(len(palindrome_of_numbers)):

             if j == len(palindrome_of_numbers)-1:
                 outputStr = outputStr + str(palindrome_of_numbers[j])  #No space for last element
             else:
                 outputStr = outputStr + str(palindrome_of_numbers[j]) + ' '

         starting_space -= 2
         upper_half.append(outputStr)
         print(outputStr)

    upper_half.reverse()   #printing upper half in reverse order for the lower half
    middle_row = upper_half.pop(0)
    for i in upper_half:
        print(i)

def Dragons():
    inputStr = input().split(' ')
    strength = int(inputStr[0])
    total_dragons = int(inputStr[1])

    dragon_strength = []
    dragon_reward = []
    for i in range(total_dragons):
        inputStr2 = input().split(' ')
        dragon_strength.append(int(inputStr2[0]))
        dragon_reward.append(int(inputStr2[1]))

    possible = True

    while total_dragons > 0 and possible:
        index_of_possible_dragons = [i for i,x in enumerate(dragon_strength) if x < strength]

        if len(index_of_possible_dragons) == 0:
            possible = False
        else:
            possible_rewards = []
            for i in index_of_possible_dragons:
                possible_rewards.append(dragon_reward[i])

            rewards_in_ascending = [y for y,x in sorted(zip(possible_rewards,index_of_possible_dragons))]
            index_in_ascending = [x for y, x in sorted(zip(possible_rewards, index_of_possible_dragons))]
            strength = strength + rewards_in_ascending[len(rewards_in_ascending)-1]
            total_dragons -= 1
            dragon_strength.pop(index_in_ascending[len(index_in_ascending)-1])
            dragon_reward.pop(index_in_ascending[len(index_in_ascending)-1])


    if total_dragons == 0 and possible:
        print("YES")
    else:
        print("NO")

def Dragons2():
    s, n = map(int, input().split())
    a = []
    for _ in range(n):
        a.append(list(map(int, input().split())))
    #print(a)
    b = sorted(a, key = lambda l:l[0], reverse=False)
    #A lambda is a small anonymous function in Python. The l is the argument to the lambda
    # separated by the body of the function by  :.
    # The l[1] takes the list passed to the lambda and returns the second item (subscript [1] is the second item...)
    #print(b)
    #Earlier approach: if the  dragon strength is lower than current person strength then we select that dragon
    #whose reward is maximum, but this is not necessary as if the dragon strength is lower than person strngth then ultimately
    #the person will be defeating the dragon,


    for x, y in b:

        if s <= x:
            print('NO')
            return()
        else:
            s += y
    print('YES')

def Puzzles():
    kids , totalPresents = map(int, input().split())
    pieces_in_each = list(map(int,input().split()))

    pieces_sorted = sorted(pieces_in_each)
    i = 0
    j = kids-1
    #print(pieces_sorted)
    minimum_diff = pieces_sorted[j] - pieces_sorted[i]
    while j < len(pieces_sorted):

        if pieces_sorted[j] - pieces_sorted[i] < minimum_diff:
            minimum_diff = pieces_sorted[j] - pieces_sorted[i]

        j += 1
        i += 1

    print(minimum_diff)

def Chat_room():
    #a = re.search("h.*e.*l.*l.*o", input())
    s = iter(input())
    print(s)
    k = [all(c in s for c in 'hello')]
    print(k)
    # def convert(string):
    #     list1 = []
    #     list1[:0] = string
    #     return list1
    # input_stirng_list = convert(input())
    # print(input_stirng_list)
    # unique_char = set(input_stirng_list)
    # print(unique_char)
    #
    # string = ''
    # for i in unique_char:
    #     string = string + i
    #
    # if 'hello' in string:
    #     print("YES")
    # else:
    #     print("NO")

def Airport():
    numPassengers , numPlanes = map(int, input().split())
    emptySeats = list(map(int, input().split()))

    sortedSeats = sorted(emptySeats)

    minimum_revenue = 0
    maximum_revenue = 0

    placed_min = 0
    while placed_min < numPassengers:
        #print(minimum_revenue)
        minimum_revenue += sortedSeats[0]
        sortedSeats[0] -= 1
        if sortedSeats[0] == 0:
            sortedSeats.pop(0)
        placed_min += 1

    placed_max = 0

    sortedSeats = sorted(emptySeats, reverse=True)
    while placed_max < numPassengers:
        maximum_revenue += sortedSeats[0]
        sortedSeats[0] -= 1
        sortedSeats = sorted(sortedSeats, reverse=True)
        placed_max += 1

    print("{} {}".format(maximum_revenue, minimum_revenue))

def DZY_Loves_Chessboard(): #This function arranges the output according to input. Better way would be to arrange the chess in alernate fashion
    #and then place dashes according to the input. This is done in the second function
    def convert(string):
        list1 = []
        list1[:0] = string
        return  list1
    
    rows, columns = map(int, input().split())
    chessboard = []
    for i in range(rows):
        chessboard.append(convert(input()))

    output=[]
    for i in range(rows):
        list2 = []
        for j in range(columns):
            list2.append('-')
        output.append(list2)

    for i in range(rows):
        for j in range(columns):
            if chessboard[i][j] == '.':
                # if (((j+1)>=0) and (output[i][j+1] == 'B')):
                #     output[i][j] = 'W'
                # else:
                #     output[i][j] = 'B'

                if ((((i-1)>=0) and (output[i-1][j] == 'B')) or  (((j-1)>=0) and (output[i][j-1] == 'B')) or (((i+1) < rows) and (output[i+1][j] == 'B')) or (((j+1) < columns) and (output[i][j+1] == 'B'))):
                    output[i][j] = 'W'
                else:
                    output[i][j] = "B"

    for i in range(rows):
        outputStr = ''
        for j in output[i]:
            outputStr = outputStr + j
        print(outputStr)

def DZY_Loves_Chessboard2():
    def convert(string):
        list1 = []
        list1[:0] = string
        return  list1

    rows, columns = map(int, input().split())
    chessboard = []
    for i in range(rows):
        chessboard.append(convert(input()))

    #output= [[0]*columns]*rows This sets all elements to be equal , do not do this

    output = []
    for i in range(rows):
        list2 = []
        for j in range(columns):
            list2.append(0)
        output.append(list2)

    columns_even = columns % 2
    prev_col = 'B'

    for i in range(rows):

        if columns_even == 0 and prev_col == 'B':
            prev_col = 'W'
        elif columns_even == 0 and prev_col == 'W':
            prev_col = 'B'

        for j in range(columns):
            if prev_col == 'B' and chessboard[i][j] == '.':
                output[i][j] = 'W'
                prev_col = 'W'
            elif prev_col == 'W' and chessboard[i][j] == '.':
                output[i][j] = 'B'
                prev_col = 'B'
            elif prev_col == 'B' and chessboard[i][j] == '-':
                output[i][j] = '-'
                prev_col = 'W'
            elif prev_col == 'W' and chessboard[i][j] == '-':
                output[i][j] = '-'
                prev_col = 'B'

    for i in range(rows):
        outputStr = ''
        for j in output[i]:
            outputStr = outputStr + j
        print(outputStr)

def Pashmak_and_Flowers():
    import math
    numFlowers = int(input())
    flower_beauty = list(map(int, input().split()))
    beauty_sorted = sorted(flower_beauty)
    minimum_beauty = beauty_sorted[0]
    maximum_beauty = beauty_sorted[len(beauty_sorted)-1]

    maxDiff = maximum_beauty - minimum_beauty

    minBeuaty_flowers = beauty_sorted.count(minimum_beauty)
    maxBeaty_flowers = beauty_sorted.count(maximum_beauty)

    if maxDiff == 0: #if this is the case then all flowers are of same beauty
        possibleCombinations = math.comb(numFlowers,2)
    else:
        possibleCombinations = minBeuaty_flowers * maxBeaty_flowers

    print("{} {}".format(maxDiff, possibleCombinations))

def Jeff_and_Periods():   #Time limit excedded, this happended because we are performing enumerate multiple times for the same element
    #better to use dictionary, go over the list only once and save the indexes while going over the list one time only
    #done in second function
    def checkAP(list1):
        const_diff = list1[1] - list1[0]

        isAP = True
        i = 0
        j = 1
        while j < len(list1):
            if list1[j] - list1[i] != const_diff:
                isAP = False
                break
            i += 1
            j += 1

        return isAP, const_diff

    n = int(input())
    sequence_of_num = list(map(int, input().split()))
    unique_num = list(set(sequence_of_num))

    index_dict = {}
    for num in sequence_of_num:
        index_list = [i for i,x in enumerate(sequence_of_num) if x == num]
        index_dict[num] = index_list

    output_list = []
    for i in unique_num:
        if len(index_dict[i]) == 1:
            list1 = [i , 0]
            output_list.append(list1)
        else:
            isAP, const_diff = checkAP(index_dict[i])
            if (isAP):
                list1 = [i,const_diff]
                output_list.append(list1)

    output_list = sorted(output_list, key=lambda l: l[0], reverse=False)
    print(len(output_list))
    for i in output_list:
        print("{} {}".format(i[0],i[1]))

def Jeff_and_Periods2():
    def checkAP(list1):
        const_diff = list1[1] - list1[0]

        isAP = True
        i = 0
        j = 1
        while j < len(list1):
            if list1[j] - list1[i] != const_diff:
                isAP = False
                break
            i += 1
            j += 1

        return isAP, const_diff

    n = int(input())
    sequence_of_num = list(map(int , input().split()))

    unique_num = list(set(sequence_of_num))
    index_dict = {}
    for i in unique_num:
        index_dict[i] = []

    for i in range(len(sequence_of_num)):
        index_dict[sequence_of_num[i]].append(i)

    output_list = []
    for i in unique_num:
        if len(index_dict[i]) == 1:
            output_list.append([i,0])
        else:
            isAP, const_diff = checkAP(index_dict[i])

            if isAP:
                output_list.append([i,const_diff])

    output_list = sorted(output_list , key = lambda l : l[0] , reverse = False)
    print(len(output_list))
    for i in output_list:
        print("{} {}".format(i[0], i[1]))

def Little_Girl_and_Game():
    def covert(string):
        list1 = []
        list1[:0] = string
        return list1

    inputList = covert(input())
    uniqueLetters = list(set(inputList))

    index_dict = {}
    for i in uniqueLetters:
        index_dict[i] = []

    for i in range(len(inputList)):
        index_dict[inputList[i]].append(i)

    oddOccurances = 0 #this counts how many elements occus odd number of times in the list
    for i in uniqueLetters:
        if len(index_dict[i]) % 2 == 1:
            oddOccurances += 1

    if oddOccurances % 2 == 1 or oddOccurances == 0: #if the number of odd ocuurances are zeros eg aabb -- abab or are odd eg aabbc -- abcba, then first player wins
        print("First")
    else:
        print("Second")

def Sail():
    def convert(string):
        list1 = []
        list1[:0] = string
        return list1
    #East,West affect x coord , North, soth affect y coordinate
    t , sx, sy, ex, ey = map(int ,  input().split())
    windDirections = convert(input())

    E = 0
    W = 0
    N = 0
    S = 0
    if ex > sx : E += ex - sx
    else: W += sx - ex

    if ey > sy: N += ey - sy
    else: S += sy - ey

    #print(E,W,N,S)

    direction_dict = {}
    direction_dict['E'] = 0
    direction_dict['W'] = 0
    direction_dict['N'] = 0
    direction_dict['S'] = 0

    time_taken = 0
    for i in windDirections:

        direction_dict[i] += 1
        time_taken += 1
        #print(direction_dict , time_taken),


        if direction_dict['E'] >= E and direction_dict['W'] >= W and direction_dict['N'] >= N and direction_dict['S'] >= S:
            #Used greater than or equal because at wrong directions, anchor will be used, only correct wind directions matter
            break

    if time_taken < t :
        print(time_taken)
    elif direction_dict['E'] >= E and direction_dict['W'] >= W and direction_dict['N'] >= N and direction_dict['S'] >= S:
        print(time_taken)
    else:
        print(-1)

def Shower_Line():
    from itertools import permutations

def Shooshuns_and_Sequence():
    n , k = map(int, input().split())
    intSequence = list(map(int, input().split()))

    swappingIndex = k-1

    list_after_swappingIndex = intSequence[swappingIndex:]
    uniqueElements = list(set(list_after_swappingIndex))

    if len(uniqueElements) > 1:
        print(-1)
    else:
        steps_required = k-1
        for i in range(1,swappingIndex+1):
            before_swappingIndex = swappingIndex-i
            if intSequence[before_swappingIndex] == intSequence[swappingIndex]:
                steps_required -= 1
            else:
                break
        print(steps_required)

def Xenia_and_Divisors():
    n = int(input())
    sequence = list(map(int, input().split()))

    num1C = sequence.count(1)
    num2C = sequence.count(2)
    num3C = sequence.count(3)
    num4C = sequence.count(4)
    num5C = sequence.count(5)
    num6C = sequence.count(6)
    num7C = sequence.count(7)

    if num5C != 0 or num7C != 0 or num1C != n//3 :
        print(-1)
    else:
        #Type 1 is 1 2 4, type 2 is 1 2 6 , type 3 is 1 3 6
        sequence_printed = []

        while num3C > 0 and num6C > 0:
            sequence_printed.append("1 3 6")
            num3C -= 1
            num6C -= 1

        while num2C > 0 and num4C > 0:
            sequence_printed.append("1 2 4")
            num2C -= 1
            num4C -= 1

        while num2C > 0  and num6C > 0:
            sequence_printed.append("1 2 6")
            num2C -= 1
            num6C -= 1
        if len(sequence_printed) == 0 or (num2C != 0 or num3C != 0 or num4C != 0 or num6C != 0):
            print(-1)
        else:
            for i in sequence_printed:
                print(i)

def Letter():
    def convert(string):
        list1 = []
        list1[:0] = string
        return list1

    heading_list = convert(input())
    text_list = convert(input())
    uniqueChar_heading = list(set(heading_list))
    uniqueChar_text = list(set(text_list))

    letterDict_heading = {}
    letterDict_text = {}
    for i in uniqueChar_heading:
        letterDict_heading[i] = []
    for i in uniqueChar_text:
        letterDict_text[i] = []

    for i in range(len(heading_list)):
        letterDict_heading[heading_list[i]].append(i)
    for i in range(len(text_list)):
        letterDict_text[text_list[i]].append(i)

    possible = True
    for i in uniqueChar_text:
        if i != ' ' and i not in letterDict_heading.keys():
            #print("First", i)
            possible = False
            break
        elif i != ' ' and len(letterDict_heading[i]) < len(letterDict_text[i]) :
            #print("Second" , i)
            possible = False
            break

    if not possible:
        print("NO")
    else:
        print("YES")

def Kitahara_Harukis_Gift():
    numApples = int(input())
    weightSequence = list(map(int, input().split()))
    totalWeight = sum(weightSequence)

    count_1 = weightSequence.count(100)
    count_2 = weightSequence.count(200)

    if totalWeight % 2 != 0:
        print("NO")
        return
    else:
        weight_of_one = totalWeight // 2

        if weight_of_one % 100 != 0:  #Each one will also get multiples of 100 and 200 only
            print("NO")
            return
        else:
            count_2_left = count_2 - (2 * (count_2 // 2))
            count_1_left = count_1 - (2 * (count_1 // 2))

            if count_2_left == 0 and count_1_left == 0:
                print("YES")
                return
            else:
                print("NO")
                return

def Comparing_Strings():
    def convert(string):
        list1 = []
        list1[:0] = string
        return list1

    genome1 = convert(input())
    genome2 = convert(input())

    if len(genome1) != len(genome2) :
        print("NO")
        return
    else:
        not_matched_G1 = []
        not_matched_G2 = []

        for i in range(len(genome1)):
            if genome1[i] != genome2[i]:
                not_matched_G1.append(genome1[i])
                not_matched_G2.append(genome2[i])

        if len(not_matched_G1) != 2 :
            print("NO")
            return
        else:
            if not_matched_G1[0] == not_matched_G2[1] and not_matched_G1[1] == not_matched_G2[0]:
                print("YES")
                return
            else:
                print("NO")
                return

def Hungry_Sequence():  #Run time error due to prime printing. Instead go from n to 2n-1 to print n numbers.
    #print prime numbers
    def checkPrime(n):
        isPrime = True
        for i in range(2,n):
            if (n %i ) == 0:
                isPrime = False
                return isPrime
        return isPrime

    sequenceLength = int(input())
    hungry = []
    hungry.append(2)
    index = 3
    while len(hungry) < sequenceLength:
        if checkPrime(index):
            hungry.append(index)
        index += 1

    outputStr = ''
    for i in hungry:
        outputStr = outputStr + str(i) + ' '
    print(outputStr)

def Hungry_Sequence2():
    n = int(input())

    #Join ist using a = ' '.join(str(i) for i in [1,2,3])
    print(' '.join(str(i) for i in range(n, n + n)))


def Big_Segment():  #Run time error
    numSegments = int(input())
    startCoor = []
    endCoor = []

    for i in range(numSegments):
        s,e = map(int, input().split())
        startCoor.append(s)
        endCoor.append(e)

    min_start = min(startCoor)
    max_end = max(endCoor)

    min_start_index = [i for i,x in enumerate(startCoor) if x == min_start]
    max_end_index = [i for i,x in enumerate(endCoor) if x == max_end]

    for i in min_start_index:
        if i in max_end_index:
            print(i+1)
            return

    print(-1)

def Big_Segment2():
    numSegments = int(input())
    startCoor = []
    endCoor = []

    for i in range(numSegments):
        s,e = map(int, input().split())
        startCoor.append(s)
        endCoor.append(e)

    min_start = min(startCoor)
    max_end = max(endCoor)

    index = 0
    for s,e in zip(startCoor,endCoor):
        if s == min_start and e == max_end:
            print(index+1)
            return
        index += 1

    print(-1)
    return

def Little_Elephant_and_Bits():
    #Have to remove a zero, remove that zero which is most ahead in the string
    def convert(string):
        list1 = []
        list1[:0] = string
        return list1

    binaryNum = ''
    def convertBinary(n):
        if n > 1:
            convertBinary(n//2)
        #print(n%2)
        binaryNum = binaryNum + str(n%2)

    inputBit = convert(input())
    inputBit_reversed = inputBit[::-1]

    last_0_index = -1

    index = 0
    for i in inputBit_reversed:
        if i == '0':
            last_0_index = index
        index += 1

    #print(inputBit_reversed)
    #print(last_0_index)
    if last_0_index != -1 :
        inputBit_reversed.pop(last_0_index)
    else:
        inputBit_reversed.pop(0)

    index = 0
    decimalNum = 0
    for i in inputBit_reversed:
        if i == '1':
            decimalNum += 2**index
        index += 1

    print(decimalNum)
    convertBinary(decimalNum)
    print(binaryNum)

#Since we are allowed to swap any two neighbouring elements, and allowed to do it any number of times(finite), thus
#we will be able to achieve any required permutation of array
def Yaroslav_and_Permutations():
    n = int(input())
    sequence = list(map(int,input().split()))

    freqCount_dict = {}

    for i in sequence:
        if i in freqCount_dict.keys():
            freqCount_dict[i] += 1
        else:
            freqCount_dict[i] = 1

    max_count = 0
    for i in freqCount_dict.keys():
        if freqCount_dict[i] > max_count:
            max_count = freqCount_dict[i]

    if n%2 == 0:
        if max_count > n//2:
            print("NO")
        else:
            print("YES")
    else:
        if max_count > ((n//2) + 1):
            print("NO")
        else:
            print("YES")

def Fence():   #Time Limit exceeded, Avoid for loop within while loop, for each new window shift, one num gets added, one num gets subtracted
    n , k = map(int, input().split())
    heightSequence = list(map(int, input().split()))
    print(heightSequence)

    index = 0
    min_sum = sum(heightSequence)
    small_index_start = 0
    while index+k< len(heightSequence):
        sum1 = 0
        for i in range(k):
            sum1 += heightSequence[index+i]

        if sum1 < min_sum:
            min_sum = sum1
            small_index_start = index

        index += 1

    print(small_index_start+1)

def Fence2():
    n , k = map(int , input().split())
    heightSequence = list(map(int, input().split()))

    windowSum = 0
    globalSum_min = 0
    min_index = 0
    for i in range(k):
        windowSum += heightSequence[i]
    globalSum_min = windowSum

    for i in range(k,len(heightSequence)):

        windowSum = windowSum + heightSequence[i] - heightSequence[i-k]

        if windowSum < globalSum_min:
            min_index = i - (k - 1) #start index of that window
            globalSum_min = windowSum

    print(min_index+1)

def TL():
    n,m = map(int, input().split())
    correctSol_time = list(map(int,input().split()))
    incorrectSol_time = list(map(int ,input().split()))

    soretd_correctTime = sorted(correctSol_time)

    v_gte1 = 2*soretd_correctTime[0]
    v_gte2 = soretd_correctTime[len(soretd_correctTime)-1]

    v_gte = max(v_gte1,v_gte2)   #gte means greater than or equal

    v_lt = min(incorrectSol_time)  #lt means less than and lte means less than or equal
    v_lte = v_lt - 1

    if v_gte <= v_lte:
        print(v_gte)
    else:
        print(-1)

def Increase_and_Decrease():
    #First using the shift operation, shift all the water in the first bucket(hypothetacally)
    #Now the first element is the sum of all elements and all the other elements is zero
    #start distributing the water from first bucket to rest of the buckets. if its a perfect division then each element will be
    # totalsum/n else n-1 buckets will be totalsum/n(floor of this) and one bucket will be unequal
    arraySize = int(input())
    array = list(map(int, input().split()))

    totalSum = sum(array)

    if totalSum % arraySize == 0:
        print(arraySize)
    else:
        print(arraySize-1)

def Two_Bags_of_Potatoes(): #Time limit exceeded. Instead if using range for 1 to n-y. Go in multiples of k, till n and x+y <= n
    y,k,n = map(int , input().split())

    numPossible = []
    for x in range(1,n-y+1):
        if (x+y) % k == 0:
            numPossible.append(x)

    if len(numPossible) > 0:
        print(' '.join(str(i) for i in numPossible))
    else:
        print(-1)

def Two_Bags_of_Potatoes2():                   # x + y <= n then x <= n - y  
    y,k,n = map(int , input().split())         # x + y = (t*k) i.e x = ((t*k) - y)
                                               # so (t*k) - y <= n - y i.e (t*k) <= n 
    count = 1
    multiple = k * count #multiple is x+y candidate
    numPossible = []
    while multiple <= n:

        x = multiple - y
        if x >= 1:
            numPossible.append(x)
        count += 1
        multiple = k * count


    if len(numPossible) == 0:
        print(-1)
    else:
        print(' '.join(str(i) for i in numPossible))

def Unlucky_Ticket():
    def convert(string):
        list1 = []
        list1[:0] = string
        return list1

    n = int(input())
    ticketList = convert(input())

    firstHalf = ticketList[:n]
    secondHalf = ticketList[n:]

    firstHalf_sorted = sorted(firstHalf)
    secondHalf_sorted = sorted(secondHalf)

    if firstHalf_sorted[0] == secondHalf_sorted[0]:
        print("NO")
        return
    else:
        first_compare = firstHalf_sorted[0] < secondHalf_sorted[0]
        possible = True

        for i in range(1,len(firstHalf_sorted)):

            new_compare = firstHalf_sorted[i] < secondHalf_sorted[i] #Everything should be strictly smaller

            if new_compare != first_compare or firstHalf_sorted[i] == secondHalf_sorted[i]:
                possible = False
                break

        if possible:
            print("YES")
        else:
            print("NO")

def Boys_and_Girls():
    boys, girls = map(int , input().split())

    outputStr = ''
    if boys > girls:
        for i in range(girls):
            outputStr += 'BG'

        for i in range(boys-girls):
            outputStr += 'B'

    else:
        for i in range(boys):
            outputStr += 'GB'

        for i in range(girls-boys):
            outputStr += 'G'

    print(outputStr)

def Easy_Number_Challenge(): #Time limit exceeded, use list only instead of dictionary
    a, b, c = map(int, input().split())
    max_num = a*b*c

    divisorDictCount = {}
    for i in range(1,max_num+1):
        divisorDictCount[i] = 0

    for i in range(1,max_num+1):
        currentMultiple = i
        while currentMultiple <= max_num:
            divisorDictCount[currentMultiple] += 1
            currentMultiple += i

    totalCount = 0
    for i in range(1,a+1):
        for j in range(1,b+1):
            for k in range(1,c+1):
                totalCount += divisorDictCount[i*j*k]
    print(divisorDictCount)
    print(totalCount)

def Easy_Number_Challenge2():
    a,b,c = map(int, input().split())
    max_num = a * b * c

    divisorCountList = [1] * (max_num)

    #print(divisorCountList)
    for i in range(2,max_num+1):
        #print(divisorCountList , i)
        currentNum = i

        while currentNum <= max_num:
            divisorCountList[currentNum-1] += 1
            currentNum += i

    totalSum = 0
    for i in range(1,a+1):
        for j in range(1,b+1):
            for k in range(1,c+1):
                totalSum += divisorCountList[(i*j*k) - 1]
    #print(divisorCountList)
    print(totalSum)


def Pythagorean_Theorem_II():
    import math
    n = int(input())

    totalCombinations = []
    thirdSide = []
    a = 1
    while a <= math.sqrt((n*n) - 1):
        b = a+1
        while b <= math.sqrt((n*n)-1):
            c_square = (a**2) + (b**2)
            c = math.sqrt(c_square)

            if int(c) == c:
                print(c, int(c))
                thirdSide.append(c)
                if c == 25.0:
                    print("NO" , [a,b])
                if [a, b] in totalCombinations:
                    print("YES", [a, b])
                totalCombinations.append([a,b])

            b += 1
        a += 1

    print(len(totalCombinations))
    print(totalCombinations)
    print(thirdSide)
    unique = list(set(thirdSide))
    countDict = {}
    for i in unique:
        countDict[i] = 0

    for i in thirdSide:
        countDict[i] += 1

    for i in countDict.keys():
        if countDict[i] > 1:
            print(i)
    #print(set(thirdSide))

    #for i in thirdSide:
    #    if not in unique:

def Cards_with_Numbers():
    n = int(input())
    cardNum_sequence = [int(x) for x in input().split()]
    #print(n)
    #print(cardNum_sequence)

    uniqueNumList = list(set(cardNum_sequence))
    index_dict = {}

    for index,num in enumerate(cardNum_sequence):
        if num in index_dict.keys():
            index_dict[num].append(index)
        else:
            index_dict[num] = [index]

    outputStr = ''

    for uniqueNum in uniqueNumList:
        if len(index_dict[uniqueNum]) % 2 != 0:
            print(-1)
            return 
        else: 
            currentPtr = 0 
            while currentPtr < len(index_dict[uniqueNum]):
                outputStr = outputStr + str(index_dict[uniqueNum][currentPtr]+1) + ' ' + str(index_dict[uniqueNum][currentPtr+1]+1) +'\n'
                currentPtr += 2
    
    outputStr = outputStr.strip()
    print(outputStr)
                 
def Domino():
    n = int(input())
    upperHalf_num = []
    lowerHalf_num = []
    odd_even_domino = False 
    #the sum can either be even even, odd odd, odd even
    #whenever the sum is odd, the even numbers exist, the odd numbers are always in pair
    #so if the case is odd even, it can never be made even even, in odd, one odd will be without pair

    for domino in range(n):
        numList = [int(x) for x in input().split(' ')]
        upperHalf_num.append(numList[0])
        lowerHalf_num.append(numList[1])

        if (not odd_even_domino) and ((numList[0] % 2 == 0 and numList[1] % 2 != 0) or (numList[0] % 2 != 0 and numList[1] %2 == 0)):
            odd_even_domino = True 
    
    upperHalf_sum = sum(upperHalf_num)
    lowerHalf_sum = sum(lowerHalf_num)

    if (upperHalf_sum % 2 == 0) and (lowerHalf_sum % 2 == 0):
        print(0)
        return
    elif (upperHalf_sum % 2 != 0) and (lowerHalf_sum % 2 != 0):
        if odd_even_domino:
            print(1)
            return
        else:
            print(-1)
            return
    else:
        print(-1)
        return

def Cinema_Line():
    n = int(input())
    value_of_bills = [int(x) for x in input().split(' ')]

    num_25 = 0
    num_50 = 0
    num_100 = 0

    for bill in value_of_bills:
        #print(num_25, num_50, num_100)
        if bill == 25:
            num_25 += 1
        elif bill == 50:
            num_50 += 1
        else:
            num_100 += 1
        
        if bill == 25:
            continue
        elif bill == 50 and num_25 >= 1 :
            num_25 -= 1
        elif  bill == 100 and num_50 >= 1 and num_25 >= 1:
            num_50 -= 1
            num_25 -= 1
        elif bill == 100 and num_25 >= 3:
            num_25 -= 3
        else:
            print("NO")
            return 
    
    print("YES")
    return

def Rank_List():
    list1 = [int(x) for x in input().split(' ')]
    n = list1[0]
    k = list1[1]
    
    probSolved = []
    penaltyTime = []
    timeDict = {}

    for i in range(n):
        list2 = [int(x) for x in input().split(' ')]
        probSolved.append(list2[0])
        penaltyTime.append(list2[1])

        if list2[0] in timeDict.keys():
            timeDict[list2[0]].append(list2[1])
        else: 
            timeDict[list2[0]] = [list2[1]]
    
    probSolved_sorted = sorted(probSolved, reverse= True)
    probs_at_reqd_pos = probSolved_sorted[k-1]

    teams_before = 0 
    for unique_prob in timeDict.keys():
        if unique_prob > probs_at_reqd_pos:
            teams_before += len(timeDict[unique_prob])
    
    pos_in_that_slab = k - teams_before 

    time_sorted_that_prob = sorted(timeDict[probs_at_reqd_pos])
    time_at_reqd_pos = time_sorted_that_prob[pos_in_that_slab - 1]

    teams_sharing = time_sorted_that_prob.count(time_at_reqd_pos)
    print(teams_sharing)
    return

def Cut_Ribbon1():
    #we want xa + yb + zc = n. we want to find solutions for (x,y,z) such that (x+y+z) is maximum and x,y,z should be integer
    #
    list1 = [int(x) for x in input().split(' ')]
    n = list1[0]
    a = list1[1]
    b = list1[2]
    c = list1[3] 

    cut_sizes = [a,b,c]
    a_pieces_max = n//a
    b_pieces_max = n//b 
    
    max = 0 

    for a_pieces in range(0,a_pieces_max+1):
        for b_pieces in range(0,b_pieces_max+1):
            z_value =(n - (a_pieces*a) - (b_pieces*b))/c 
            if z_value != int(z_value) or (z_value<0):
                continue 
            else:
                num_pieces = a_pieces + b_pieces + z_value 
                if max < num_pieces:
                    max = num_pieces
    
    print(int(max)) 
    return

def Cut_Ribbon2():
    #num_ways is a function which return the maximum steps needed to step down from nth stair to base, using a step size of a or b or c
    #Now from nth stair, we have 3 options for first step size if n is not zero
    #we take that step size out of three, which results in maximum steps, we add 1 as we are taking at least one step
    def num_ways(n,a,b,c,globalDict):
        #print(n,globalDict)
        if n in globalDict.keys():
            return globalDict[n]
        elif n == 0: # already at the base
            globalDict[n] = 0
            return globalDict[n]
        elif n < 0: #in the tree we have a node where that path is not possible, return -1 so that it is not counted in max function
            return -1
        else:
            path1 = num_ways(n-a,a,b,c,globalDict)
            path2 = num_ways(n-b,a,b,c,globalDict)
            path3 = num_ways(n-c,a,b,c,globalDict)
            if path1 == -1 and path2 == -1 and path3 == -1 :  #there is no way to reach bottom from that stair using that step sizes
                globalDict[n] = -1 
                return globalDict[n]
            else:
                max_remaining_ways = 1 + max(path1,path2,path3)
                globalDict[n] = max_remaining_ways
                return globalDict[n] 
    
    list1 = [int(x) for x in input().split(' ')]
    n = list1[0]
    a = list1[1]
    b = list1[2]
    c = list1[3]
    globalDict = {}

    print(num_ways(n,a,b,c,globalDict))

def IQ_Test():
    row1 = [1 if x == '#' else 0 for x in input() ]
    row2 = [1 if x == '#' else 0 for x in input() ]
    row3 = [1 if x == '#' else 0 for x in input() ]
    row4 = [1 if x == '#' else 0 for x in input() ] 
    
    #print(len(row1))
    diff_1_2 = [0,0,0,0]
    add_1_2 = [0,0,0,0]
    for i in range(4):
        diff_1_2[i] = abs(row1[i] - row2[i]) 
        add_1_2[i] = row1[i] + row2[i]
    
    diff_2_3 = [0,0,0,0]
    add_2_3 = [0,0,0,0]
    for i in range(4):
        diff_2_3[i] = abs(row2[i] - row3[i]) 
        add_2_3[i] = row2[i] + row3[i]

    diff_3_4 = [0,0,0,0]
    add_3_4 = [0,0,0,0]
    for i in range(4):
        diff_3_4[i] = abs(row3[i] - row4[i]) 
        add_3_4[i] = row3[i] + row4[i]

    found = False 
    marker = 0 
    while not found and marker < (len(row1)-1):
        #print(marker)
        d1 = diff_1_2[marker] + diff_1_2[marker+1]  #alowed cases  0 1 ,1 0, 0 0 
        d2 = diff_2_3[marker] + diff_2_3[marker+1]  # 0 0 is allowed only when the additions are same that is all 4 are already same
        d3 = diff_3_4[marker] + diff_3_4[marker+1]  #this allowed values of di are 1 or 0
        a1 = add_1_2[marker] - add_1_2[marker+1]    #if di is zero then ai must be 0
        a2 = add_2_3[marker] - add_2_3[marker+1]
        a3 = add_3_4[marker] - add_3_4[marker+1]
        if (d1 == 1 or (d1 == 0 and a1 == 0 )or d2 == 1 or (d2 == 0 and a2 == 0) or d3 == 1 or (d3 == 0 and a3 == 0)):
            found = True
        marker += 1 
    
    if found:
        print("YES")
    else:
        print("NO")
    
    return

def Building_Permutation():
    n = int(input())
    sequence = [int(x) for x in input().split(' ')]
    sequence_sorted = sorted(sequence) #in ideal case this should be 1,2,3,4,5,....,n
    #the minimum number of steps required would be when sequence_sorted[i] is made integer i, closest distance
    actual_seq = [x for x in range(1,n+1)]
    
    dist = 0
    for index in range(len(sequence_sorted)):
        dist += abs(sequence_sorted[index] - actual_seq[index])
    print(dist)

    return

def Kuriyama_Mirai_Stones():
    n = int(input())
    sequence = [int(x) for x in input().split()]
    sequence_sorted = sorted(sequence)
    m = int(input())

    sequence_sum = []
    running_sum = 0
    for num in sequence:
        running_sum += num 
        sequence_sum.append(running_sum)
    
    sequence_sorted_sum = []
    running_sum = 0 
    for num in sequence_sorted:
        running_sum += num 
        sequence_sorted_sum.append(running_sum)
    
    outputStr= ''
    #print(sequence_sum)
    #print(sequence_sorted_sum)
    
    for q in range(m):
        list1 = [int(x) for x in input().split(' ')]
        typeq = list1[0]
        l = list1[1]-1 #as numbering the question starts from 1 and not 0
        r = list1[2]-1
        if typeq == 1:
            if l > 0:
                res =  sequence_sum[r] - sequence_sum[l-1]                
            else:
                 res = sequence_sum[r]
        else:
            if l > 0:
                res = sequence_sorted_sum[r] - sequence_sorted_sum[l-1]
            else:
                 res = sequence_sorted_sum[r]
        
        outputStr += str(res) + '\n'
    
    outputStr = outputStr.strip()
    print(outputStr) 
    return

def T_primes():
    import math

    def isprime(num):
        for n in range(2,int(num**0.5)+1):
            if num%n==0:
                return False
        return True
    
    n = int(input())
    #sequence = [int(x) for x in input().split()]
    sequence = inlt()
    outputStr= ''

    for num in sequence:
        sqrt = math.sqrt(num)
        even_bool = (num%2==0)
        four_bool = (num==4)
        if num != 1 and not (even_bool and not four_bool) and  int(sqrt) == sqrt:
            if isprime(sqrt):
                outputStr += 'YES' + '\n'
            else:
                outputStr += 'NO' + '\n'
        else:
            outputStr += 'NO' + '\n'
    
    outputStr = outputStr.strip()
    print(outputStr)
    return

def  Sereja_and_Suffixes():
    list1 = [int(x) for x in input().split(' ')]
    n = list1[0]
    m = list1[1]

    sequence = [int(x) for x in input().split(' ')]
    sequence.reverse()
    distict_elements = []
    distict_elements_count = [0]*n
    
    index = 0
    for num in sequence:
        if num not in distict_elements:
            distict_elements.append(num)
            distict_elements_count[index] = len(distict_elements)
        else:
            distict_elements_count[index] = len(distict_elements)
        index += 1
   
    outputStr = ''
    for q in range(m):
        pos = int(input())
        pos_from_back = n - (pos-1) - 1 
        outputStr += str(distict_elements_count[pos_from_back]) +'\n'
    outputStr = outputStr.strip()
    print(outputStr)
    return 

#Sereja_and_Suffixes()
T_primes()                               #NOT COMPLETED, Correct sol, time imit exceeded
#Kuriyama_Mirai_Stones()                  #NOT COMPLETED, Correct sol, time imit exceeded
#Building_Permutation()
#IQ_Test()
#Cut_Ribbon2()
#Cut_Ribbon1() Both work correctly    
#Rank_List()
#Cinema_Line()
#Domino()
#Cards_with_Numbers()                         #Correct solution, different input output expected in codeforces
#Pythagorean_Theorem_II()
#Easy_Number_Challenge2()
#Boys_and_Girls()                                 #NOT COMPLETED
#Unlucky_Ticket()
#Two_Bags_of_Potatoes2()
#Increase_and_Decrease()
#TL()
#Fence2()
#Yaroslav_and_Permutations()
#Little_Elephant_and_Bits()                         #NOT COMPLETED
#Big_Segment2()
#Hungry_Sequence2()
#Comparing_Strings()
#Kitahara_Harukis_Gift()                             #NOT COMPLETED
#Letter()
#Xenia_and_Divisors()
#Shooshuns_and_Sequence()                             @@@ GOOD PROBLEM
#Shower_Line()                                        #NOT COMPLETED
#Sail()
#Little_Girl_and_Game()
#Jeff_and_Periods2()
#Pashmak_and_Flowers()
#DZY_Loves_Chessboard2()
#Airport()
#Chat_room()                                            #NOT COMPLETED
#Puzzles()
#Dragons2()
#Present_from_Lena()
#Little_Elephant_and_Function()
#String_Task()
#Football_52()
#The_number_of_positions()
#k_String()                                   @@@ GOOD PROBLEM
#Dubstep()
#Business_trip()
#System_of_Equations()
#Sale()
#Bicycle_Chain()
#Football()
#Translation()
#Magic_Numbers()                               @@@ GOOD PROBLEM- check 1,14 or 144
#Xenia_and_Ringroad()
#Jeff_and_Digits()
#Hexadecimals_theorem()
#Little_Elephant_and_Rozdil()
#Even_Odds()
#Reconnaissance_2()
#Parallelepiped()
#Petr_and_Book()
#Supercentral_Point()                                            #NOT COMPLETED
#Jzzhu_and_Children()
#Dima_and_Friends()
#Effective_Approach2()
#Bit()
# Team()
# Petya_and_Strings()
# HQ9()
# Soft_Drinking()
# Amusing_Joke()
# Boy_or_Girl()
# Way_Too_Long_Words()
# Is_your_horseshoe_on_the_other_hoof()
# Helpful_Maths()
# Tram()
# I_love_username()
# Cupboards()
# Insomnia_cure()
# Drinks()
# Arrival_of_the_General()
# Perfect_Permutation()
# Ultra_Fast_Mathematician()
# Panoramixs_Prediction()


#ctrl + k ctrl + j to expand the code fragments
#ctrl + k ctrl + 0 to collapse the code fragments