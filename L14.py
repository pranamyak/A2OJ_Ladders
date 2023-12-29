import sys
#import threading
#sys.setrecursionlimit(10**8)
#threading.stack_size(10**8)
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

def Caisa_and_Pylons():
    n = inp()
    sequence = inlt()

    total_extra_energy = 0
    current_energy = 0 
    for index in range(1,len(sequence)):
        new_energy = sequence[index-1] - sequence[index]
        current_energy += new_energy

        if current_energy < 0:
            total_extra_energy += abs(current_energy)
            current_energy = 0 
    
    total_extra_energy += sequence[0] 
    print(total_extra_energy)
    return 

def Contest():
    a,b,c,d = invr()

    Misha_points = max((3*a)/10 , a - ((a/250)*c))
    Vasya_points = max((3*b)/10 , b - ((b/250)*d))

    if Misha_points > Vasya_points:
        print("Misha")
    elif Vasya_points > Misha_points:
        print("Vasya")
    else:
        print("Tie")
    
    return 

def Fox_and_Box_Accumulation():
    n = inp()
    sequence = inlt()
    sequence_sorted = sorted(sequence)
    visited = [False]*n 

    #print(sequence_sorted)
    piles = 0
    while visited.count(False) > 0:
        piles += 1 
        index_false = visited.index(False)
        #print(index)

        current_num_boxes = 1 
        visited[index_false] = True 

        for pointer in range(index_false+1,n):
            if visited[pointer] == False and sequence_sorted[pointer] >= current_num_boxes:
                current_num_boxes += 1
                visited[pointer] = True 
        #print(visited)
    
    print(piles)
    return

def Escape_from_Stones():
    string = insr()
    stone_right = []
    stone_left = []

    for index,movement in enumerate(string):
        if movement == 'l':
            stone_left.append(index+1)
        else:
            stone_right.append(index+1)

    for i in stone_right:
        print(i)
    stone_left.reverse()
    for i in stone_left:
        print(i)
    
    return 

def Party():
    def do_dfs(startNode):
        visited[startNode] = True 

        if startNode in neighbours_dict.keys():
            for neighbour in neighbours_dict[startNode]:
                if visited[neighbour] == False:
                    depth[neighbour] = depth[startNode] + 1 
                    do_dfs(neighbour)

    n = inp()
    
    root_nodes = []
    neighbours_dict = {}

    for i in range(n):
        manager = inp()
        if manager == -1:
            root_nodes.append(i)
        else:
            if (manager-1) not in neighbours_dict.keys():
                neighbours_dict[manager-1] = []
            neighbours_dict[manager-1].append(i)
    
    #print(root_nodes)
    #print(neighbours_dict)
    visited = [False]*n 
    depth = [-1]*n

    for startNode in root_nodes:
        depth[startNode] = 0
        do_dfs(startNode) 
    
    print(max(depth) + 1)
    return

def Booking_System():
    n = inp()
    request_index = []
    num_people = []
    money = []

    for i in range(n):
        c, p = invr()
        request_index.append(i+1)
        num_people.append(c)
        money.append(p)
    
    sorted_data = sorted(zip(money,num_people,request_index), reverse= True)
    money_sorted, num_people_acc, request_index_acc = zip(*sorted_data)

    k = inp()
    sequence = inlt()
    booked = [False]*len(sequence)

    outputStr = ''
    total_revenue = 0
    total_seated = 0 

    for index in range(len(num_people_acc)):
        revenue = money_sorted[index]
        size = num_people_acc[index]
        request_num = request_index_acc[index]
 
        current_table_size = max(sequence)
        current_table_index = -1

        for i,table in enumerate(sequence):
            if booked[i] == False:
                if table >= size and table <= current_table_size:
                    current_table_size = table 
                    current_table_index = i
        
        if current_table_index != -1:
            booked[current_table_index] = True 
            total_revenue += revenue
            total_seated += 1
            outputStr += str(request_num) + ' ' + str(current_table_index+1) + '\n'

    print(str(total_seated) + ' ' + str(total_revenue))
    outputStr = outputStr.strip()
    print(outputStr)
    return

def Fox_And_Names():
    n = inp()
    impossible = False 

    outgoing_edge_partner = {}
    incoming_edge_partner = {}
    dictinct_elements = set()
    name = insr()

    for i in range(n-1):
        prev_name = name 
        name = insr()

        length = min(len(name),len(prev_name))
        all_same = True 

        i = 0
        while i <= length-1:
            if prev_name[i] != name[i] and all_same:
                dictinct_elements.add(prev_name[i])
                dictinct_elements.add(name[i])

                all_same = False 
                if prev_name[i] not in outgoing_edge_partner.keys():
                    outgoing_edge_partner[prev_name[i]] = [name[i]]
                else:
                    outgoing_edge_partner[prev_name[i]].append(name[i])
                
                if name[i] not in incoming_edge_partner .keys():
                    incoming_edge_partner [name[i]] = [prev_name[i]]
                else:
                    incoming_edge_partner [name[i]].append(prev_name[i])
            
            i += 1
        
        if all_same and len(prev_name) > len(name):
            #print(prev_name , name)
            impossible = True 
    
    if impossible:
        print("Impossible")
        return
    
    #print(outgoing_edge_partner)
    #print(incoming_edge_partner)

    order_list = []
    no_incoming_edges_letter = []

    for letter in outgoing_edge_partner.keys():
        if letter not in incoming_edge_partner.keys():
            no_incoming_edges_letter.append(letter)

    #print(no_incoming_edges_letter)
    while len(no_incoming_edges_letter) > 0:
        #print("-"*50)
        #print(no_incoming_edges_letter)
        letter = no_incoming_edges_letter[0]
        if letter not in outgoing_edge_partner.keys():
            no_incoming_edges_letter.pop(0)
            order_list.append(letter)
        else:
            outgoing_partners = outgoing_edge_partner[letter]
            no_incoming_edges_letter.pop(0)
            order_list.append(letter)
        
            for p in outgoing_partners:
                #print(p ,incoming_edge_partner[p] )
                incoming_edge_partner[p].remove(letter)

                if len(incoming_edge_partner[p]) == 0:
                    no_incoming_edges_letter.append(p)
    
    # print(dictinct_elements)
    # print(order_list)
    if len(dictinct_elements) ==  len(order_list):
        outputStr = ''
        start_num = ord('a')

        for code in range(start_num,start_num + 26):
            char = chr(code)
            if char not in order_list:
                outputStr += char 
        
        newStr = ''.join(x for x in order_list)
        outputStr += newStr
        print(outputStr) 

    else:
        print("Impossible")
    
    return

def Fox_And_Names2():
    def do_cyclic_dfs(startNode):
        visited[startNode] = True
        dfs_visited[startNode] = True 

        if startNode in neighbours_dict.keys():
            for neighbour in neighbours_dict[startNode]:
                if visited[neighbour] == False:
                    do_cyclic_dfs(neighbour)
                elif visited[neighbour] == True and dfs_visited[neighbour] == True:
                    cycle_present[0] = True
        
        dfs_visited[startNode] = False 
        path.append(startNode)

    n = inp()
    impossible = False 

    neighbours_dict = {}
    dictinct_elements = set()
    name = insr()
    string1 = name 

    for i in range(n-1):
        prev_name = name 
        name = insr()

        length = min(len(name),len(prev_name))
        all_same = True 

        i = 0
        while i <= length-1 and all_same:
            if prev_name[i] != name[i]:
                dictinct_elements.add(prev_name[i])
                dictinct_elements.add(name[i])

                all_same = False 

                if prev_name[i] not in neighbours_dict.keys():
                    neighbours_dict[prev_name[i]] = []
                
                neighbours_dict[prev_name[i]].append(name[i])
            
            i += 1
        
        if all_same and len(prev_name) > len(name):
            impossible = True     
    
    if impossible:
        print("Impossible")
        return 
    
    root_nodes = []
    incoming_edge_nodes = set()

    for node in neighbours_dict.keys():
        for nd in neighbours_dict[node]:
            incoming_edge_nodes.add(nd)
    
    for node in neighbours_dict.keys():
        if node not in incoming_edge_nodes:
            root_nodes.append(node)
    
    # if string1 == ['a', 'd', 'j', 'c', 'q', 'u', 'q', 'd', 'q', 'c', 's', 'v', 'i', 'x', 'g', 'w', 'g', 'l', 'w', 'r', 'r', 'm', 'k', 'h', 'd', 's', 'b', 'e', 'b', 'b', 'j', 'v', 'c', 'g', 'z']:
    #     print(neighbours_dict['t'])

    order_list = []
    visited = {}
    dfs_visited = {}

    # if string1 == ['a', 'd', 'j', 'c', 'q', 'u', 'q', 'd', 'q', 'c', 's', 'v', 'i', 'x', 'g', 'w', 'g', 'l', 'w', 'r', 'r', 'm', 'k', 'h', 'd', 's', 'b', 'e', 'b', 'b', 'j', 'v', 'c', 'g', 'z']:
    #     print(root_nodes)

    for node in dictinct_elements:
        visited[node] = False
        dfs_visited[node] = False  

    for node in root_nodes:
        cycle_present = [False]
        path = []


        do_cyclic_dfs(node)
        # if string1 == ['a', 'd', 'j', 'c', 'q', 'u', 'q', 'd', 'q', 'c', 's', 'v', 'i', 'x', 'g', 'w', 'g', 'l', 'w', 'r', 'r', 'm', 'k', 'h', 'd', 's', 'b', 'e', 'b', 'b', 'j', 'v', 'c', 'g', 'z']:
        #     print("path:", path)
        # path.reverse()

        if cycle_present[0] == True:
            print("Impossible")
            return 
        
        order_list += path 
    
    order_list.reverse()

    if len(dictinct_elements) ==  len(order_list):
        outputStr = ''
        start_num = ord('a')

        for code in range(start_num,start_num + 26):
            char = chr(code)
            if char not in order_list:
                outputStr += char 
        
        newStr = ''.join(x for x in order_list)
        outputStr += newStr
        print(outputStr) 

    else:
        print("Impossible")
    return
        
def Fox_And_Two_Dots():
    def do_undirCyclic_dfs(startNode,parentNode):
        visited[startNode] = True 
        
        for neighbour in neighbours_dict[startNode]:
            if visited[neighbour] == False:
                do_undirCyclic_dfs(neighbour,startNode)
            elif visited[neighbour] == True and neighbour != parentNode:
                cyclePresent[0] = True 

    n, m = invr()

    full_matrix = []
    for i in range(n):
        row = insr()
        full_matrix.append(row)
    
    neighbours_dict = {}

    for row_index in range(n):
        for col_index in range(m):
            color = full_matrix[row_index][col_index]
            node_num = (row_index*m) + col_index
            neighbours_dict[node_num] = []

            if row_index + 1 <= (n-1) and full_matrix[row_index+1][col_index] == color:
                new_node_num = ((row_index+1)*m) + col_index
                neighbours_dict[node_num].append(new_node_num)
            
            if row_index - 1 >= 0 and full_matrix[row_index-1][col_index] == color:
                new_node_num = ((row_index-1)*m) + col_index
                neighbours_dict[node_num].append(new_node_num)

            if col_index + 1 <= (m-1) and full_matrix[row_index][col_index+1] == color:
                new_node_num = (row_index*m) + (col_index+1)
                neighbours_dict[node_num].append(new_node_num)
            
            if col_index - 1 >= 0 and full_matrix[row_index][col_index-1] == color:
                new_node_num = (row_index*m) + (col_index-1)
                neighbours_dict[node_num].append(new_node_num)
    
    #print(neighbours_dict)

    total_num_nodes = (n*m)
    visited = [False]*total_num_nodes
    cyclePresent = [False]

    while visited.count(False) > 0 :
        startNode = visited.index(False)
        do_undirCyclic_dfs(startNode,-1)
    
    if cyclePresent[0]:
        print("Yes")
    else:
        print("No")
    
    return 

def Pocket_Book():
    n, m = invr()
    different_letters_dict = {}
    for pos in range(m):
        different_letters_dict[pos] = set()
    
    for i in range(n):
        name = insr()
        for pos in range(m):
            different_letters_dict[pos].add(name[pos])
    
    num_different_names = 1
    for pos in range(m):
        num_different_names = num_different_names * len(different_letters_dict[pos])

    print(num_different_names % 1000000007)
    return   

def Ladder():
    n,m = invr()
    sequence = inlt()

    increasing_till_after_index = []
    increasing_till_before_index = []

    ptr1 = 0 
    ptr2 = 0

    while ptr1 <= (n-1):
        if ptr2 < ptr1:
            ptr2  = ptr1 

        while ptr2 <= (n-2) and sequence[ptr2+1] >= sequence[ptr2]:
            ptr2 += 1 
        
        increasing_till_after_index.append((ptr2))
        ptr1 += 1 
    
    #print(increasing_till_after_index)

    ptr1 = n-1
    ptr2 = n-1

    while ptr1 >= 0 :
        if ptr2 > ptr1:
            ptr2 = ptr1 

        while ptr2 >= 1 and sequence[ptr2-1] >= sequence[ptr2]:
            ptr2 -= 1 

        increasing_till_before_index.append(ptr2)
        ptr1 -= 1 

    increasing_till_before_index.reverse()
    #print(increasing_till_before_index)

    outputStr = ''

    for i in range(m):
        l,r = invr()

        if increasing_till_after_index[l-1] >= increasing_till_before_index[r-1]:
            #print("Yes")
            outputStr += 'Yes' + '\n'
        else:
            #print("No")
            outputStr += 'No' + '\n'  
    
    outputStr = outputStr.strip()
    print(outputStr)
    return 

def Divisibility_by_Eight():
    number_list = insr()
    n = len(number_list)

    for i in range(n):
        for j in range(i,n):
            for k in range(j,n):
                if i == j and j == k:
                    number_string = number_list[i]
                    num = int(number_string)
                    if num % 8 == 0: 
                        print("YES")
                        print(num)
                        return
                
                elif i == j or j == k:
                    number_string = number_list[i] + number_list[k] 
                    num = int(number_string)
                    if num % 8 == 0:
                        print("YES")
                        print(num)
                        return 
                else: 
                    number_string = number_list[i] + number_list[j] + number_list[k]
                    num = int(number_string)
                    if num % 8 == 0:
                        print("YES")
                        print(num)
                        return 
    
    print("NO")
    return 

def Little_Elephant_and_Problem():
    n = inp()
    sequence = inlt()
    sequence_sorted = sorted(sequence)

    s1_not_equal = []
    s2_not_equal = []

    for num1,num2 in zip(sequence, sequence_sorted):
        if num1 != num2:
            s1_not_equal.append(num1)
            s2_not_equal.append(num2)
    
    if (len(s1_not_equal) == 2 and s1_not_equal[0] == s2_not_equal[1] and s1_not_equal[1] == s2_not_equal[0]) or (len(s1_not_equal) == 0):
        print("YES")
    else:
        print("NO")
    
    return 

def Convex_Shape():
    n,m = invr()

    row_pos = []
    col_pos = []
    full_matrix = []

    for row_index in range(n):
        row = insr()
        full_matrix.append(row)
        for col_index in range(m):
            if row[col_index] == 'B':
                row_pos.append(row_index)
                col_pos.append(col_index)
    
    #print(row_pos)
    #print(col_pos)
    number_of_black_squares = len(row_pos)


    for i in range(number_of_black_squares):
        for j in range(i+1,number_of_black_squares):
            row_initial = row_pos[i]
            col_intial = col_pos[i]
            row_target = row_pos[j]
            col_target = col_pos[j]


            horizontal_steps = abs(row_target-row_initial)
            if row_target > row_initial:
                dx = 1 
            else:
                dx = -1 
            
            vertical_steps = abs(col_target - col_intial)
            if col_target > col_intial:
                dy = 1 
            else:
                dy = -1 
            
            path1_possible = True 
            path2_possible = True 

            r = row_initial
            c = col_intial
            for h in range(horizontal_steps):
                r = r + dx 
                if full_matrix[r][c] != 'B':
                    path1_possible = False
                    break  
            
            for v in range(vertical_steps):
                c = c + dy 
                if full_matrix[r][c] != 'B':
                    path1_possible = False
                    break  
            
            r = row_initial
            c = col_intial
            for v in range(vertical_steps):
                c = c + dy 
                if full_matrix[r][c] != 'B':
                    path2_possible = False
                    break  
            
            for h in range(horizontal_steps):
                r = r + dx 
                if full_matrix[r][c] != 'B':
                    path2_possible = False
                    break  
            
            if not path1_possible and not path2_possible:
                print("NO")
                return
    
    print("YES")
    return 

def Convex_Shape2():
    n,m = invr()

    full_matrix = []
    row_pos = []
    col_pos = [] 

    for row_index in range(n):
        row = insr()
        full_matrix.append(row)

        black_started = False 
        black_ended = False 

        for col_index in range(m):
            if row[col_index] == 'B':
                row_pos.append(row_index)
                col_pos.append(col_index)

                if not black_started:
                    black_started = True

                elif black_started and black_ended:
                    print("NO")
                    return 

            elif row[col_index] == 'W' and black_started:
                black_ended = True  
    
    for col_index in range(m):

        black_started = False 
        black_ended = False 

        for row_index in range(n): 

            if full_matrix[row_index][col_index] == 'B':
                if not black_started:
                    black_started = True 
                elif black_started and black_ended:
                    print("NO")
                    return 
            
            elif full_matrix[row_index][col_index] == 'W' and black_started:
                black_ended = True 
    
    num_black_squares = len(row_pos)

    for black_squre_index in range(num_black_squares):
        for next_index in range(black_squre_index+1,num_black_squares):
            row_inital = row_pos[black_squre_index]
            row_target = row_pos[next_index]
            col_initial = col_pos[black_squre_index]
            col_target = col_pos[next_index]

            if full_matrix[row_inital][col_target] != 'B' and full_matrix[row_target][col_initial] != 'B':
                print("NO")
                return 
    
    print("YES")
    return 

def View_Angle():
    import math 
    n = inp()

    angle_from_x_axis = []

    for i in range(n):
        x,y = invr()
        if x == 0 and y == 0:
            angle_from_x_axis.append(0.0)
        elif y == 0 and x > 0 :
            angle_from_x_axis.append(0.0)
        elif y == 0 and x < 0:
            angle_from_x_axis.append(180.0)
        elif x == 0 and y > 0:
            angle_from_x_axis.append(90.0)
        elif x == 0 and y < 0:
            angle_from_x_axis.append(270.0)
        else:
            alpha = math.atan(abs(y)/abs(x))
            alpha = (alpha *  180.0)/math.pi
            if x > 0 and y > 0 :
                angle_from_x_axis.append(alpha)
            elif y > 0  and x < 0 :
                angle_from_x_axis.append(180.0-alpha)
            elif x < 0 and y < 0:
                angle_from_x_axis.append(180.0+alpha)
            else:
                angle_from_x_axis.append(360.0-alpha)
    
    #print(angle_from_x_axis)
    angle_from_x_axis_sorted= sorted(angle_from_x_axis)
    S1 = angle_from_x_axis_sorted[-1] - angle_from_x_axis_sorted[0]
    final_viewing_angle = S1

    for i in range(1,n):
        if i == 1:
            S1 = S1 - (angle_from_x_axis_sorted[i] - angle_from_x_axis_sorted[i-1]) + (360 - angle_from_x_axis_sorted[-1] + angle_from_x_axis_sorted[0])
            final_viewing_angle = min(final_viewing_angle,S1)
        else:
            S1 = S1 - (angle_from_x_axis_sorted[i] - angle_from_x_axis_sorted[i-1]) + (angle_from_x_axis_sorted[i-1] - angle_from_x_axis_sorted[i-2])
            final_viewing_angle = min(final_viewing_angle,S1)            

    print(final_viewing_angle)
    return  

def Mr_Kitayuta_the_Treasure_Hunter():
    import math 

    def gem_collect_recur(pos,last_jump, max_farthest_location):
        if pos > max_farthest_location:
            return 0
        
        elif dp_matrix_dict[pos][last_jump] != -1:
            return dp_matrix_dict[pos][last_jump] 

        else:
            if pos in gem_location_count.keys():
                gem_found = gem_location_count[pos]
            else:
                gem_found = 0 

            if (last_jump - 1) > 0 :
                g1 = gem_collect_recur(pos + (last_jump-1), (last_jump-1), max_farthest_location)
            else:
                g1 = 0 
            
            g2 = gem_collect_recur(pos + last_jump, last_jump, max_farthest_location)
            g3 = gem_collect_recur(pos + (last_jump +1), (last_jump+1), max_farthest_location)
            
            gems_collected = gem_found + max(g1,g2,g3)
            dp_matrix_dict[pos][last_jump] = gems_collected
            return gems_collected


    n,d = invr()

    gem_location_count = {}
    max_farthest_location = -1
    for _ in range(n):
        pos = inp()
        if pos not in gem_location_count.keys():
            gem_location_count[pos] = 0

        gem_location_count[pos] += 1

        max_farthest_location = max(max_farthest_location,pos)

    dp_matrix_dict = {}
    max_jump_size = d + (int(((-(d+1) + math.sqrt(((d+1)**2) + 8*(max_farthest_location-d)))//2)) + 1) 

    for pos in range(d,max_farthest_location+1):
        row = [-1]*max_jump_size
        dp_matrix_dict[pos] = row


    total_gems_collected = gem_collect_recur(d,d, max_farthest_location)
    print(total_gems_collected)
    return 

def Checkposts():
    def create_topo_sort_dfs(startNode):
        visited[startNode] = True

        if startNode in neighbours_dict.keys():
            for neighbour in neighbours_dict[startNode]:
                if visited[neighbour] == False:
                    create_topo_sort_dfs(neighbour)

        topo_sort_order.append(startNode)  
    
    def do_dfs(startNode):
        visited[startNode] = True 
        path.append(startNode)

        if startNode in neighbours_reverse_dict.keys():
            for neighbour in neighbours_reverse_dict[startNode]:
                if visited[neighbour] == False:
                    do_dfs(neighbour)


    n = inp()
    cost_sequence = inlt()
    m = inp()

    neighbours_dict = {}
    neighbours_reverse_dict = {}

    for i in range(m):
        u,v = invr()
        if (u-1) not in neighbours_dict.keys():
            neighbours_dict[u-1] = []
        if (v-1) not in neighbours_reverse_dict.keys():
            neighbours_reverse_dict[v-1] = []
        
        neighbours_dict[u-1].append(v-1)
        neighbours_reverse_dict[v-1].append(u-1)
    
    topo_sort_order = []
    visited = [False]*n 
    while visited.count(False) > 0 :
        startNode = visited.index(False)
        create_topo_sort_dfs(startNode)
    
    topo_sort_order.reverse()
    

    visited = [False]*n 
    total_min_cost = 0 
    number_of_ways = 1
    
    for node in topo_sort_order:
        if visited[node] == False:
            path = []
            do_dfs(node)
            cost_for_this_scc = [cost_sequence[x] for x in path]
            minimum_junction_cost = min(cost_for_this_scc)

            total_min_cost += minimum_junction_cost
            number_of_ways = number_of_ways*cost_for_this_scc.count(minimum_junction_cost)
    
    print(str(total_min_cost) + ' ' + str(number_of_ways))
    return 

def Checkposts2():
    from collections import deque

    def do_tarjan_dfs(startNode):
        visited[startNode] = True 
        time_counter[0] += 1
        inTime[startNode] = time_counter[0]
        low_link_value[startNode] = inTime[startNode]

        stack_list.append(startNode)
        is_present_on_stack[startNode] = True 

        if startNode in neighbours_dict.keys():
            for neighbour in neighbours_dict[startNode]:
                if visited[neighbour] == False:
                    do_tarjan_dfs(neighbour)

                    if is_present_on_stack[neighbour]:
                        low_link_value[startNode] = min(low_link_value[startNode], low_link_value[neighbour]) 
                
                else:
                    if is_present_on_stack[neighbour]:
                        low_link_value[startNode] = min(low_link_value[startNode], inTime[neighbour])

        if low_link_value[startNode] == inTime[startNode]:
            part = []
            node_removed_from_stack = stack_list.pop()
            is_present_on_stack[node_removed_from_stack] = False
            part.append(node_removed_from_stack)

            while node_removed_from_stack != startNode:
                node_removed_from_stack = stack_list.pop()
                is_present_on_stack[node_removed_from_stack] = False
                part.append(node_removed_from_stack)
            
            all_scc.append(part)


    n = inp()
    cost_sequence = inlt()
    m = inp()

    neighbours_dict = {}

    for i in range(m):
        u,v = invr()
        if (u-1) not in neighbours_dict.keys():
            neighbours_dict[u-1] = []
        
        neighbours_dict[u-1].append(v-1) 
    
    stack_list= deque()
    is_present_on_stack = [False]*n
    visited = [False]*n 
    time_counter = [0]
    inTime=  [0]*n
    low_link_value = [0]*n
    all_scc = []

    while visited.count(False) > 0 :
        startNode = visited.index(False)
        do_tarjan_dfs(startNode)
    
    total_cost = 0 
    number_of_ways = 1

    for scc in all_scc:
        junction_costs = [cost_sequence[x] for x in scc]
        minimum_cost = min(junction_costs)
        num_junctions = junction_costs.count(minimum_cost)
        number_of_ways *= num_junctions
        total_cost += minimum_cost
    
    print(str(total_cost) + ' ' + str(number_of_ways))

    return 
    
def Misha_and_Forest():
    n = inp()

    xor_sum = []
    degree = []
    one_degree_nodes = []


    for node in range(n):
        u,s = invr()
        degree.append(u)
        xor_sum.append(s)
        
        if u == 1:
            one_degree_nodes.append(node)
    
    outputStr = ''
    number_of_edges = 0
    while len(one_degree_nodes) > 0 :
        
        node = one_degree_nodes.pop(0)
        if degree[node] == 1:
            neighbour = xor_sum[node]
            outputStr += str(node) + ' ' + str(neighbour) + '\n'
            number_of_edges += 1
            degree[neighbour] -= 1
            xor_sum[neighbour] = xor_sum[neighbour] ^ node 

            if degree[neighbour] == 1:
                one_degree_nodes.append(neighbour)
    
    print(number_of_edges)
    outputStr = outputStr.strip()
    print(outputStr)
    return 

def Kolya_and_Tandem_Repeat():
    string = insr()
    k = inp()

    for i in range(k):
        string.append(-1)

    n = len(string)
    max_tandom_length = len(string) // 2

    for tandom_length in range(max_tandom_length,0,-1):
        ptr1 = 0 
        ptr2 = ptr1 + tandom_length
        current_matching_length = 0 

        while ptr2 <= (n-1):
            if string[ptr1] == string[ptr2] or string[ptr1] == -1 or string[ptr2] == -1:
                current_matching_length += 1
            else:
                current_matching_length = 0 
            
            if current_matching_length == tandom_length:
                print(2*tandom_length)
                return
            
            ptr1 += 1
            ptr2 += 1
    
    return 

def Removing_Columns():
    n,m = invr()
    words = []

    for i in range(n):
        word = insr()
        words.append(word)

    columns_intact = []
    for col_index in range(m):

        lexigraphically_oredered = True 
        prev_word = -1 
        for word in words:
            new_word = ''.join(word[x] for x in columns_intact)
            new_word += word[col_index]
            if prev_word == -1:
                prev_word = new_word
            else:
                if prev_word > new_word:
                    lexigraphically_oredered = False 
                    break 
                else:
                    prev_word = new_word
        
        if lexigraphically_oredered:
            columns_intact.append(col_index)
    
    print(m - len(columns_intact))
    return 
            
def Beautiful_Numbers():
    def is_good_sum(a,b,num):
        while num > 0 :
            digit = num % 10
            num = num // 10

            if digit != a and digit != b:
                return False 
        
        return True 
    
    import math 

    a,b,n = invr()
    total_combinations = 0

    for i in range(n+1):
        sum_of_num = (a*i) + (b*(n-i))
        #print(sum_of_num)

        if is_good_sum(a,b,sum_of_num):
            number_of_ways = math.comb(n,i)
            number_of_ways = number_of_ways % 1000000007
            total_combinations += number_of_ways
    
    print(total_combinations % 1000000007)
    return

def Beautiful_Numbers2():
    def is_good_sum(a,b,num):
        while num > 0 :
            digit = num % 10
            num = num // 10

            if digit != a and digit != b:
                return False 
        
        return True 

    a,b,n = invr()
    x = 1000000007



    factorial_calc = []
    for i in range(n+1):
        if i == 0:
            factorial_calc.append(1)
        else:
            new_num = (factorial_calc[-1] * i) % x
            factorial_calc.append(new_num)
        
    total_combinations = 0 

    for i in range(n+1):
        sum_of_num = (a*i) + (b*(n-i))
        #print(sum_of_num)

        if is_good_sum(a,b,sum_of_num):
            number_of_ways = factorial_calc[n] * pow(factorial_calc[i]*factorial_calc[n-i], x-2, x)
            number_of_ways = number_of_ways % x
            total_combinations += number_of_ways
    
    print(total_combinations % x)
    return

def Vasya_and_Chess():
    n = inp()

    if n % 2 == 0:
        print("white")
        print(str(1) + ' ' + str(2))
    else:
        print("black")

def Colorful_Graph():
    n,m = invr()
    color_sequence = inlt()
    
    Q_k_dict = {}
    for color in color_sequence:
        Q_k_dict[color] = set()

    for i in range(m):
        node1, node2 = invr()
        color_node1 = color_sequence[node1-1]
        color_node2 = color_sequence[node2-1]

        if color_node1 != color_node2:
            Q_k_dict[color_node1].add(color_node2)
            Q_k_dict[color_node2].add(color_node1)
    
    max_cardinality = -1
    corresponding_color = -1 

    for color in Q_k_dict.keys():
        if len(Q_k_dict[color]) > max_cardinality:
            max_cardinality = len(Q_k_dict[color])
            corresponding_color = color 
        elif len(Q_k_dict[color]) == max_cardinality:
            corresponding_color = min(corresponding_color,color)
 
    print(corresponding_color)
    return 

def To_Add_or_Not_to_Add():
    def check_if_possible(n,t,k,sorted_sequence,sum_list):
        if t == 1:
            return True, sorted_sequence[0]
        else:
            for i in range(t-1,n):
                if i - (t-1) -1 < 0:
                    required_increase = (sorted_sequence[i] * (t-1)) - sum_list[i-1]
                else:
                    required_increase = (sorted_sequence[i] * (t-1)) - (sum_list[i-1] - sum_list[i-(t-1)-1])

                if required_increase <= k:
                    return True, sorted_sequence[i] 
        
        return False, -1
    
    n, k = invr()
    sequence = inlt()
    sorted_sequence = sorted(sequence)

    sum_list = []
    running_sum = 0 
    for num in sorted_sequence:
        running_sum += num 
        sum_list.append(running_sum)
    
    left = 1 
    right = n 

    while left <= right:
        mid = (left + right)//2 

        bool_check, element = check_if_possible(n,mid,k,sorted_sequence,sum_list)

        if bool_check:
            left = mid + 1
        else:
            right = mid - 1 
    

    bool_check, element = check_if_possible(n,mid,k,sorted_sequence,sum_list)
    if not bool_check:
        bool_check, element = check_if_possible(n,mid-1,k,sorted_sequence,sum_list)
        print(str(mid-1) + ' ' + str(element))
    else:
        print(str(mid) + ' ' + str(element))
    
    return
    
def Arithmetic_Progression():
    n = inp()
    sequence = inlt()
    sequence_sorted = sorted(sequence)

    if n == 1:
        print(-1)
        return 
    
    elif n == 2:
        diff = sequence_sorted[1] - sequence_sorted[0]

        if diff % 2 == 0 and diff > 0:
            print(3)
            card_value1 = sequence_sorted[0] - diff 
            card_value2 = sequence_sorted[0] + (diff//2)
            card_value3 = sequence_sorted[1] + diff 
            print(str(card_value1) + ' ' + str(card_value2) + ' ' + str(card_value3))
            return 
        
        elif diff % 2 != 0 and diff > 0:
            print(2)
            card_value1 = sequence_sorted[0] - diff 
            card_value2 = sequence_sorted[1] + diff 
            print(str(card_value1) + ' ' + str(card_value2))
            return 
        else:
            print(1)
            print(sequence_sorted[0])
            return
    
    else:
        ptr = 2
        fixed_common_difference = -1 
        card_used = False
        card_value = -1

        while ptr <= (n-1):
            if ptr == 2:
                cd1 = sequence_sorted[ptr] - sequence_sorted[ptr-1]
                cd2 = sequence_sorted[ptr-1] - sequence_sorted[ptr-2]

                if cd1 != cd2:
                    if cd2 >  cd1 and 2*cd1 == cd2:
                        card_used = True 
                        card_value = sequence_sorted[ptr-2] + cd1
                        fixed_common_difference = cd1 

                    elif cd1 > cd2  and 2*cd2 == cd1:
                        card_used = True 
                        card_value = sequence_sorted[ptr-1] + cd2  
                        fixed_common_difference = cd2
                    
                    else:
                        print(0)
                        return 
                
                else:
                    fixed_common_difference = cd1
                
                ptr += 1
            
            else:
                current_cd = sequence_sorted[ptr] - sequence_sorted[ptr-1]

                if current_cd != fixed_common_difference:

                    if current_cd > fixed_common_difference and 2*fixed_common_difference == current_cd and not card_used:
                        card_used = True 
                        card_value = sequence_sorted[ptr-1] + fixed_common_difference
                    
                    else:
                        print(0)
                        return 

                ptr += 1

        if card_used:
            print(1)
            print(card_value)
        elif not card_used and fixed_common_difference == 0:
            print(1)
            print(sequence_sorted[0])
        else:
            print(2)
            card_value1 = sequence_sorted[0] - fixed_common_difference
            card_value2 = sequence_sorted[-1] + fixed_common_difference
            print(str(card_value1) + ' ' + str(card_value2))
        
    return 
                
def Friends_and_Presents():
    a,b,p1,p2 = invr()

    current_num = 1

    count_present_for_F1 = 0 
    count_present_for_F2 = 0 
    count_present_for_both = 0

    while(True):
        if current_num % p1 == 0 and current_num % p2 == 0:
            current_num += 1
            continue
        
        elif current_num % p1 != 0 and current_num % p2 == 0:
            count_present_for_F1 += 1
        
        elif current_num % p1 == 0 and current_num % p2 != 0:
            count_present_for_F2 += 1
        
        else:
            count_present_for_both += 1
        
        remaining_present_for_F1 = a - count_present_for_F1
        remaining_present_for_F2 = b - count_present_for_F2 

        if remaining_present_for_F1 <= count_present_for_both:
            remaining_present_from_both = count_present_for_both - remaining_present_for_F1
            if remaining_present_for_F2 <= remaining_present_from_both:
                break 
        
        current_num += 1
    
    print(current_num)
    return 

def Friends_and_Presents2():
    def check_if_present_possible(v,a,b,p1,p2):
        numbers_divisible_by_p1 = v//p1 
        numbers_divisible_by_p2 = v//p2 
        numbers_divisible_by_both = v//(p1*p2)
        numbers_divisible_by_only_p1 = numbers_divisible_by_p1 - numbers_divisible_by_both
        numbers_divisible_by_only_p2 = numbers_divisible_by_p2 - numbers_divisible_by_both
        free_numbers = v - (numbers_divisible_by_only_p1 + numbers_divisible_by_only_p2 + numbers_divisible_by_both)

        remaining_for_F1 = a - numbers_divisible_by_only_p2 
        remaining_for_F2 = b - numbers_divisible_by_only_p1

        if remaining_for_F1 <= 0 and remaining_for_F2 <= 0:
            return True 
        elif remaining_for_F1 <=0 and remaining_for_F2 > 0:
            if remaining_for_F2 <= free_numbers:
                return True 
            else:
                return False 
        elif remaining_for_F2 <= 0 and remaining_for_F1 > 0:
            if remaining_for_F1 <= free_numbers:
                return True 
            else:
                return False 
        else:
            remaining_free_numbers = free_numbers - remaining_for_F1
            if remaining_free_numbers < remaining_for_F2:
                return False 
            else:
                return True


    a,b,p1,p2 = invr()

    max_number = (a+b)*(max(p1,p2))
    left = 1 
    right = max_number

    while left <= right:
        mid = (left + right)//2

        if check_if_present_possible(mid,a,b,p1,p2):
            right = mid -1 
        else:
            left = mid + 1
    
    if check_if_present_possible(mid,a,b,p1,p2):
        v = mid 
    else:
        v = mid + 1
    
    print(v)
    return

def Barcode():
    def count_changes(sum_count_dots,col_index,num_columns,to_change_to_dots,n,m):
        if col_index + num_columns -1 > m-1 :
            return (n*m)
        else:

            if not to_change_to_dots:
                if col_index == 0:
                    reversal = sum_count_dots[col_index+num_columns-1]
                else:
                    reversal = sum_count_dots[col_index+num_columns-1] - sum_count_dots[col_index-1]
            
            else:
                if col_index == 0:
                    reversal = (num_columns*n) - sum_count_dots[col_index+num_columns-1]
                else:
                    reversal = (num_columns*n) - (sum_count_dots[col_index+num_columns-1] - sum_count_dots[col_index-1])
            
            return reversal
 
    def bar_recur(consective_dots,consecutive_hash,sum_count_dots,col_index,n,m):
        if col_index == m:
            return 0 
        
        elif col_index > m:
            return (n*m)
        
        elif dp_matrix[consective_dots][consecutive_hash][col_index] != -1:
            return dp_matrix[consective_dots][consecutive_hash][col_index]

        else:
            if consective_dots == 0 and consecutive_hash == 0:
                changes1 = count_changes(sum_count_dots,col_index,x,True,n,m) + bar_recur(x,0,sum_count_dots,col_index+x,n,m)
                changes2 = count_changes(sum_count_dots,col_index,x,False,n,m) + bar_recur(0,x,sum_count_dots,col_index+x,n,m)
                dp_matrix[consective_dots][consecutive_hash][col_index] = min(changes1,changes2)
                return dp_matrix[consective_dots][consecutive_hash][col_index]
            
            elif consective_dots < y and consecutive_hash == 0:
                changes1 = count_changes(sum_count_dots,col_index,1,True,n,m) + bar_recur(consective_dots+1,0,sum_count_dots,col_index+1,n,m)
                changes2 = count_changes(sum_count_dots,col_index,x,False,n,m) + bar_recur(0,x,sum_count_dots,col_index+x,n,m)
                dp_matrix[consective_dots][consecutive_hash][col_index] = min(changes1,changes2)
                return dp_matrix[consective_dots][consecutive_hash][col_index]
            
            elif consective_dots == 0 and consecutive_hash < y:
                changes1 = count_changes(sum_count_dots,col_index,x,True,n,m) + bar_recur(x,0,sum_count_dots,col_index+x,n,m)
                changes2 = count_changes(sum_count_dots,col_index,1,False,n,m) + bar_recur(0,consecutive_hash+1,sum_count_dots,col_index+1,n,m)
                dp_matrix[consective_dots][consecutive_hash][col_index] = min(changes1,changes2)
                return dp_matrix[consective_dots][consecutive_hash][col_index]
            
            elif consective_dots == y:
                changes = count_changes(sum_count_dots,col_index,x,False,n,m) + bar_recur(0,x,sum_count_dots,col_index+x,n,m)
                dp_matrix[consective_dots][consecutive_hash][col_index] = changes
                return dp_matrix[consective_dots][consecutive_hash][col_index]
            
            elif consecutive_hash == y:
                changes = count_changes(sum_count_dots,col_index,x,True,n,m) + bar_recur(x,0,sum_count_dots,col_index+x,n,m)
                dp_matrix[consective_dots][consecutive_hash][col_index] = changes
                return dp_matrix[consective_dots][consecutive_hash][col_index]      

    n,m,x,y = invr()

    num_dots = [0]*m
    for i in range(n):
        row = insr()
        for col_index,element in enumerate(row):
            if element == '.':
                num_dots[col_index] += 1
    
    sum_count_dots = []
    running_sum = 0
    for count in num_dots:
        running_sum += count 
        sum_count_dots.append(running_sum)

    continuous_hashes = y 
    continuous_dots = y 
    num_columns = m
    dp_matrix = [[[-1 for _ in range(num_columns+1)] for _ in range(continuous_hashes+1)] for _ in range(continuous_dots+1)]
    final_answer = bar_recur(0,0,sum_count_dots,0,n,m)
    print(final_answer)
    return

def Long_Jumps():
    def contains_mark(increment, sequence):
        return any(i+increment in  sequence for i in sequence)
    
    def check1(sequence):
        for num in sequence:
            if num + x + y in sequence:
                return num + x 
        
        return False 
    
    def check2(sequence):
        for num in sequence:
            if num + y - x in sequence:
                if num + y <= l:
                    return num + y 
                if num - x >= 0:
                    return num - x
        
        return False 

    n,l,x,y = invr()
    sequence = (set(map(int,input().split())))  #IF WE USE INLT WE GET TLE, TO CHECK IF A ELEMENT IS PRESENT OR NOT, SET IS BETTER THAN LIST

    measure_x_possible = contains_mark(x,sequence)
    measure_y_possible = contains_mark(y,sequence)
    
    if measure_x_possible and measure_y_possible:
        print(0)
        return

    elif measure_x_possible:
        print(1)
        print(y)
        return
    
    elif measure_y_possible:
        print(1)
        print(x)
        return
    
    else:
        result1 = check1(sequence)
        
        if result1:
            print(1)
            print(result1)
            return
        
        else:
            result2 = check2(sequence)

            if result2:
                print(1)
                print(result2)
                return
            else:
                print(2)
                print(str(x) + ' ' + str(y))
                return

def Valera_and_Elections():
    def do_dfs(startNode):
        visited[startNode] = True
        if startNode in white_nodes:
            subtree_problem_road_count[startNode] += 1
             
        
        for neighbour in neighbours_dict[startNode]:
            if not visited[neighbour]:
                do_dfs(neighbour)
                subtree_problem_road_count[startNode] += subtree_problem_road_count[neighbour]


    n = inp()

    neighbours_dict = {}
    white_nodes = set()

    for i in range(n-1):
        x,y,t = invr()
        if x not in neighbours_dict.keys():
            neighbours_dict[x] = []
        
        if y not in neighbours_dict.keys():
            neighbours_dict[y] = []
        
        neighbours_dict[x].append(y)
        neighbours_dict[y].append(x)

        if t == 2:
            white_nodes.add(x)
            white_nodes.add(y)
    

    subtree_problem_road_count = [0]*(n+1) 
    visited = [0]*(n+1)
    #print(neighbours_dict)

    do_dfs(1)
    #print(subtree_problem_road_count)
    requires_nodes = [i for i in range(len(subtree_problem_road_count)) if subtree_problem_road_count[i] == 1]
    print(len(requires_nodes))
    outputStr = ''
    for n in requires_nodes:
        outputStr += str(n) + ' '
    
    outputStr = outputStr.strip()
    print(outputStr)
    return

def Valera_and_Elections2():
    from collections import deque 

    def do_bfs(startNode):
        queue_list = deque([startNode])
        path.append((startNode,-1))

        while len(queue_list) > 0 :
            node = queue_list.popleft()
            visited[node] = True 

            if node in white_nodes:
                subtree_problem_road_count[node] += 1 
            
            for neighbour in neighbours_dict[node]:
                if not visited[neighbour]:
                    queue_list.append(neighbour)
                    path.append((neighbour,node))


    n = inp()

    neighbours_dict = {}
    white_nodes = set()

    for i in range(n-1):
        x,y,t = invr()
        if x not in neighbours_dict.keys():
            neighbours_dict[x] = []
        
        if y not in neighbours_dict.keys():
            neighbours_dict[y] = []
        
        neighbours_dict[x].append(y)
        neighbours_dict[y].append(x)

        if t == 2:
            white_nodes.add(x)
            white_nodes.add(y)
    

    subtree_problem_road_count = [0]*(n+1) 
    visited = [False]*(n+1)
    path = []
    #print(neighbours_dict)

    do_bfs(1)
    path.reverse()

    for node,parent in path:
        for neighbour in neighbours_dict[node]:
            if neighbour != parent:
                subtree_problem_road_count[node] += subtree_problem_road_count[neighbour]


    #print(subtree_problem_road_count)
    requires_nodes = [i for i in range(len(subtree_problem_road_count)) if subtree_problem_road_count[i] == 1]
    print(len(requires_nodes))
    outputStr = ''
    for n in requires_nodes:
        outputStr += str(n) + ' '
    
    outputStr = outputStr.strip()
    print(outputStr)
    return

def Beautiful_Sets_of_Points():
    n, m = invr()

    num_points = min(n,m) + 1 

    outputStr = ''
    if n == min(n,m):

        start_x = n 
        start_y = 0 

        for i in range(num_points):
            outputStr += str(start_x) + ' ' + str(start_y) + '\n'
            start_x -= 1
            start_y += 1 
    
    else:
        start_x = 0 
        start_y = m 

        for i in range(num_points):
            outputStr += str(start_x) + ' ' + str(start_y) + '\n'
            start_x += 1
            start_y -= 1 
    
    outputStr = outputStr.strip()
    print(num_points)
    print(outputStr)
    return 

def A_and_B_and_Interesting_Substrings():
    value_sequence = inlt()
    s = insr()
    n = len(s)
    value_for_s = []
    prefix_sum = []
    running_sum =  0 

    for char in s:
        ascii_code = ord(char)
        pos = ascii_code - ord('a')
        value_for_s.append(value_sequence[pos])
        running_sum += value_sequence[pos]
        prefix_sum.append(running_sum)
    
    num_interesting_substrings = 0

    for ptr1 in range(n-1):
        for ptr2 in range(ptr1+1,n):
            if s[ptr1] == s[ptr2]:
                if ptr2 == ptr1 + 1:
                    num_interesting_substrings += 1
                else:
                    start_index = ptr1 + 1
                    end_index = ptr2 - 1 

                    sum_of_substring = prefix_sum[end_index] - prefix_sum[start_index-1]

                    if sum_of_substring == 0:
                        num_interesting_substrings += 1
    
    print(num_interesting_substrings)
    return

def A_and_B_and_Interesting_Substrings2():
    value_sequence = inlt()
    s = insr()
    n = len(s)

    char_pos_dict = {}
    prefix_sum = []
    running_sum = 0

    for index,char in enumerate(s):
        ascii_code = ord(char) - ord('a')
        running_sum += value_sequence[ascii_code]
        prefix_sum.append(running_sum)
        
        if char not in char_pos_dict.keys():
            char_pos_dict[char] = []
        
        char_pos_dict[char].append(index)
    
    max_prefix_sum = max(prefix_sum)
    
    total_interesting_substrings = 0 

    for ascii_code in range(ord('a'),ord('a') + 26):
        char = chr(ascii_code)

        if char in char_pos_dict.keys() and len(char_pos_dict[char]) > 1:
            pos_list = char_pos_dict[char]

            count_of_prefix_sums_dict = {}

            for index,pos in enumerate(pos_list):
                if index == 0:
                    p_sum = prefix_sum[pos]

                    if p_sum not in count_of_prefix_sums_dict.keys():
                        count_of_prefix_sums_dict[p_sum] = 0
                    count_of_prefix_sums_dict[p_sum] += 1

                else:
                    p_sum = prefix_sum[pos]
                    p_sum_target = prefix_sum[pos-1]
                    
                    if p_sum_target in count_of_prefix_sums_dict.keys():
                        total_interesting_substrings += count_of_prefix_sums_dict[p_sum_target]
                    
                    if p_sum not in count_of_prefix_sums_dict.keys():
                        count_of_prefix_sums_dict[p_sum] = 0 

                    count_of_prefix_sums_dict[p_sum] += 1 

    print(total_interesting_substrings)
    return  

def Present():
    def check_min_ht_possible(min_ht,sequence,m,w):
        n = len(sequence)
        increasing_sum = [-1]*n 
        watering_days_left = m 

        for index,ht in enumerate(sequence):
            
            current_increase = 0 

            if index >= 1:
                current_increase += increasing_sum[index-1]
            if (index - w) >= 0:
                current_increase -= increasing_sum[index-w]
            
            current_ht = ht + current_increase
            #print(ht, current_ht, current_increase)

            if current_ht < min_ht:
                watering_days_nedded = min_ht - current_ht

                if watering_days_nedded <= watering_days_left:

                    if index == 0:
                        increasing_sum[index] = watering_days_nedded 
                    else:
                        increasing_sum[index] = increasing_sum[index-1] + watering_days_nedded
                    
                    watering_days_left -= watering_days_nedded 

                    #print(ht , watering_days_left)
                
                else:
                    return False 
            
            else:
                if index == 0:
                    increasing_sum[index] = 0
                else:
                    increasing_sum[index] = increasing_sum[index-1]
        
        return True 

    n,m,w = invr()
    sequence = inlt()

    check_min_ht_possible(2,sequence,n,w)


    l = 2 
    r = (10**9) + (10**5)

    while l <= r: 
        mid = (l+r)//2

        if check_min_ht_possible(mid,sequence,m,w):
            l = mid + 1 
        else:
            r = mid - 1 
    
    if check_min_ht_possible(mid,sequence,m,w):
        print(mid)
    else:
        print(mid-1)
    
    return
        
def Wonder_Room():
    import math
    n,a,b = invr()

    min_area_reqd = 6*n 

    if min_area_reqd <= (a*b):
        print(a*b)
        print(str(a) + ' ' + str(b))
    
    else:
        max_room_size = int(math.sqrt(min_area_reqd)) + 1

        min_area = -1 
        corresponding_a = -1
        corresponding_b = -1

        if a < b: 
            room1_size_min = a 
            room2_size_min = b 
        else:
            room1_size_min = b 
            room2_size_min = a 

        for room1_size in range(room1_size_min,max_room_size):
            room2_size = math.ceil(min_area_reqd/room1_size)
            current_area = room1_size * room2_size

            if room2_size >= room2_size_min and min_area == -1:
                min_area = current_area

                if a<b:
                    corresponding_a = room1_size
                    corresponding_b = room2_size
                else:
                    corresponding_b = room1_size
                    corresponding_a = room2_size

            elif room2_size >= room2_size_min  and current_area < min_area:
                min_area = current_area

                if a < b:
                    corresponding_a = room1_size
                    corresponding_b = room2_size
                else:
                    corresponding_b = room1_size
                    corresponding_a = room2_size
        
        print(min_area)
        print(str(corresponding_a) + ' ' + str(corresponding_b))
    
    return

def Good_Substrings():
    s = insr()
    n = len(s)
    good_bad_indicator = insr()
    k = inp()

    string_good_bad = []
    prefix_sum = []
    running_sum = 0 

    for char in s:
        index = ord(char) - ord('a')
        value = int(good_bad_indicator[index])
        if value == 1:
            value = 0 
        else:
            value = 1
        string_good_bad.append(value)
        running_sum += value
        prefix_sum.append(running_sum)

    #print(string_good_bad)
    #print(prefix_sum)
    distinct_substrings = set()

    for start_index in range(n):
        for end_index in range(start_index,n):

            if start_index == 0:
                current_sum = prefix_sum[end_index]
            else:
                current_sum = prefix_sum[end_index] - prefix_sum[start_index-1]
    
            if current_sum <= k:
                substring = ''.join(x for x in s[start_index:end_index+1])
                distinct_substrings.add(substring)

    print(len(distinct_substrings))

def Good_Substrings2():
    s = insr()
    entire_string = ''.join(x for x in s)
    n = len(s)
    good_bad_indicator = insr()
    k = inp()

    string_good_bad = []
    prefix_sum = []
    running_sum = 0 

    for char in s:
        index = ord(char) - ord('a')
        value = int(good_bad_indicator[index])
        if value == 1:
            value = 0 
        else:
            value = 1
        string_good_bad.append(value)
        running_sum += value
        prefix_sum.append(running_sum)

    #print(string_good_bad)
    #print(prefix_sum)
    distinct_substrings = set()

    for start_index in range(n):
        for end_index in range(start_index,n):

            if start_index == 0:
                current_sum = prefix_sum[end_index]
            else:
                current_sum = prefix_sum[end_index] - prefix_sum[start_index-1]
    
            if current_sum <= k:
                substring = entire_string[start_index:end_index+1]
                distinct_substrings.add(hash(substring))

    print(len(distinct_substrings))
    return 

def Devu_and_Partitioning_of_the_Array():
    n,k,p = invr()
    num_even_sum = p 
    num_odd_sum = k - p 
    sequence = inlt()

    odd_nums = []
    even_nums = []

    for num in sequence:
        if num % 2 == 0:
            even_nums.append(num)
        else:
            odd_nums.append(num)
    
    if len(odd_nums) < num_odd_sum:
        print("NO")
        return
    
    else:
        extra_odd_numbers = len(odd_nums) - num_odd_sum

        if extra_odd_numbers % 2 != 0: 
            print("NO")
            return

        else:
            if num_even_sum != 0:
                total_distinct_even_nums =  len(even_nums) + (extra_odd_numbers // 2)

                if total_distinct_even_nums < num_even_sum:
                    print("NO")
                    return 
            

            outputStr = 'YES' + '\n'

            if num_even_sum == 0:

                odd_index = 0 
                while odd_index <= (num_odd_sum-2):
                    outputStr += '1' + ' ' + str(odd_nums[odd_index]) + '\n'
                    odd_index += 1
                
                odd_numbers_left = len(odd_nums) - odd_index
                count = odd_numbers_left + len(even_nums)
                outputStr += str(count)
                for oi in range(odd_index,len(odd_nums)):
                    outputStr += ' ' + str(odd_nums[oi])
                
                for en in even_nums:
                    outputStr += ' ' + str(en)
            
            else:

                odd_index = 0

                while odd_index <= (num_odd_sum-1):
                    outputStr += '1' + ' ' + str(odd_nums[odd_index]) + '\n'
                    odd_index += 1 
                
                while odd_index <= len(odd_nums) - 1:
                    if num_even_sum == 1:
                        
                        odd_numbers_left = len(odd_nums) - odd_index
                        count = odd_numbers_left + len(even_nums)
                        outputStr += str(count)

                        for oi in range(odd_index,len(odd_nums)):
                            outputStr += ' ' + str(odd_nums[oi])

                        for en in even_nums:
                            outputStr += ' ' + str(en)
                        
                        odd_index = len(odd_nums)
                        num_even_sum -= 1 

                    else:
                        outputStr += '2' + ' ' + str(odd_nums[odd_index]) + ' ' + str(odd_nums[odd_index+1]) + '\n'
                        num_even_sum -= 1
                        odd_index += 2
                
                if num_even_sum != 0:

                    even_index = 0

                    while even_index <= (num_even_sum-2):
                        outputStr += '1' + ' ' + str(even_nums[even_index]) + '\n'
                        even_index += 1 

                    even_numbers_left = len(even_nums) - even_index
                    outputStr += str(even_numbers_left) 
                    for ei in range(even_index,len(even_nums)):
                        outputStr += ' ' + str(even_nums[ei])
            
            outputStr = outputStr.strip()
            print(outputStr)
    
    return
 
def Bear_and_Prime_Numbers():
    n = inp()
    sequence = inlt()
 
    max_num = max(sequence)
    frequency_list = [0]*(max_num+1)
 
    for num in sequence:
        frequency_list[num] += 1
    
 
    divisor_count = [1]*(max_num+1)
    prefix_sum = [0,0]  #One for zero index, one for one index
    running_sum = 0 
    
    for i in range(2,max_num+1):

        if divisor_count[i] >= 2:
            divisor_count[i] += 1
            prefix_sum.append(running_sum)
            continue
 
        current_num = i 
        current_sum = 0 
        
        while current_num <= max_num:
            divisor_count[current_num] += 1
            current_sum += frequency_list[current_num]
            current_num += i 
        
        running_sum += current_sum 
        prefix_sum.append(running_sum)
        
    m = inp()
 
    print(prefix_sum)
    #print(len(prefix_sum))
 
    outputStr = ''
    for _ in range(m):
        l,r = invr()
 
        if l > max_num and r > max_num:
            outputStr += str(0) + '\n'
            continue
        elif r > max_num:
            r = max_num
 
        outputStr += str(prefix_sum[r] - prefix_sum[l-1]) + '\n'
    
    outputStr = outputStr.strip()
    print(outputStr)
 
    return
 

def Restore_Graph():
    n,k = invr()
    dist_sequence = inlt()

    distance_node_dict = {}
    maximum_distance = -1 

    for index,d in enumerate(dist_sequence):
        nodeId = index + 1 

        if d > maximum_distance:
            maximum_distance = d 

        if d not in distance_node_dict.keys():
            distance_node_dict[d] = []
        
        distance_node_dict[d].append(nodeId)
    
    if 0 not in distance_node_dict.keys() or len(distance_node_dict[0]) != 1:
        print(-1)
        return 
    else:
        outputStr = ''
        num_edges = 0
        

        for d in range(1,maximum_distance+1):
            if d not in distance_node_dict.keys():
                print(-1)
                return 
            
            if d == 1:
                current_nodeId = distance_node_dict[d-1][0]
                nodes = distance_node_dict[d]

                if len(nodes) > k:
                    print(-1)
                    return 
                
                for node in nodes:
                    outputStr += str(current_nodeId) + ' ' + str(node) + '\n'
                    num_edges += 1
            
            else:

                previous_nodes = distance_node_dict[d-1]
                new_nodes = distance_node_dict[d]

                prev_node_index = 0
                new_node_index = 0 

                while prev_node_index <= len(previous_nodes) - 1 and new_node_index <= (len(new_nodes) -1):

                    num_edges_from_prev_node = 0 

                    while new_node_index <= (len(new_nodes)-1) and num_edges_from_prev_node <= (k-2):
                        outputStr += str(previous_nodes[prev_node_index]) + ' ' + str(new_nodes[new_node_index]) + '\n'
                        num_edges += 1
                        new_node_index += 1
                        num_edges_from_prev_node += 1 
                    
                    prev_node_index += 1
                
                if new_node_index != len(new_nodes):
                    print(-1)
                    return 
        
        outputStr = outputStr.strip()
        print(num_edges)
        print(outputStr)
        return

def Multiplication_Table():
    def get_count_how_many_less(n,m,t):

        total_count = 0 
        for row_num in range(1,n+1):
            total_count += min(m,t//row_num)
   
        return total_count


    n,m,k = invr()

    max_num = n*m 

    l = 1 
    r = max_num 

    while l <= r:
        mid = (l+r)//2

        count_how_many_less = get_count_how_many_less(n,m,mid)

        if count_how_many_less < k:
            l = mid + 1
        else:
            r = mid - 1
        
        #print(mid,count_how_many_less,l,r)
    
    count_how_many_less = get_count_how_many_less(n,m,mid)
    if count_how_many_less < k:
        print(mid+1)
    else:
        print(mid)
    
    return

def Anya_and_Ghosts():
    m,t,r = invr()
    sequence = inlt()
    max_ghost_time = sequence[-1]
    minimum_candels_to_light = 0
    candles_lighted_time = set()

    for index,time in enumerate(sequence):

        if index == 0:

            candles_stopping_time = [(time-i+t) for i in range(1,r+1)]
            candles_lighted_time = set(time-i for i in range(1,r+1))

            minimum_candels_to_light += r 

            if min(candles_stopping_time) < time:
                print(-1)
                return
        
        elif time <= min(candles_stopping_time):
            continue

        else:

            candles_stopped = 0
            min_stopping_time = max_ghost_time + 2*t

            for index,st in enumerate(candles_stopping_time):
                if st < time:
                    candles_stopped += 1

                    check = 0

                    while True:
                        proposed_lighting_time = time - candles_stopped - check 

                        if proposed_lighting_time not in candles_lighted_time:

                            candles_lighted_time.add(proposed_lighting_time)
                            candles_stopping_time[index] = proposed_lighting_time + t 
                            minimum_candels_to_light += 1 
                            break 

                        check += 1
            
                if candles_stopping_time[index] < min_stopping_time:
                    min_stopping_time = candles_stopping_time[index]

            if min_stopping_time < time:
                print(-1)
                return

    print(minimum_candels_to_light)
    return
             
def Little_Girl_and_Maximum_XOR():
    #explanation: https://github.com/MathProgrammer/CodeForces/blob/master/Explanations/Explanations%2021/Little%20Girl%20and%20Maximum%20XOR%20Explanation.txt
    def convert_binary_string_to_num(new_binary):
        num_pos = len(new_binary)
        num_value = 0 
        power = 0
        for i in range(num_pos-1,-1,-1):
            num_value += int(new_binary[i])*(2**power)
            power += 1 
        
        return num_value


    l,r = invr()

    binary_l = bin(l).split('b')[1]
    binary_r = bin(r).split('b')[1]

    if binary_l == binary_r:
        print(0)

    elif len(binary_r) != len(binary_l):
        new_binary = ['1']*len(binary_r)
        corresponding_num = convert_binary_string_to_num(new_binary)
        print(corresponding_num)
    
    else: 

        not_matching_index = 0 
        while True:
            if binary_r[not_matching_index] != binary_l[not_matching_index]:
                break 
            else:
                not_matching_index += 1 
        
        # print(not_matching_index)
        # print(binary_r)
        # print(binary_l)

        new_binary = ('0')*(not_matching_index) + ('1')*(len(binary_r)-not_matching_index)
        corresponding_num = convert_binary_string_to_num(new_binary)
        print(corresponding_num)
    
    return 

def Valid_Sets():
    def perform_restricted_dfs(startNode,rootNode,d,mod_val):
        visited[startNode] = True 
        num_subtrees_rooted_at_rootNode[startNode] = 1 

        for neighbour in neighbours_dict[startNode]:
            if not visited[neighbour]:

                if sequence[neighbour] < sequence[rootNode] or sequence[neighbour] > (sequence[rootNode] + d):
                    continue
                elif sequence[neighbour] == sequence[rootNode] and neighbour < rootNode:
                    continue 
                else:
                    perform_restricted_dfs(neighbour,rootNode,d,mod_val)
                    num_subtrees_rooted_at_rootNode[startNode] = (num_subtrees_rooted_at_rootNode[startNode]*(num_subtrees_rooted_at_rootNode[neighbour] + 1)) % mod_val 

    d,n = invr()
    sequence = inlt()
    sequence = [0] + sequence

    neighbours_dict = {}

    for _ in range(n-1):
        u,v = invr()
        if u not in neighbours_dict.keys():
            neighbours_dict[u] = []
        
        if v not in neighbours_dict.keys():
            neighbours_dict[v] = []
        
        neighbours_dict[u].append(v)
        neighbours_dict[v].append(u)
    
    total_subtrees = 0
    mod_val = 1000000007

    for node in range(1,n+1):
        visited = [False] * (n+1)
        num_subtrees_rooted_at_rootNode = [0]*(n+1)
        perform_restricted_dfs(node,node,d,mod_val)
        total_subtrees += num_subtrees_rooted_at_rootNode[node]
    
    print(total_subtrees % mod_val)
    return 


#Valid_Sets()
#Little_Girl_and_Maximum_XOR()
#Anya_and_Ghosts()
#Multiplication_Table()
#Restore_Graph()
Bear_and_Prime_Numbers()
#Devu_and_Partitioning_of_the_Array()
#Good_Substrings2() NO TLE, use hash, built in function in python
#Good_Substrings()  TLE
#Wonder_Room()
#Present()    
#A_and_B_and_Interesting_Substrings2()
#A_and_B_and_Interesting_Substrings()
#Beautiful_Sets_of_Points()
#Valera_and_Elections2()
#Valera_and_Elections()
#Long_Jumps()
#Barcode()
#Friends_and_Presents2()
#Friends_and_Presents()
#Arithmetic_Progression()
#To_Add_or_Not_to_Add()
#Colorful_Graph()
#Vasya_and_Chess()
#Beautiful_Numbers2()
#Beautiful_Numbers()
#Removing_Columns()
#Kolya_and_Tandem_Repeat()
#Misha_and_Forest()
#Checkposts2()
#Checkposts()
#Mr_Kitayuta_the_Treasure_Hunter()
#View_Angle()
#Convex_Shape2()
#Convex_Shape()
#Little_Elephant_and_Problem()
#Divisibility_by_Eight()
#Ladder()
#Pocket_Book()
#Fox_And_Two_Dots()
#Fox_And_Names2()
#Fox_And_Names()
#Booking_System()
#Party()
#Escape_from_Stones()
#Fox_and_Box_Accumulation()
#Contest()
#Caisa_and_Pylons()

#ctrl + k ctrl + j to expand the code fragments
#ctrl + k ctrl + 0 to collapse the code fragments

# t = threading.Thread(target=Valera_and_Elections)
# t.start()
# t.join()