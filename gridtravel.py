'''Say that you're a traveler on a 2D grid. 
You begin in the top-left corner and you goal is to travel 
to the bottom-right corner. You may only move down or right. 

In how many ways can you travel to the goal on a grid with dimensions M * N?
 _ _ _
|_|_|_|
|_|_|_| M
|_|_|_|
    N
'''

def gridTraveler(m,n, memo={}):
    key = str(m) + ',' + str(n)
    if key in memo:
        return memo[key]
    if(m == 1 and n == 1):
        return 1
    if(m == 0 or n == 0):
        return 0
    memo[key] = gridTraveler(m-1, n, memo) + gridTraveler(m,n-1, memo)
    return memo[key]
#O(2^n+m) time complexity and space complexity is O(m+n)    
print(gridTraveler(1,1))
print(gridTraveler(2,3))
print(gridTraveler(3,2))
print(gridTraveler(3,3))
print(gridTraveler(18,18))