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


def Magnets():
    n = inp()

    number_of_groups = 1
    current_group_size = 0 

    for _ in range(n):
        pos = insr()

        if current_group_size == 0:
            last_pole = pos[1]
            current_group_size += 1
        else:
            if last_pole != pos[0]: 

                last_pole = pos[1]
                current_group_size += 1

            else:
                number_of_groups += 1
                current_group_size = 1 
                last_pole = pos[1] 
    
    print(number_of_groups)

def Mafia():
    import math 

    def check_possible(num_games, sum_games, max_games, n):
        if num_games >= max_games and num_games >= (sum_games/(n-1)):
            return True 
        else:
            return False
        


    n = inp()
    sequence = inlt()
    sum_games = sum(sequence)
    max_games = max(sequence)
    min_games = min(sequence)


    l = min_games
    r = sum_games

    while l <= r:
        mid = (l+r)//2
        
        if check_possible(mid,sum_games,max_games,n):
            r = mid - 1 
        else:
            l = mid + 1 
    
    if check_possible(mid,sum_games,max_games,n):
        print(mid)
    else:
        print(mid+1)
    
    return

def Almost_Arithmetical_Progression():
    


Almost_Arithmetical_Progression()
#Mafia()    
#Magnets()

#ctrl + k ctrl + j to expand the code fragments
#ctrl + k ctrl + 0 to collapse the code fragments

# t = threading.Thread(target=Valera_and_Elections)
# t.start()
# t.join()