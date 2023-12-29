import sys
#sys.setrecursionlimit(10**7)
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

def Choosing_Teams():
    n,k = invr()
    sequence = inlt()

    number_of_players_available = 0
    for times_participated in sequence:
        remaining_chances = 5 - times_participated
        
        if remaining_chances >= k:
            number_of_players_available += 1 

    print(number_of_players_available//3)
    return 

def Nearly_Lucky_Number():
    num_as_string = insr()
    
    count_lucky_nums = 0
    for char in num_as_string:
        if char == '4' or char == '7':
            count_lucky_nums += 1 
    
    #print(count_lucky_nums)
    if count_lucky_nums == 0:
        print("NO")
    
    else:

        while count_lucky_nums > 0:

            digit = count_lucky_nums % 10
            count_lucky_nums = count_lucky_nums // 10
            
            if digit != 4 and digit != 7:
                print("NO")
                return 

        print("YES")
        return

def Presents():
    n = inp()
    giving_list = inlt()

    giving_dict = {}
    for index,friend in enumerate(giving_list):
        giving_dict[index+1] = friend

    receiving_dict = dict([(value,key) for key,value in giving_dict.items()])

    receiving_list = []
    for friend in range(n):
        receiving_list.append(receiving_dict[friend+1])
    
    outputStr = ' '.join(str(x) for x in receiving_list)
    print(outputStr)
    return

def Dividing_Orange():
    n,k = invr()  #k children, each gets n pieces
    total_num_pieces = n*k

    all_available_pieces_indices = [(i+1) for i in range(n*k)]

    desired_piece_list = inlt() 

    for desired_piece in desired_piece_list:
        all_available_pieces_indices.remove(desired_piece)

    outputStr = ''

    current_piece_index = 0

    for child in range(k):
        for piece in range(n):
            if piece == 0:
                outputStr += str(desired_piece_list[child]) + ' '                           
            else:
                outputStr += str(all_available_pieces_indices[current_piece_index]) + ' '                                
                current_piece_index += 1
        
        outputStr += '\n'
    
    outputStr = outputStr.strip()
    print(outputStr)
    return

def Queue_at_the_School():
    n,t = invr()
    sequence1 = insr()

    for time in range(t):
        sequence2 = []

        for child in sequence1:
            #print(sequence2)

            if len(sequence2) == 0:
                sequence2.append(child)
                previous_swapped = False

            else:
                if previous_swapped == False:
                    if child == 'G' and sequence2[len(sequence2)-1] == 'B':
                        sequence2[len(sequence2)-1] = 'G'
                        sequence2.append('B')
                        previous_swapped = True
                    else:
                        sequence2.append(child) 
                else:
                    sequence2.append(child)
                    previous_swapped = False

        sequence1 = sequence2

    outputStr = ''.join(x for x in sequence1)
    print(outputStr)
    return  

def Word():
    s1 = insr()

    uppaercase_count = 0
    lowercase_count = 0

    for char in s1:
        if char.isupper():
            uppaercase_count += 1
        else:
            lowercase_count += 1 
    
    string = ''.join(x for x in s1)
    if uppaercase_count > lowercase_count:
        print(string.upper())
    else:
        print(string.lower())
    
    return 

def Stones_on_the_Table():
    n = inp()
    sequence = insr()

    sequence2 = []
    removed_stones = 0

    for stone in sequence:
        if len(sequence2) == 0:
            sequence2.append(stone)
        else:
            if stone == sequence2[len(sequence2)-1]:
                removed_stones += 1
            else:
                sequence2.append(stone)
    
    print(removed_stones)
    return

def Beautiful_Year():
    def is_ditinct(num):
        digits = []
        while num > 0:
            digits.append(num % 10)
            num = num // 10 

        if len(digits) == len(list(set(digits))):
            return True
        else:
            return False

    year = inp()

    while True:
        year += 1
        if is_ditinct(year):
            print(year)
            return

def Vanya_and_Cards():
    n,x = invr()
    value_list = inlt()

    current_sum = 0
    for value in value_list:     #can be done as sum(value_list) also
        current_sum += value 
    
    if abs(current_sum) % x == 0:
        number_of_cards_needed = abs(current_sum)//x
    else:
        number_of_cards_needed = (abs(current_sum)//x) + 1
    print(number_of_cards_needed)
    return  

def Little_Elephant_and_Chess():
    rows = []
    for row_index in range(8):
        rows.append(insr())

    for row in rows:
        currentPtr = 0
        nextPtr = 1

        while nextPtr <= 7:
            if row[nextPtr] == row[currentPtr]:
                print("NO")
                return 
            currentPtr += 1
            nextPtr += 1
    
    print("YES")
    return

def Permutation():
    n = inp()
    sequence = inlt()

    count_dict = {}

    for num in sequence:
        if num not in count_dict.keys():
            count_dict[num] = 0

        count_dict[num] += 1

    elements_to_be_replaced = 0

    for num in count_dict.keys():
        if num > n:
            elements_to_be_replaced += count_dict[num]
        else:
            if count_dict[num] >= 2:
                elements_to_be_replaced += (count_dict[num]-1)

    print(elements_to_be_replaced)
    return 

def Magic_Numbers():
    sequence1 = insr()
    sequence2 = []

    for char in sequence1:
        added = False 

        if len(sequence2) == 0:
            if char == '1': #The string has to start with 1
                sequence2.append(char)
                added = True 

        else:
            if char == '1':
                sequence2.append(char)
                added = True
            
            elif char == '4' and sequence2[len(sequence2)-1] == '1':
                sequence2.append(char)
                added = True
            
            elif len(sequence2) >= 2:
                if char == '4' and sequence2[len(sequence2)-1] == '4' and sequence2[len(sequence2)-2] == '1':
                    sequence2.append(char)
                    added = True

        
        if not added:
            print("NO")
            return 
    
    print("YES")
    return

def Heads_or_Tails():
    x,y,a,b = invr()

    outputStr= ''
    numOutcomes = 0

    for ci in range(a,x+1):
        if b <= (ci-1):
            for di in range(b,(ci-1)+1):
                if di <= y:
                    numOutcomes += 1
                    outputStr += str(ci) + ' ' + str(di) + '\n'
    
    if numOutcomes == 0:
        print(numOutcomes)
    else:
        print(numOutcomes)
        outputStr = outputStr.strip()
        print(outputStr)
    return

def Marks():
    n,m  = invr()

    matrix_nm = []

    for student_index in range(n):
        string_list = insr()
        marks = list(map(int,string_list))
        matrix_nm.append(marks)
    
    successfull_students = []

    for subject_index in range(m):

        subject_wise_marks = [row[subject_index] for row in matrix_nm]
        subject_max_score = max(subject_wise_marks)

        for index,student_score in enumerate(subject_wise_marks):
            if student_score == subject_max_score:
                successfull_students.append(index)
    
    unique_succesfull_students = len(set(successfull_students))
    print(unique_succesfull_students)
    return 

def Twins():
    n = inp()
    sequence = inlt()

    sequence_sorted = sorted(sequence, reverse=True)
    total_sum = sum(sequence_sorted)

    num_of_coins_taken = 0
    current_personal_sum = 0
    remaining_sum = total_sum - current_personal_sum

    for coin_value in sequence_sorted:
        if current_personal_sum > remaining_sum:
            break 
        else:
            num_of_coins_taken += 1
            current_personal_sum += coin_value
            remaining_sum = total_sum - current_personal_sum

    print(num_of_coins_taken)
    return 

def Chat_room(): #Just have to check if there is h, e after h, l after e, l after l and o after l 
    string_list = insr()
    required_characters = ['h','e','l','l','o']

    checking_index = 0
    found_hello = False 

    for char in string_list:
        if char == required_characters[checking_index]:
            checking_index += 1 
        
        if checking_index == 5:
            found_hello = True 
            break 
    
    if found_hello:
        print("YES")
    else:
        print("NO")
    
    return 

def Football():
    player_sequence = insr()
    sequence2 = []

    for player in player_sequence:
        if len(sequence2) <= 5:
            sequence2.append(player)
        
        else:
            previous_6_players = sequence2[-6:]
            unique_players = list(set(previous_6_players))

            if len(unique_players) == 1 and player == unique_players[0]:
                print("YES")
                return 
            else:
                sequence2.append(player)
    
    print("NO")
    return

def Ilya_and_Bank_Account():
    def number_to_digitList(num):
        digits = []
        while num > 0 :
            digits.append(num % 10)
            num = num // 10 
        
        digits.reverse()  #digits list initially will contain ones place number at index 0
        return digits


    n = inp()

    if n >= 0:
        print(n)
    else:
        digits_list = number_to_digitList(-n)

 
        if digits_list[len(digits_list)-1] > digits_list[len(digits_list)-2]:
            index = len(digits_list)-1 
            digits_list.pop(index)
        else:
            index = len(digits_list)-2
            digits_list.pop(index)
        
        string_num = ''.join(str(x) for x in digits_list)
        
        if string_num == '0':
            print(string_num)
        else:
            string_num = '-' + string_num
            print(string_num)
        
    return

def  Playing_Cubes():
    def return_game_score(starting_color,R,B):
        num_red = R
        num_blue = B
        total_cubes = R + B

        if starting_color == 'red':
            last_cube_red  = True
            num_red -= 1
            cubes_placed = 1
        else:
            last_cube_red = False 
            num_blue -= 1
            cubes_placed = 1
        
        petya_turn = False
        vs_score = 0 
        pt_score = 0

        while cubes_placed <= (total_cubes-1):

            if not petya_turn:
                if last_cube_red and num_blue != 0:
                    last_cube_red = False  
                    num_blue -= 1
                    cubes_placed += 1 
                    vs_score += 1

                elif not last_cube_red and num_red != 0:
                    last_cube_red = True 
                    num_red -= 1 
                    cubes_placed += 1
                    vs_score += 1 

                elif last_cube_red:
                    last_cube_red = True 
                    num_red -= 1 
                    cubes_placed += 1 
                    pt_score += 1
                
                elif not last_cube_red:
                    last_cube_red = False 
                    num_blue -= 1 
                    cubes_placed += 1
                    pt_score += 1 
            
            else:
                if last_cube_red and num_red != 0:
                    last_cube_red = True 
                    num_red -= 1 
                    cubes_placed += 1
                    pt_score += 1

                elif not last_cube_red and num_blue != 0:
                    last_cube_red = False 
                    num_blue -= 1 
                    cubes_placed += 1
                    pt_score += 1

                elif last_cube_red:
                    last_cube_red = False 
                    num_blue -= 1
                    cubes_placed += 1
                    vs_score += 1

                elif not last_cube_red:
                    last_cube_red = True 
                    num_red -= 1 
                    cubes_placed += 1
                    vs_score += 1
            
            if petya_turn:
                petya_turn = False 
            else:
                petya_turn = True
        
        return pt_score,vs_score

    R,B = invr()

    pt_score1, vs_score1 = return_game_score('red',R,B)
    pt_score2,vs_score2 = return_game_score('blue',R,B)

    if pt_score1 > pt_score2:
        print(str(pt_score1) + ' ' + str(vs_score1))
    elif pt_score2 > pt_score1:
        print(str(pt_score2) + ' ' + str(vs_score2))
    elif vs_score1 < vs_score2:
        print(str(pt_score1) + ' ' + str(vs_score1))
    else:
        print(str(pt_score2) + ' ' + str(vs_score2))
    
    return

def Points_on_Line():
    n,d = invr()
    sequence = inlt()

    total_points = 0
    for start_index in range(n):
        for end_index in range(n-1,start_index+1,-1):
            if end_index - start_index <= 1:
                continue
            else:
                if sequence[end_index] - sequence[start_index] <= d:
                    total_points += (end_index - start_index) - 1
    
    print(total_points)
    return

def Points_on_Line2():
    import math 

    n,d = invr()
    sequence = inlt()

    if n == 1 or n == 2:
        print(0)
    else:
        left_index_count = {}
        left_index = 0 
        right_index = 2 

        while right_index <= (n-1) and (sequence[right_index] - sequence[left_index] <= d):
            right_index += 1

        right_index -= 1

        if (right_index - left_index - 1) == 0:
            left_index_count[left_index] = 0
        else:
            flexible_points = right_index - left_index
            left_index_count[left_index] = math.comb(flexible_points,2)
        
        for left_index in range(1,n-2):

            while right_index <= (n-1) and sequence[right_index] -sequence[left_index] <= d :
                right_index += 1
            
            right_index -= 1

            if right_index - left_index - 1 == 0:
                left_index_count[left_index] = 0 
            else:
                flexible_points = right_index - left_index
                left_index_count[left_index] = math.comb(flexible_points,2)
        

        total_points = 0
        for left_index in left_index_count.keys():
            total_points += left_index_count[left_index]
        print(total_points)

    return 

def Little_Pony_and_Expected_Maximum():
    from tqdm import tqdm
    import time 
    m,n = invr()

    prob_for_max_num_dict = {}
    total_possible_arrangements = m**n 

    for num in tqdm(range(1,m+1)):
        start = time.time()
        num_ways = (num**n) - ((num-1)**n)
        end = time.time()
        print(end-start)
        probability_to_get_num_max = num_ways/total_possible_arrangements
        prob_for_max_num_dict[num] = probability_to_get_num_max
    
    expected_value = 0
    for num in prob_for_max_num_dict.keys():
        expected_value += (num * prob_for_max_num_dict[num])
    
    print(expected_value)
    return 

def Little_Pony_and_Expected_Maximum2():
    m,n = invr()

    prob_for_max_num_dict = {}

    for num in (range(1,m+1)):
        probability = ((num/m)**n) - (((num-1)/m)**n)
        prob_for_max_num_dict[num] = probability
    
    expected_value = 0
    for num in prob_for_max_num_dict.keys():
        expected_value += (num * prob_for_max_num_dict[num])
    
    print(expected_value)
    return 

def Cosmic_Tables():
    n,m,k = invr()

    matrix = []
    outputStr =  ''

    for row_index in range(n):
        row = inlt()
        matrix.append(row)
    
    for q in range(k):
        query = input().split()

        if query[0] == 'g':
            #print(matrix[int(query[1])-1][int(query[2])-1])
            outputStr += str(matrix[int(query[1])-1][int(query[2])-1]) + '\n'

        elif query[0] == 'c':
            xi = int(query[1])-1
            yi = int(query[2])-1

            column_1 = [row[xi] for row in matrix]
            column_2 = [row[yi] for row in matrix]

            for row_index,row in enumerate(matrix):
                row[xi] = column_2[row_index]
                row[yi] = column_1[row_index]
        
        else:
            xi = int(query[1]) - 1
            yi = int(query[2]) - 1

            row_1 = matrix[xi]
            row_2 = matrix[yi]

            matrix[xi] = row_2
            matrix[yi] = row_1
    
    outputStr = outputStr.strip()
    print(outputStr)

    return 

def Cosmic_Tables2():
    n,m,k = invr()

    matrix = []

    rows_list = [i for i in range(n+1)]
    columns_list = [i for i in range(m+1)]

    for i in range(n):
        row = inlt()
        matrix.append(row)
    # print(matrix)
    outputStr = ''

    for i in range(k):
        query = input().split()

        if query[0] == 'g':
            row_id = rows_list[int(query[1])]
            column_id = columns_list[int(query[2])]
            # print(row_id-1)
            # print(column_id-1)
            outputStr += str(matrix[row_id-1][column_id-1]) + '\n'
        
        elif query[0] == 'c':
            xi = int(query[1])
            yi = int(query[2])

            dummy = columns_list[xi]
            columns_list[xi] = columns_list[yi]
            columns_list[yi] = dummy
        
        else:
            xi = int(query[1])
            yi = int(query[2])

            dummy = rows_list[xi]
            rows_list[xi] = rows_list[yi]
            rows_list[yi] = dummy
    
    outputStr = outputStr.strip()
    print(outputStr)
    return  

def Cosmic_Tables3():
    n,m,k = invr()

    matrix = []

    rows_dict = {i:i for i in range(n+1)}
    columns_dict = {i:i for i in range(m+1)}

    for i in range(n):
        row = inlt()
        matrix.append(row)
    # print(matrix)
    outputStr = ''

    for i in range(k):
        query = input().split()

        if query[0] == 'g':
            # print(row_id-1)
            # print(column_id-1)
            outputStr += str(matrix[rows_dict[int(query[1])]-1][columns_dict[int(query[2])]-1]) + '\n'
        
        elif query[0] == 'c':
            columns_dict[int(query[1])], columns_dict[int(query[2])] = columns_dict[int(query[2])],columns_dict[int(query[1])]
        
        else:
            rows_dict[int(query[1])],rows_dict[int(query[2])] = rows_dict[int(query[2])],rows_dict[int(query[1])]
    
    outputStr = outputStr.strip()
    print(outputStr)
    return  

def Lucky_Sum_of_Digits():    
    n = inp()

    lucky_num_sum_of_digits = [4,7]
    lucky_nums = [4,7]

    if n < 4: 
        print(-1)
        return 
    elif n == 4:
        print(4)
        return
    elif n > 4 and n < 7:
        print(-1)
        return 
    elif n == 7:
        print(7)
        return 
    
    pointer_index = 0 

    while True:
        #print(lucky_nums, pointer_index)
        num1 = (lucky_nums[pointer_index]*10) + 4 
        num2 = (lucky_nums[pointer_index]*10) + 7
        num1_sum_of_digits = lucky_num_sum_of_digits[pointer_index] + 4 
        num2_sum_of_digits = lucky_num_sum_of_digits[pointer_index] + 7 
        #print(num1_sum_of_digits,num2_sum_of_digits)

        if num1_sum_of_digits == n:
            print(num1)
            return 
        elif num2_sum_of_digits == n:
            print(num2)
            return 
        elif num1_sum_of_digits % 4 == 0 and n < num1_sum_of_digits:  ##start of a level
            print(-1)
            return 
        
        pointer_index += 1
        lucky_nums.append(num1)
        lucky_nums.append(num2)
        lucky_num_sum_of_digits.append(num1_sum_of_digits)
        lucky_num_sum_of_digits.append(num2_sum_of_digits)

def Lucky_Sum_of_Digits2():
    n = inp()

    possible_b = []
    possible_a = []
    num_of_digits = []

    b = 0
    while True:
        a_num = (n - (7*b))/4

        if a_num < 0 :
            break

        if a_num == int(a_num):
            possible_b.append(b)
            possible_a.append(int(a_num))
            num_of_digits.append(int(a_num) + b)
        
        b += 1 
    
    if len(possible_a) == 0:
        print(-1)
        return 
     
    # print(possible_a)
    # print(possible_b)
    # print(num_of_digits)
    min_digits = min(num_of_digits)
    final_a = min_digits
    final_b = min_digits

    for index,digits_count in enumerate(num_of_digits):

        if digits_count == min_digits:
            
            if possible_b[index] <= final_b:
                final_b = possible_b[index]
                final_a = possible_a[index]
    
    outputStr = ('4'*final_a) + ('7'*final_b)
    print(outputStr)
    return 

def Ice_Skating():
    n = inp()

    connected_components = {}
    total_components = 1 

    xi,yi = invr()
    connected_components[total_components] = [set(xi),set(yi)]

    for i in range(n-1):
        xi , yi = invr()
        found_path = False
        #print(connected_components)

        for component in connected_components.keys():
            if xi in connected_components[component][0] or yi in connected_components[component][1]:
                found_path = True 
                connected_components[component][0].append(xi)
                connected_components[component][1].append(yi)
                break 
        
        if not found_path:
            total_components += 1 
            connected_components[total_components] = [[xi],[yi]]
    
    print(total_components - 1)
    print(connected_components)
    return

def Ice_Skating2():
    def do_dfs(startNode):
        node_index = total_nodes.index(startNode)
        visited[node_index] = True 

        for neighbour in neighbours_dict[startNode]:
            node_index = total_nodes.index(neighbour)
            if visited[node_index] == False: 
                do_dfs(neighbour)

    n = inp()

    neighbours_dict = {}
    total_nodes = []
    for i in range(n):
        xi,yi = invr()
        node1 = str(xi) + '_x'
        node2 = str(yi) + '_y'

        if node1 not in neighbours_dict.keys():
            neighbours_dict[node1] = []
            total_nodes.append(node1)
        
        if node2 not in neighbours_dict.keys():
            neighbours_dict[node2] = []
            total_nodes.append(node2)

        neighbours_dict[node1].append(node2)
        neighbours_dict[node2].append(node1)
    
    for node in neighbours_dict.keys():
        neighbours_dict[node] = list(set(neighbours_dict[node]))
    
    visited = [False]*len(total_nodes)

    number_of_connected_components = 0
    while visited.count(False) > 0:
        number_of_connected_components += 1
        index_False = visited.index(False)
        node = total_nodes[index_False]
        do_dfs(node)
    
    print(number_of_connected_components-1)
    return

def Free_Cash():
    n = inp()

    sequence2_H = []
    sequence2_M = []
    longest_same_stream = 1
    current_same_stream = 1

    for i in range(n):
        h , m = invr()

        if len(sequence2_H) == 0:
            sequence2_M.append(m)
            sequence2_H.append(h)
        
        else:
            if h == sequence2_H[len(sequence2_H)-1] and m == sequence2_M[len(sequence2_M)-1]:
                current_same_stream += 1
                if current_same_stream > longest_same_stream:
                    longest_same_stream = current_same_stream
            else:
                current_same_stream = 1

            sequence2_M.append(m)
            sequence2_H.append(h)
    
    print(longest_same_stream)
    return 

def Mashmokh_and_ACM():
    def dvivisible_recur(sequence, count_good_sequences):

        if len(sequence) == k:
            count_good_sequences += 1 
            return count_good_sequences
        
        elif len(sequence) == 0:
            for i in range(1,n+1):
                sequence2 = sequence + [i]
                count_good_sequences = dvivisible_recur(sequence2,count_good_sequences)
        else:

            for i in range(1,n+1):
                penultimalte_num = sequence[len(sequence)-1]

                if i >= penultimalte_num and i % penultimalte_num == 0:
                    sequence2 = sequence + [i]
                    count_good_sequences = dvivisible_recur(sequence2, count_good_sequences) 
        
        return count_good_sequences

    n , k = invr()

    start_seq = []
    count_good_sequences = 0
    c = dvivisible_recur(start_seq,count_good_sequences)
    print(c)
    return 

def Mashmokh_and_ACM2():
    def dvivisible_recur(sequence, count_good_sequences):

        if len(sequence) == k:
            count_good_sequences += 1 
            return count_good_sequences
        
        elif len(sequence) == 0:
            for i in range(1,n+1):
                sequence2 = sequence + [i]
                count_good_sequences = dvivisible_recur(sequence2,count_good_sequences)
        else:
            penultimalte_num = sequence[len(sequence)-1]

            for i in range(penultimalte_num,n+1,penultimalte_num):
                sequence2 = sequence + [i]
                count_good_sequences = dvivisible_recur(sequence2,count_good_sequences)
        
        return count_good_sequences

    n , k = invr()

    start_seq = []
    count_good_sequences = 0
    c = dvivisible_recur(start_seq,count_good_sequences)
    print(c)
    return 

def Mashmokh_and_ACM3():
    def divide_recur(penultimate_num,length_of_sequence):

        if length_of_sequence != 0 and dp_matrix[penultimate_num-1][length_of_sequence-1] != -1:
            return dp_matrix[penultimate_num-1][length_of_sequence-1]
        
        elif length_of_sequence == k:
            return 1
               
        elif length_of_sequence != 0  and (penultimate_num*2) > n:
            return 1
        else:
            if length_of_sequence == 0:
                penultimate_num = 1
            
            total_ways = 0 
            for i in range(penultimate_num,n+1,penultimate_num):
                num_ways = divide_recur(i,length_of_sequence+1)
                dp_matrix[i-1][length_of_sequence] = (num_ways )
                total_ways += (num_ways )
            
            return total_ways
    
    n , k = invr()

    dp_matrix = []
    for i in range(n):
        row = [-1]*(k)
        dp_matrix.append(row)
    
    #print(dp_matrix)
    total_number_of_ways = divide_recur(-1,0)
    #print(dp_matrix)
    print(total_number_of_ways % ((10**9)+7))
    return

def Mashmokh_and_ACM4():
    n ,k = invr()

    dp_matrix = []
    for row_index in range(n+1):
        row = [-1]*(k+1)
        dp_matrix.append(row)
    
    for col_number in range(1,k+1):
        if col_number == 1:
            for num in range(1,n+1):
                dp_matrix[num][col_number] = 1 
        else:
            for num in range(1,n+1):
                new_value = 0
                for multiples in range(num,n+1,num):
                    new_value += dp_matrix[multiples][col_number-1]
                dp_matrix[num][col_number] = new_value 
    
    final_sum = 0 
    for num in range(1,n+1):
        final_sum += dp_matrix[num][k]
    
    print(final_sum % 1000000007)
    return
                
def Gargari_and_Bishops():
    n = inp()

    matrix = []
    for i in range(n):
        row = inlt()
        matrix.append(row)
    
    right_sloped_diagonals = [0]*((2*n)-1)
    left_sloped_diagonals = [0]*((2*n)-1)

    bottom_left_x = n 
    bottom_left_y = 1
    bottom_right_x = n
    bottom_right_y = n 

    for row_index in range(1,n+1):
        for col_index in range(1,n+1):
            cell_value = matrix[row_index-1][col_index-1]

            right_diagonal_index = abs(bottom_left_x - row_index) + abs(bottom_left_y - col_index)
            right_sloped_diagonals[right_diagonal_index] += cell_value

            left_diagonal_index = abs(bottom_right_x - row_index) + abs(bottom_right_y - col_index)
            left_sloped_diagonals[left_diagonal_index] += cell_value

    global_x_even = -1
    global_y_even = -1
    global_even_sum_max = -1

    global_x_odd = -1
    global_y_odd = -1
    global_odd_sum_max = -1 

    for row_index in range(1,n+1):
        for col_index in range(1,n+1):

            if (row_index + col_index) % 2 != 0 :

                current_cell_value = matrix[row_index-1][col_index-1]
                distance_right_sloped = abs(bottom_left_x - row_index) + abs(bottom_left_y - col_index)
                distance_left_sloped = abs(bottom_right_x - row_index) + abs(bottom_right_y - col_index)
                total_gain = right_sloped_diagonals[distance_right_sloped] + left_sloped_diagonals[distance_left_sloped] - current_cell_value

                if total_gain > global_odd_sum_max:
                    global_odd_sum_max = total_gain
                    global_x_odd = row_index
                    global_y_odd = col_index

            else:

                current_cell_value = matrix[row_index-1][col_index-1]
                distance_right_sloped = abs(bottom_left_x - row_index) + abs(bottom_left_y - col_index)
                distance_left_sloped = abs(bottom_right_x - row_index) + abs(bottom_right_y - col_index)
                total_gain = right_sloped_diagonals[distance_right_sloped] + left_sloped_diagonals[distance_left_sloped] - current_cell_value

                if total_gain > global_even_sum_max:
                    global_even_sum_max = total_gain
                    global_x_even = row_index
                    global_y_even = col_index
    
    print(global_even_sum_max + global_odd_sum_max)
    outputStr = str(global_x_even) + ' ' + str(global_y_even) + ' ' + str(global_x_odd) + ' ' + str(global_y_odd)
    print(outputStr)
    return

def Vasya_and_Basketball():
    n = inp()
    team_a_dist = inlt()
    m = inp()
    team_b_dist = inlt()
    team_b_counter = 0

    team_a_dist_sorted = sorted(team_a_dist)
    team_b_dist_sorted = sorted(team_b_dist)

    team_a_points = []
    team_b_points = []
    diff = []

    for index,a_dist in enumerate(team_a_dist_sorted):
        d = a_dist - 1 
        three_pointer_a = n - index
        two_pointer_a = n - three_pointer_a

        while team_b_counter <= (m-1) and team_b_dist_sorted[team_b_counter] <= d:
            team_b_counter += 1
        
        two_pointer_b = team_b_counter
        three_pointer_b = m - two_pointer_b

        points_a = (3*three_pointer_a) + (2*two_pointer_a)
        points_b = (3*three_pointer_b) + (2*two_pointer_b)
        team_a_points.append(points_a)
        team_b_points.append(points_b)
        diff.append(points_a-points_b)
    
    all_two_pointer_a = 2*n
    all_two_pointer_b = 2*m
    team_a_points.append(all_two_pointer_a)
    team_b_points.append(all_two_pointer_b)
    diff.append(all_two_pointer_a-all_two_pointer_b)

    # print(team_a_points)
    # print(team_b_points)
    # print(diff)

    max_index = diff.index(max(diff))
    print(str(team_a_points[max_index]) + ':' + str(team_b_points[max_index]))
    return 

def Tetrahedron():
    def recur_walk(current_pos,remaning_steps):


        if current_pos != 3 and remaning_steps == 1:
            return 1 
        
        elif current_pos != 3 and remaning_steps == 0:
            return 0
        
        elif current_pos == 3 and remaning_steps == 0:
            return 1

        elif current_pos == 3 and remaning_steps == 1:
            return 0 
        
        elif dp_matrix[current_pos][remaning_steps] != -1:
            return dp_matrix[current_pos][remaning_steps]
          
        else:
            total_paths = 0

            for vertex in range(4):
                if vertex != current_pos:
                    path = recur_walk(vertex,remaning_steps-1)
                    dp_matrix[vertex][remaning_steps-1] = path
                    total_paths += path 
            
            return total_paths

    n = inp()
    # 0 means A
    # 1 means B
    # 2 means C
    # 3 means D

    dp_matrix = []

    for vertex in range(4):
        row = [-1]*(n+1)
        dp_matrix.append(row)

    total_number_of_paths = recur_walk(3,n)
    #print(dp_matrix)
    print(total_number_of_paths % 1000000007)

def Tetrahedron2():
    def recur_walk(current_pos,remaning_steps):


        if current_pos != 1 and remaning_steps == 1:
            return 1 
        
        elif current_pos != 1 and remaning_steps == 0:
            return 0
        
        elif current_pos == 1 and remaning_steps == 0:
            return 1

        elif current_pos == 1 and remaning_steps == 1:
            return 0 
        
        elif dp_matrix[current_pos][remaning_steps] != -1:
            return dp_matrix[current_pos][remaning_steps]
          
        else:
            total_paths = 0

            if current_pos == 1:
                path = recur_walk(0,remaning_steps-1)
                total_paths += (3*path)
            
            else: 
                path1 = recur_walk(0,remaning_steps-1)
                path2 = recur_walk(1,remaning_steps-1)
                total_paths = (2*path1) + path2
            
            dp_matrix[current_pos][remaning_steps] = total_paths
            
            return total_paths

    n = inp()
    # 0 means A
    # 1 means B
    # 2 means C
    # 3 means D

    dp_matrix = []

    for vertex in range(2):
        row = [-1]*(n+1)
        dp_matrix.append(row)

    total_number_of_paths = recur_walk(1,n)
    #print(dp_matrix)
    print(total_number_of_paths % 1000000007)

def Tetrahedron3():
    n = inp()
    dp_matrix = []

    for pos_index in range(2):
        row = [-1]*(n+1)
        dp_matrix.append(row)
    
    dp_matrix[0][0] = 0
    dp_matrix[1][0] = 1
    dp_matrix[0][1] = 1
    dp_matrix[1][1] = 0

    for steps in range(2,n+1):
        dp_matrix[0][steps] = ((2*dp_matrix[0][steps-1]) + (dp_matrix[1][steps-1])) % 1000000007
        dp_matrix[1][steps] = (3*dp_matrix[0][steps-1]) % 1000000007
    
    total_number_ways = dp_matrix[1][n] % 1000000007
    print(total_number_ways)
    return 

def Color_the_Fence():
    v = inp()
    paint_sequence = inlt()    
    least_paint_required = min(paint_sequence)

    if v < least_paint_required:
        print(-1)
        return 


    num_list = [(i+1) for i,x in enumerate(paint_sequence) if x == least_paint_required]
    largest_num_for_least_paint = (num_list[len(num_list)-1])

    num_digits = v//least_paint_required

    useful_numbers = []
    corresponding_paints = []

    for index,paint in enumerate(paint_sequence):
        if (index+1) >= largest_num_for_least_paint:
            useful_numbers.append(index+1)
            corresponding_paints.append(paint)
    

    current_num = [largest_num_for_least_paint]*num_digits
    paint_used = num_digits * least_paint_required
    paint_remaining = v -paint_used

    for index in range(len(current_num)):
        print(1)
    return 

def Color_the_Fence2():
    v = inp()
    sequence = inlt()

    smallest_paint = min(sequence)

    if smallest_paint > v :
        print(-1)
        return
    
    smallest_paint_largest_num = -1

    for index,paint in enumerate(sequence):
        num = index + 1
        if paint == smallest_paint and num > smallest_paint_largest_num:
            smallest_paint_largest_num = num 
    
    base_number = [smallest_paint_largest_num] * (v//smallest_paint)
    length = v//smallest_paint
    extra_paint_each_digit = [(p-smallest_paint) for p in sequence]
    remaining_paint = v - (smallest_paint*length)

    for pos in range(length):
        for new_num in range(9,smallest_paint_largest_num,-1):
            if extra_paint_each_digit[new_num-1] <= remaining_paint:
                base_number[pos] = new_num
                remaining_paint -= extra_paint_each_digit[new_num-1]
                break 
    
    #print(base_number)
    outputStr = ''.join(str(x) for x in base_number)
    print(outputStr)
    return 


def Factory():
    def power_of_2(num):
        p = 1 
        while num % (2**p) == 0:
            p += 1
        return p - 1     

    a , m = invr()

    if m == 1 or m == 2 :
        print("Yes")
        return 

    power_of_2_m = power_of_2(m)
    power_of_2_a = power_of_2(a)

    t1 = int(m/(2**power_of_2_m))
    t2 = int(a/(2**power_of_2_a))

    if t2 % t1 != 0:
        print("No")
    else:
        print("Yes")
    return 

def Ping_Pong_Easy_Version():
    def create_neighbours(edges):
        neighbours_dict = {}
        total_nodes = set()
        for edge in edges:
            node1 = edge[0]
            node2 = edge[1]
            total_nodes.add(node1)
            total_nodes.add(node2)
            
            if node1 not in neighbours_dict.keys():
                neighbours_dict[node1] = []
            # if node2 not in neighbours_dict.keys():
            #     neighbours_dict[node2] = []
            
            neighbours_dict[node1].append(node2)
            # neighbours_dict[node2].append(node1)
        
        num_nodes = len(total_nodes)
        return neighbours_dict , num_nodes
    
    def do_dfs(visited,start_node, neighbours_dict):
        visited[start_node-1] = True 

        if start_node in neighbours_dict.keys():
            for neighbour in neighbours_dict[start_node]: 
                if visited[neighbour-1] == False:
                    do_dfs(visited, neighbour, neighbours_dict)
        
        return visited

    n = inp()
    node_a = []
    node_b = []
    edges = []
    outputStr=  ''
    current_node_index = 0

    for i in range(n):
        q,x,y = invr()
        if q == 1:
            current_node_index += 1
            node_index = 1 
            for a,b in zip(node_a,node_b):
                if x < a < y or x < b < y: 
                    edges.append((node_index,current_node_index))
                if a < x < b or a < y < b :   
                    edges.append((current_node_index, node_index))
                node_index += 1 
            
            node_a.append(x)
            node_b.append(y)
            #print(edges)
        else:
            neighbours_dict , num_nodes = create_neighbours(edges)
            #print("neighbours dict:", neighbours_dict)
            if x not in neighbours_dict.keys():
                outputStr += 'NO' + '\n'
                #print("NO")
            else:
                visited = [False]*current_node_index
                #print("visited:", visited)
                visited[x-1] = True
                visited = do_dfs(visited,x,neighbours_dict)
                #print("visited:", visited)
                if visited[y-1] == True:
                    outputStr += 'YES' + '\n'
                    #print("YES")
                else:
                    outputStr += 'NO' + '\n'
                    #print("NO") 
    
    outputStr = outputStr.strip()
    print(outputStr)

    return 

def Tourist_Problem():
    def compute_hcf(num1,num2):
        if num1 == 1 :
            return 1
        if num2 == 1:
            return 1
        
        y = min(num1,num2)
        if num1 == y :
            x = num2
        else:
            x = num1 
        
        while(y):
            x,y = y , x % y
        
        return x

    n = inp()
    sequence = inlt()
    sequence_sorted = sorted(sequence)

    total_sum = sum(sequence)

    modular_sum = 0 
    for index,element in enumerate(sequence_sorted):
        modular_sum += ((index*element) - ((n-1-index)*element))
    
    Nr = total_sum + 2*modular_sum 
    Dr = n 
    hcf = compute_hcf(Nr,Dr)
    Nr = Nr // hcf 
    Dr = Dr // hcf 
    print(str(Nr) + ' ' + str(Dr))
    return 

def Color_Stripe():
    n , k = invr()
    sequence = insr()

    color = 'A'
    possible_colors = ['A']
    for _ in range(k-1):
        last_color = possible_colors[len(possible_colors)-1]
        new_color = chr(ord(last_color)+1)
        possible_colors.append(new_color)

    if k > 2:
        colors_changed = 0 
        sequence2 = []

        for index,color in enumerate(sequence):

            if len(sequence2) == 0:
                sequence2.append(color)
            
            else:
                prev_color = sequence2[index-1]
                
                if color != prev_color:
                    sequence2.append(color)
                else:
                    if index + 1 <= (n-1) :
                        next_color = sequence[index + 1]
                        
                        for c in possible_colors:
                            if c != prev_color and c!= next_color:
                                sequence2.append(c)
                                colors_changed += 1
                                break                     
                    else:
                        for c in possible_colors:
                            if c != prev_color:
                                sequence2.append(c)
                                colors_changed += 1
                                break 
        
        print(colors_changed)
        print(''.join(x for x in sequence2))
    
    else:
        sequence2 = []
        colors_changed2 = 0 

        sequence3 = []
        colors_changed3 = 0 

        for index, color in enumerate(sequence):
            if index == 0:
                sequence2.append(color)
                for c in possible_colors:
                    if c != color:
                        sequence3.append(c)
                        colors_changed3 += 1
            else:
                prev_color2 = sequence2[index-1]
                prev_color3 = sequence3[index-1]

                if color != prev_color2:
                    sequence2.append(color)
                else:
                    for c in possible_colors:
                        if c != prev_color2:
                            sequence2.append(c)
                            colors_changed2 += 1 
                            break
                
                if color != prev_color3:
                    sequence3.append(color)
                else:
                    for c in possible_colors:
                        if c != prev_color3:
                            sequence3.append(c)
                            colors_changed3 += 1
                            break 
        
        if colors_changed2 < colors_changed3:
            print(colors_changed2)
            print(''.join(x for x in sequence2))

        else:
            print(colors_changed3)
            print(''.join(x for x in sequence3))
                    
    return

def Maze():
    def do_dfs(visited,neighbours_dict,start_node,visited_nodes,num_of_times_to_visit):
        #print(visited_nodes)
        if visited_nodes == num_of_times_to_visit:
            return visited , visited_nodes 
        
        visited[start_node] = True 
        visited_nodes += 1

        for neighbour in neighbours_dict[start_node]:
            if visited[neighbour] == False:
                visited, visited_nodes = do_dfs(visited,neighbours_dict,neighbour,visited_nodes,num_of_times_to_visit)
        
        return visited , visited_nodes

    n, m, k = invr()

    full_matrix = []
    for i in range(n):
        row = insr()
        full_matrix.append(row)

    #print(full_matrix)
    neighbours_dict = {}

    for row_index in range(n):
        for col_index in range(m):
            current_node_number  = (row_index*m) + col_index 
            neighbours_dict[current_node_number] = []

            if full_matrix[row_index][col_index] == '.':

                if (row_index - 1) >=0 and full_matrix[row_index-1][col_index] == '.':
                    node_number = ((row_index-1)*m) + col_index
                    neighbours_dict[current_node_number].append(node_number)

                if (row_index + 1) <= (n-1) and full_matrix[row_index + 1][col_index] == '.':
                    node_number = ((row_index+1)*m) + col_index
                    neighbours_dict[current_node_number].append(node_number)
                
                if (col_index-1) >= 0 and full_matrix[row_index][col_index-1] == '.':
                    node_number = ((row_index)*m) + (col_index-1)
                    neighbours_dict[current_node_number].append(node_number)
                
                if (col_index+1) <= (m-1) and full_matrix[row_index][col_index+1] == '.':
                    node_number = ((row_index)*m) + (col_index+1)
                    neighbours_dict[current_node_number].append(node_number)
    
    #print(neighbours_dict)
    nodes_part_of_connected_component = []

    total_num_nodes = 0
    for node in neighbours_dict.keys():
        if len(neighbours_dict[node]) != 0:
            nodes_part_of_connected_component.append(node)
        total_num_nodes += 1

    visited = [False]*total_num_nodes
    num_of_times_to_visit = len(nodes_part_of_connected_component) - k 

    #print(nodes_part_of_connected_component)
    start_node = nodes_part_of_connected_component[0]
    visited, visited_nodes = do_dfs(visited,neighbours_dict,start_node,0,num_of_times_to_visit)
    #print(visited, visited_nodes) 

    for node in nodes_part_of_connected_component:
        if visited[node] == False:
            row_index = node // m 
            col_index = node - (m*row_index)
            full_matrix[row_index][col_index] = 'X'

    for row in full_matrix:
        print(''.join(x for x in row))
    
    return 

def Maze2():
    from collections import deque 

    def do_bfs(startNode,neighbours_dict,total_num_nodes,num_of_times_to_visit):
        visited = [False]*total_num_nodes

        visited_count = 0 
        if visited_count == num_of_times_to_visit:
            return visited
        
        queue_list = deque([startNode])

        while len(queue_list) > 0 :
            last_node = queue_list.popleft()
            visited[last_node] = True 
            visited_count += 1
            

            if visited_count == num_of_times_to_visit:
                return visited
            

            for neighbour in neighbours_dict[last_node]:
                if not visited[neighbour] and neighbour not in queue_list:
                    queue_list.append(neighbour)
        
        return visited


    n, m, k = invr()

    full_matrix = []
    for i in range(n):
        row = insr()
        full_matrix.append(row)

    #print(full_matrix)
    neighbours_dict = {}

    for row_index in range(n):
        for col_index in range(m):
            current_node_number  = (row_index*m) + col_index 
            neighbours_dict[current_node_number] = []

            if full_matrix[row_index][col_index] == '.':

                if (row_index - 1) >=0 and full_matrix[row_index-1][col_index] == '.':
                    node_number = ((row_index-1)*m) + col_index
                    neighbours_dict[current_node_number].append(node_number)

                if (row_index + 1) <= (n-1) and full_matrix[row_index + 1][col_index] == '.':
                    node_number = ((row_index+1)*m) + col_index
                    neighbours_dict[current_node_number].append(node_number)
                
                if (col_index-1) >= 0 and full_matrix[row_index][col_index-1] == '.':
                    node_number = ((row_index)*m) + (col_index-1)
                    neighbours_dict[current_node_number].append(node_number)
                
                if (col_index+1) <= (m-1) and full_matrix[row_index][col_index+1] == '.':
                    node_number = ((row_index)*m) + (col_index+1)
                    neighbours_dict[current_node_number].append(node_number)
    
    #print(neighbours_dict)
    nodes_part_of_connected_component = []

    total_num_nodes = 0
    for node in neighbours_dict.keys():
        if len(neighbours_dict[node]) != 0:
            nodes_part_of_connected_component.append(node)
        total_num_nodes += 1

    num_of_times_to_visit = len(nodes_part_of_connected_component) - k 

    #print(nodes_part_of_connected_component)
    if len(nodes_part_of_connected_component) == 0:
        for row in full_matrix:
            print(''.join(x for x in row))

    else:
        start_node = nodes_part_of_connected_component[0]
        visited = do_bfs(start_node,neighbours_dict,total_num_nodes,num_of_times_to_visit)
        #print(visited, visited_nodes) 

        for node in nodes_part_of_connected_component:
            if visited[node] == False:
                row_index = node // m 
                col_index = node - (m*row_index)
                full_matrix[row_index][col_index] = 'X'

        for row in full_matrix:
            print(''.join(x for x in row))
    
    return 

def Valera_and_Tubes():
    n ,m ,k = invr()
 
    number_of_cells_for_first_pipe = (n*m) - ((2*k) - 2)
    outputStr = str(number_of_cells_for_first_pipe) + ' '
    total_cells = n*m 
 
 
    pipe_number = 1 
    cells_occupied = 0
 
    for cell_number in range(1,total_cells+1):
        cell_pos = cell_number - 1
        
        row_index = cell_pos // m 
        if row_index % 2 == 0:
            col_index = cell_pos - (row_index*m)
        else:
            col_index = m - (cell_pos - (row_index*m)) - 1 
        
        if pipe_number == 1:
            # cells[pipe_number].append(row_index+1)
            # cells[pipe_number].append(col_index+1)
            outputStr += str(row_index+1) + ' '+ str(col_index+1) + ' '
            cells_occupied += 1 
 
            if cells_occupied == number_of_cells_for_first_pipe:
                pipe_number = 2 
                #cells[pipe_number] = []
                first_addition = False 
                cells_occupied = 0 
        
        else:
            if not first_addition:
                outputStr += '\n'
                outputStr += '2' + ' '
                first_addition = True
            # cells[pipe_number].append(row_index+1)
            # cells[pipe_number].append(col_index+1)
            outputStr += str(row_index+1) + ' '+ str(col_index+1) + ' '
            cells_occupied += 1 
 
            if cells_occupied == 2:
                pipe_number += 1
                #cells[pipe_number] = []
                first_addition = False 
                cells_occupied = 0
 
    # outputStr = ''
    # for pipe_number in range(1,k+1):
    #     outputStr += str(len(cells[pipe_number])//2) + ' '
    #     new_str = ' '.join(str(x) for x in cells[pipe_number])
    #     outputStr += new_str + '\n'
    
    outputStr = outputStr.strip()
    print(outputStr)
 
    return
 
def Polo_the_Penguin_and_Matrix():
    n,m,d = invr()

    all_numbers = []

    for i in range(n):
        row = inlt()
        all_numbers = all_numbers + row 

    mod_value = all_numbers[0] % d 
    for n in all_numbers[1:]:
        new_mod_value = n % d 
        if new_mod_value != mod_value:
            print(-1)
            return 
    
    all_numbers_sorted = sorted(all_numbers)
    total_numbers = len(all_numbers_sorted)
    median_value = all_numbers_sorted[total_numbers//2]

    steps_required = 0 
    for n in all_numbers_sorted:
        steps_required += (abs(n - median_value))/d
    
    print(int(steps_required))
    return

def Funky_Numbers():
    import math 

    n = inp()
    k1_upper_bound = int(((math.sqrt((8*n) + 1) - 1)//2) + 1)
    #print(k1_upper_bound)

    for k1 in range(1,k1_upper_bound+1):
        c = (2*n) - (k1*(1+k1))
        if c > 0 :
            k2 = (math.sqrt(1 + (4*c)) -1)/2

            if k2 > 0  and k2 == int(k2):
                print("YES")
                return 
    
    print("NO")
    return

def Xenia_and_Weights():
    def do_xenia_recur(balance_value,previous_wt,step,available_weights,path,m):

        if len(all_paths) > 0 :
            return 

        path.append(previous_wt)

        if len(path) == m:
            all_paths.append(path)
            return
        else:
            for wt in available_weights:
                if wt != previous_wt:
                    
                    if step % 2 != 0 and balance_value - wt < 0 :
                        new_step = step + 1 
                        new_balance_value = balance_value - wt 
                        new_previous_wt = wt 
                        new_path = path.copy()
                        #print( "new balance value:", new_balance_value, " new previous wt:", new_previous_wt, " new_step:" , new_step , " path:", path)
                        do_xenia_recur(new_balance_value,new_previous_wt,new_step,available_weights,new_path,m)

                    elif step % 2 == 0 and balance_value + wt > 0:
                        new_step = step + 1 
                        new_balance_value = balance_value + wt 
                        new_previous_wt = wt 
                        #print(step , previous_wt, wt)
                        new_path = path.copy() 
                        #print( "new balance value:", new_balance_value, " new previous wt:", new_previous_wt, " new_step:" , new_step , " path:", path)
                        do_xenia_recur(new_balance_value,new_previous_wt,new_step,available_weights,new_path,m)
        
        return
            


    str1 = insr()
    m = inp()

    available_weights = []
    for index,char in enumerate(str1):
        if char == '1':
            available_weights.append(index+1)

    #print(available_weights)

    for wt in available_weights:
        #print("-"*50)
        #print("initial wt:", wt)
        balance_value = wt 
        previous_wt  = wt
        step = 1 
        path = []

        all_paths = []
        do_xenia_recur(balance_value,previous_wt,step,available_weights,path,m)
        if len(all_paths) > 0 :
            print("YES")
            print(' '.join(str(x) for x in all_paths[0]))
            return 
        
    print("NO")
    return

def Little_Pony_and_Sort_by_Shift():
    n = inp()
    sequence = inlt()
    sorted_sequence = sorted(sequence)

    smallest_num = min(sequence)
    smallest_num_indexs = [i for i,x in enumerate(sequence) if x == smallest_num]

    print(smallest_num_indexs)

    for index in smallest_num_indexs:
        after_list = sequence[index:]
        before_list = sequence[:index]
        new_list = after_list + before_list 
        #print(before_list,after_list,new_list)

        if new_list == sorted_sequence:
            if len(after_list) == n:
                print(0)
                return 
            else:
                print(len(after_list))
                return 

    print(-1)
    return  

def Little_Pony_and_Sort_by_Shift2():
    n = inp()
    sequence = inlt()
    sequence2 = []

    drop_index = -1

    for i,element in enumerate(sequence):
        if len(sequence2) == 0:
            sequence2.append(element)
        else:
            prev_element = sequence2[-1]
            #print(prev_element, element,drop_index)
            if element < prev_element and drop_index == -1: 
                drop_index = i
            
            elif element < prev_element  and drop_index != -1:
                print(-1)
                return 
            
            sequence2.append(element)

    #print(drop_index)
    min_first_rise = sequence[0]
    max_second_rise = sequence[-1]

    if drop_index == -1:
        print(0)
    else:
        if max_second_rise <= min_first_rise:
            print(n-drop_index)
        else:
            print(-1)
    
    return

def Bombs():
    n = inp()
    
    xcoor = []
    ycoor = []
    dist_from_origin = []

    for _ in range(n):
        x,y = invr()
        xcoor.append(x)
        ycoor.append(y)
        dist_from_origin.append(abs(x)+abs(y))
    
    sorted_data = sorted(zip(dist_from_origin,xcoor,ycoor))
    dist_from_origin_sorted, xcoor_acc, ycoor_acc = zip(*sorted_data)
    dist_from_origin_sorted = list(dist_from_origin_sorted)
    xcoor_acc = list(xcoor_acc)
    ycoor_acc = list(ycoor_acc)

    # print(dist_from_origin_sorted)
    # print(xcoor_acc)
    # print(ycoor_acc)

    outputStr = ''
    totalInstructions = 0

    for bomb_index in range(n):
        path_forward = []
        path_return = []
        xi = xcoor_acc[bomb_index]
        yi = ycoor_acc[bomb_index]

        command = '1' + ' ' + str(abs(xi)) + ' '
        if xi > 0:
            command_forward = command + 'R'
            path_forward.append(command_forward)
            command_retrun = command + 'L'
            path_return.append(command_retrun)
        elif xi < 0:
            command_forward = command + 'L'
            path_forward.append(command_forward)
            command_retrun = command + 'R'
            path_return.append(command_retrun)
        

        command = '1' + ' ' + str(abs(yi)) + ' '
        if yi > 0:
            command_forward = command + 'U'
            path_forward.append(command_forward)
            command_retrun = command + 'D'
            path_return.append(command_retrun)
        elif yi < 0:
            command_forward = command + 'D'
            path_forward.append(command_forward)
            command_retrun = command + 'U'
            path_return.append(command_retrun)

        totalInstructions += len(path_forward) + len(path_return) + 2

        for p in path_forward:
            outputStr += p + '\n'
        outputStr += '2' + '\n'
        for p in path_return:
            outputStr += p + '\n'
        outputStr += '3' + '\n'

    outputStr = str(totalInstructions) + '\n' + outputStr
    outputStr = outputStr.strip()
    print(outputStr)
    return

def Bombs2():
    def command_path(x,y):
        if x > 0:
            x_command_f = ' R'
            x_command_r = ' L'
        elif x < 0:
            x_command_f = ' L'
            x_command_r = ' R'

        if y > 0 :
            y_command_f = ' U'
            y_command_r = ' D'
        elif y < 0:
            y_command_f = ' D'
            y_command_r = ' U'

        if x !=0 and y != 0:
            path = '1 ' + str(abs(x)) + x_command_f + '\n' + '1 ' + str(abs(y)) + y_command_f + '\n' + '2' + '\n' + '1 ' + str(abs(x)) + x_command_r + '\n' + '1 ' + str(abs(y)) + y_command_r + '\n' + '3'
            instructions = 6
        elif x != 0:
            path = '1 ' + str(abs(x)) + x_command_f + '\n' + '2' + '\n' + '1 ' + str(abs(x)) + x_command_r + '\n' + '3'
            instructions = 4
        else:
            path = '1 ' + str(abs(y)) + y_command_f + '\n' + '2' + '\n' + '1 ' + str(abs(y)) + y_command_r + '\n' + '3'
            instructions = 4
        
        return path, instructions
    
    n = inp()
    
    dist_from_origin = []
    all_paths = []
    totalInstructions = 0
    for _ in range(n):
        x,y = invr()
        path,instructions = command_path(x,y)
        totalInstructions += instructions
        all_paths.append(path)
        dist_from_origin.append(abs(x)+abs(y))
    
    sorted_data = sorted(zip(dist_from_origin,all_paths))
    dist_from_origin_sorted, all_paths_acc = zip(*sorted_data)

    outputStr = '\n'.join(x for x in all_paths_acc)
    outputStr = str(totalInstructions) + '\n' + outputStr
    outputStr = outputStr.strip()
    print(outputStr)
    return

def Vanya_and_Exams():
    n,r,avg = invr()

    current_grade = []
    essay_cost = []

    for _ in range(n):
        ai,bi = invr()
        current_grade.append(ai)
        essay_cost.append(bi)
    
    extra_grade_needed = (n*avg) - sum(current_grade)
    
    if extra_grade_needed <= 0:
        print(0)
    else:
        sorted_data = sorted(zip(essay_cost,current_grade))
        essay_cost_sorted, current_grade_acc = zip(*sorted_data)

        number_of_essays = 0
        #print("extra grade needed:", extra_grade_needed)
        for bi,ai in zip(essay_cost_sorted,current_grade_acc):

            grade_extracted = min(extra_grade_needed, r-ai)
            extra_grade_needed = extra_grade_needed - grade_extracted
            
            #print(grade_extracted,bi)
            number_of_essays += (grade_extracted*bi)
            #print("extra grade needed:", extra_grade_needed)
            #print("number_of_essays:", number_of_essays)

            if extra_grade_needed == 0:
                break 
        
        print(number_of_essays)

    return 

def LCM_Challenge():
    n = inp()

    if n == 1:
        print(1)
    elif n == 2:
        print(2)
    elif n % 2 != 0 :
        print(n*(n-1)*(n-2))
    else:
        num1 = (n-1)*(n-2)*(n-3)
        num2 = (n*(n-1)*(n-2))//2

        if n % 3 == 0:
            hcf_n_n_3 = 3
        else:
            hcf_n_n_3 = 1 
        
        num3 = (n*(n-1)*(n-3)) // hcf_n_n_3 

        print(max(num1,num2,num3))
    
    return

def Caesar_Legions():
    def do_recur_caesar(remaining_footmen, remaining_horsemen, consecutive_footmen, consecutive_horsemen):

        
        if remaining_footmen == 0 and remaining_horsemen == 0:
            return 1 
        elif remaining_footmen == 0 and consecutive_horsemen == k2:
            return 0 
        elif remaining_horsemen == 0 and consecutive_footmen == k1:
            return 0 
        elif  dp_matrix[remaining_footmen][remaining_horsemen][consecutive_footmen][consecutive_horsemen] != -1:
            return  dp_matrix[remaining_footmen][remaining_horsemen][consecutive_footmen][consecutive_horsemen]
        else:            
            if remaining_footmen == 0:
                paths_added = do_recur_caesar(remaining_footmen,remaining_horsemen-1,0,consecutive_horsemen+1)

            elif remaining_horsemen == 0:
                paths_added = do_recur_caesar(remaining_footmen-1,remaining_horsemen,consecutive_footmen+1,0)

            elif consecutive_footmen == k1:
                paths_added = do_recur_caesar(remaining_footmen,remaining_horsemen-1,0,consecutive_horsemen+1)
        
            elif consecutive_horsemen == k2:
                paths_added = do_recur_caesar(remaining_footmen-1,remaining_horsemen,consecutive_footmen+1,0)
        
            else:
                paths_added = do_recur_caesar(remaining_footmen-1,remaining_horsemen,consecutive_footmen+1,0) + do_recur_caesar(remaining_footmen,remaining_horsemen-1,0,consecutive_horsemen+1)
            
            dp_matrix[remaining_footmen][remaining_horsemen][consecutive_footmen][consecutive_horsemen] = paths_added

            return paths_added

    n1,n2,k1,k2 = invr()
    dim1 = n1 + 1 
    dim2 = n2 + 1 
    dim3 = k1 + 1
    dim4 = k2 + 1
    dp_matrix = [[[[-1 for _ in range(dim4)] for _ in range(dim3)] for _ in range(dim2)] for _ in range(dim1)]
    total_possible_comb = do_recur_caesar(n1,n2,0,0)
    print(total_possible_comb % 100000000)
    return

def Array():
    n,k = invr()
    sequence = inlt()

    element_last_index_dict = {}

    for index,n in enumerate(sequence):
            element_last_index_dict[n] = index 
    
    elements = [key for key,value in element_last_index_dict.items()]
    last_indexes = [value for key,value in element_last_index_dict.items()]

    sorted_data = sorted(zip(last_indexes,elements))
    last_indexes_sorted, elements_acc = zip(*sorted_data)


    starting_index = last_indexes_sorted[0]
    corresponding_elements = [elements_acc[0]]
    ending_index = starting_index

    distinct_elements = 1
    
    current_index = starting_index
    for n in sequence[starting_index:]:
        if distinct_elements == k:
            break 
        if n not in corresponding_elements:
            corresponding_elements.append(n)
            distinct_elements += 1 
            ending_index = current_index
        
        current_index += 1
        
    if distinct_elements == k:
        print(str(starting_index+1) + ' ' + str(ending_index+1))
    else:
        print(str(-1) + ' ' + str(-1))
    
    return

def Array2():
    n,k = invr()
    sequence = inlt()

    count_dict = {}
    for element in sequence:
        if element not in count_dict.keys():
            count_dict[element] = 1
        else:
            count_dict[element] += 1
    
    if len(count_dict.keys()) < k:
        print(str(-1) + ' ' + str(-1))
    else:
        start_index = 0
        end_index = n-1 
        end_index_found = False 
        start_index_found = False 
        number_of_distinct_elements = len(count_dict.keys())

        for index in range(n-1,-1,-1):
            if end_index_found :
                break

            element = sequence[index]
            count_dict[element] -= 1

            if count_dict[element] == 0:
                number_of_distinct_elements -= 1

                if number_of_distinct_elements < k:
                    end_index = index
                    end_index_found = True 
        
        for index in range(n):
            if start_index_found: 
                break 

            element = sequence[index]
            count_dict[element] -= 1 

            if count_dict[element] == 0:
                number_of_distinct_elements -= 1

                if number_of_distinct_elements < k:
                    start_index = index
                    start_index_found = True 
        
        print(str(start_index+1) + ' ' + str(end_index+1))

def Palindrome_Transformation():
    n,p = invr()
    string_list = insr()
    number_list = [ord(c)-96 for c in string_list]
    mid_index = n//2
    largest_index = mid_index - 1 
    index = 0 

    total_increment = []
    while index <= largest_index:
        pos1 = number_list[index]
        pos2 = number_list[n-index-1]
        dist1 = abs(pos1-pos2)
        dist2 = 26-dist1
        total_increment.append(min(dist1,dist2))
        index += 1

    
    middle  = False 
    if p - 1 > largest_index:
        if n % 2 != 0:
            if p-1 == largest_index + 1:
                middle = True 
                pointer_location = 0 
            else:
                pointer_location = (p-1) % (len(total_increment)+1)
        
        else:
            pointer_location = (p-1) % len(total_increment)
        
        total_increment.reverse()
    else:
        pointer_location = p-1

    # print(total_increment)
    # print(pointer_location)
    # print(sum(total_increment))
    non_zero_indices = []

    for index,increase in enumerate(total_increment):
        if increase != 0:
            non_zero_indices.append(index)

    if len(non_zero_indices) == 0:
        print(0)
        return
    
    smallest_non_zero_index = min(non_zero_indices)
    largest_non_zero_index = max(non_zero_indices)

    if largest_non_zero_index < pointer_location:
        steps = pointer_location - smallest_non_zero_index
    elif smallest_non_zero_index > pointer_location:
        steps = largest_non_zero_index - pointer_location
    else:
        if largest_non_zero_index - pointer_location < pointer_location - smallest_non_zero_index:
            steps = (largest_non_zero_index - pointer_location) + (largest_non_zero_index-smallest_non_zero_index)
        else:
            steps = (pointer_location - smallest_non_zero_index) + (largest_non_zero_index-smallest_non_zero_index)
    
    #print(steps)
    print(steps + sum(total_increment))
    return

def Counting_Kangaroos_is_Fun():
    print(1)

def Number_of_Ways():
    n = inp()
    sequence = inlt()
    total_sum = sum(sequence)

    if total_sum % 3 != 0:
        print(0)
    else:
        sum_of_each_part = total_sum // 3 

        sum_till_that_index = []
        possible_i = []
        running_sum = 0 

        for index,num in enumerate(sequence):
            running_sum += num 
            sum_till_that_index.append(running_sum)

            if index <= (n-3) and running_sum == sum_of_each_part:
                possible_i.append(index+1)
            
        possible_pairs = 0 
        for i in possible_i:
            for j in range(i,n-1):
                reqd_sum = sum_till_that_index[j] - sum_till_that_index[i-1]
                if reqd_sum == sum_of_each_part:
                    possible_pairs += 1
        
        print(possible_pairs)

def Number_of_Ways2():
    n = inp()
    sequence = inlt()
    total_sum = sum(sequence)

    if total_sum % 3 != 0 :
        print(0)
    else:
        required_sum_of_each_part = total_sum // 3
        running_sum = 0

        possible_i_1 = [] 
        possible_j = [] 

        for index, num in enumerate(sequence):
            running_sum += num  

            if index <= (n-3) and running_sum == required_sum_of_each_part:
                possible_i_1.append(index)
            
            if index <= (n-2) and index >= 1 and running_sum == 2*required_sum_of_each_part:
                possible_j.append(index)
        
        #print(possible_i_1)

        pointer_j = 0
        total_possible_pairs = 0
        for i_1 in possible_i_1:
            while possible_j[pointer_j] <= i_1:
                pointer_j += 1 
            
            total_possible_pairs += len(possible_j) - (pointer_j)
        
        print(total_possible_pairs)
        #print(possible_j)
        #print(total_pairs)
    
    return 

def Team():
    zeros, ones = invr()

    if ones > zeros:
        extra_ones = ones - zeros 
        if extra_ones > (1*zeros)+2:
            print(-1)
        else:
            outputStr = ''
            if extra_ones  == (zeros) + 2:
                outputStr += '110'*zeros 
                outputStr += '11'
            elif extra_ones == (zeros) + 1:
                outputStr += '110'*zeros 
                outputStr += '1'
            elif extra_ones == (zeros):
                outputStr += "110"*zeros
            else:
                outputStr += '110'*extra_ones
                remaining_zeros = zeros - extra_ones
                outputStr += '10'*remaining_zeros
            print(outputStr)

    elif zeros > ones:
        extra_zeros = zeros - ones 
        if extra_zeros > 1 :
            print(-1)
        else:
            outputStr = '01'*ones 
            outputStr += '0'
            print(outputStr)

    else:
        outputStr = '01'
        outputStr = outputStr*zeros 
        print(outputStr)
    
    return 

def Another_Problem_on_Strings():
    def string_num(s):
        return(list(map(int,s[:len(s) - 1])))
    k = inp()
    string = input()
    sequence = string_num(string)

    count_dict = {}
    running_sum = 0
    for num in sequence:
        running_sum += num 
        if running_sum not in count_dict.keys():
            count_dict[running_sum] = 1 
        else:
            count_dict[running_sum] += 1 
    
    if 0 not in count_dict.keys():
        count_dict[0] = 1
    else:
        count_dict[0] += 1
    
    #print(count_dict)
    if k == 0:
        number_of_substrings = 0
        for sum in count_dict.keys():
            number_of_zeros = count_dict[sum] - 1
            number_of_substrings += ((number_of_zeros*(number_of_zeros+1)) // 2)
        print(number_of_substrings)
    
    else:
        number_of_substrings = 0
        for sum in count_dict.keys():
            if sum >= k:
                number_of_substrings += (count_dict[sum] * count_dict[sum - k])
        print(number_of_substrings)
    
    return



#Another_Problem_on_Strings()
#Team()
#Number_of_Ways2()
#Number_of_Ways()
#Counting_Kangaroos_is_Fun()
#Palindrome_Transformation()
#Array2()
#Array()
#Caesar_Legions()
#LCM_Challenge()
#Vanya_and_Exams()
#Bombs2()
#Bombs()
#Little_Pony_and_Sort_by_Shift2() 
#Little_Pony_and_Sort_by_Shift()   
#Xenia_and_Weights()
#Funky_Numbers()
#Polo_the_Penguin_and_Matrix()
#Valera_and_Tubes()
#Maze2()
#Maze()
#Color_Stripe()
#Tourist_Problem()
#Ping_Pong_Easy_Version()    
#Factory()
Color_the_Fence2()
#Color_the_Fence()
#Tetrahedron3()
#Tetrahedron2()                                  #MLE
#Tetrahedron()                                   #MLE
#Vasya_and_Basketball()  
#Gargari_and_Bishops()
#Mashmokh_and_ACM4() 
#Mashmokh_and_ACM3()  
#Mashmokh_and_ACM2()  
#Mashmokh_and_ACM()                               #TLE
#Free_Cash()
#Ice_Skating2()
#Ice_Skating()                                     
#Lucky_Sum_of_Digits2()
#Lucky_Sum_of_Digits()
#Cosmic_Tables3()
#Cosmic_Tables2()                                #Sol good, but gives TLE
#Cosmic_Tables()                                  #gives TLE, keep the track of changed indices for rows and columns
#Little_Pony_and_Expected_Maximum2() 
#Little_Pony_and_Expected_Maximum()               #gives TLE, directly calculate probability
#Points_on_Line2()
#Points_on_Line()
#Playing_Cubes()
#Ilya_and_Bank_Account()
#Football()
#Chat_room()
#Twins()
#Marks()
#Heads_or_Tails()
#Magic_Numbers()
#Permutation()
#Little_Elephant_and_Chess()
#Vanya_and_Cards()           
#Beautiful_Year()
#Stones_on_the_Table()
#Word()
#Queue_at_the_School()
#Dividing_Orange()
#Presents()
#Nearly_Lucky_Number()
#Choosing_Teams()

#ctrl + k ctrl + j to expand the code fragments
#ctrl + k ctrl + 0 to collapse the code fragments