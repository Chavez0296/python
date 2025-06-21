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

def make_balanced_room(s):
    hold = list(s)
    stack = []
   
    for i,strs in enumerate(hold):
        if strs == '(':
            stack.append(i)
        elif strs == ')':
            if stack: 
                stack.pop()
            else:
                hold[i] = ''
        
    for i in stack:
        hold[i] = ''
    
    return ''.join(hold)
        
    pass


print(make_balanced_room("art(t(d)e)sign)")) 
print(make_balanced_room("d)e(s)ign")) 
print(make_balanced_room("))((")) 
print(sep)
def time_to_complete_dream_designs(design_times):
    n = len(design_times)
    res = [0] * n
    stack = []

    for i,t in enumerate(design_times):
        while stack and design_times[stack[-1]] < t:
            prev_i = stack.pop()
            res[prev_i] = i - prev_i

        stack.append(i)

    return res
    pass


print(time_to_complete_dream_designs([3, 4, 5, 2, 1, 6, 7, 3])) 
print(time_to_complete_dream_designs([2, 3, 1, 4]))  
print(time_to_complete_dream_designs([5, 5, 5, 5])) 
print(sep)

def next_greater_dream(dreams):
    n = len(dreams)
    
    res = [-1] * n
    stack = []
    for i in range(2 * n):
        val = dreams[i % n]
        while stack and dreams[stack[-1]] <  val:
            prev_i = stack.pop()
            res[prev_i] = val

        if i < n:
            stack.append(i)

    return res
     
    pass


print(next_greater_dream([1, 2, 1])) 
print(next_greater_dream([1, 2, 3, 4, 3])) 
print(sep)