from queue import Queue
from collections import deque
sep = "-=-=-=--=-=-=--=-=-=-=--=-=-=-=-=-=-=-=-=-=-=-=-=--=-=-=-=-=-=-=-=-"
def blueprint_approval(blueprints):
    dq = deque()

    for blue in sorted(blueprints):
        dq.append(blue)
    res = []
    while dq:
        res.append(dq.popleft())

    return res     

    pass


print(blueprint_approval([3, 5, 2, 1, 4])) 
print(blueprint_approval([7, 4, 6, 2, 5])) 
print(sep)
def build_skyscrapers(floors):

    res = []
    count = 0
    for floor in floors:
        if not res:
            res.append(floor)
            count+=1

        elif res[-1] >= floor:
            #print(res[-1])
            res.append(floor)
            #print(res)
        
        elif res[-1] < floor:
            while res and res[-1] < floor:
                res.pop()
            res.append(floor)
            count +=1
    
    return count
    pass


print(build_skyscrapers([10, 5, 8, 3, 7, 2, 9])) 
print(build_skyscrapers([7, 3, 7, 3, 5, 1, 6]))  
print(build_skyscrapers([8, 6, 4, 7, 5, 3, 2])) 
print(sep)

def max_corridor_area(segments):
    dq = deque(enumerate(segments))
    maxArea = 0

    while len(dq) > 1:
        w_left, h_left = dq[0]
        w_right, h_right = dq[-1]
        
        width = w_right - w_left
        height = min(h_left,h_right)
        maxArea = max(maxArea, width * height)
        
        if h_left < h_right:
            dq.popleft()
        else:
            dq.pop()
    
    return maxArea

    pass


print(max_corridor_area([1, 8, 6, 2, 5, 4, 8, 3, 7])) 
print(max_corridor_area([1, 1])) 
print(sep)
def min_swaps(s):
    
    count = 0
    steps = 0
    for par in s:
        if par == '[':
            count +=1
        else:
            count -=1
        
        if count < 0:
            steps = max(steps, -count)
    
    return (steps + 1) // 2
    pass

print(min_swaps("][][")) 
print(min_swaps("]]][[[")) 
print(min_swaps("[]"))  
print(sep)