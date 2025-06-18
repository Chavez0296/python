def arrange_guest_arrival_order(arrival_pattern):
  stack = []
  res = []

  for i in range(len(arrival_pattern)+1):
    stack.append(str(i + 1))
    #print(stack)
    if i == len(arrival_pattern) or arrival_pattern[i] == 'I':
      while stack:
        res.append(stack.pop())
        #print(f"result:{res}")



  return ''.join(res)
    
  pass

print(arrange_guest_arrival_order("IIIDIDDD"))  
print(arrange_guest_arrival_order("DDD"))  

from collections import deque

def reveal_attendee_list_in_order(attendees):
  dq = deque()

  for num in sorted(attendees, reverse=True):
    #print(num)
    if dq:
      dq.appendleft(dq.pop())
      #print(dq)       
    
    dq.appendleft(num)
    #print(dq)
  return list(dq)
  pass

# sorted [17,13,11,7,5,3,2]
# appenedLeft 17
# append 17 after pop
# append left 13
# repeat

print(reveal_attendee_list_in_order([17,13,11,2,3,5,7])) 
print(reveal_attendee_list_in_order([1,1000]))  


def arrange_attendees_by_priority(attendees, priority):
#   smaller = []
#   eq = []
#   larger = []
#   for prio in attendees:
#     if prio < priority:
#       smaller.append(prio)
#     elif prio == priority:
#       eq.append(prio)
#     else:
#       larger.append(prio)
    
#   return smaller + eq + larger
#   Brute Force Solution

#   low, mid, high = 0,0, len(attendees) - 1

#   while mid <= high:
#     if attendees[mid] < priority:
#       attendees[low], attendees[mid] = attendees[mid], attendees[low]
#       low += 1
#       mid += 1
#     elif attendees[mid] > priority:
#       attendees[mid], attendees[high] = attendees[high], attendees[mid]
#       high -= 1 
#     else:
#       mid += 1
  
#   return attendees

# Three pointer solution (O(n) time, O(n) space)
  n = len(attendees)
  l = 0

  for r in range(n):
    if attendees[r] < priority:
      val = attendees[r]
      attendees[l+1 : r+1] = attendees[l : r]
      attendees[l] = val
      l += 1

  for r in range(l,n):
    if attendees[r] == priority:
      val = attendees[r]
      attendees[l+1 : r+1] = attendees[l : r]
      attendees[l] = val
      l += 1

  return attendees
  #time and space complexity (O(n^2))
  pass

print(arrange_attendees_by_priority([9,12,5,10,14,3,10], 10)) 
print(arrange_attendees_by_priority([-3,4,3,2], 2)) 

def rearrange_guests(guests):
  pos = []
  neg = []

  for num in guests:
    if num > 0:
      pos.append(num)
    else:
      neg.append(num)

  filtered_guests = []
  i = 0
  j = 0
  while i < len(pos) or j < len(neg):
    if i < len(pos):
      filtered_guests.append(pos[i])
      i+= 1
    if j < len(neg):
      filtered_guests.append(neg[j])
      j += 1

  return filtered_guests
  pass

print(rearrange_guests([3,1,-2,-5,2,-4]))  
print(rearrange_guests([-1,1])) 

def min_changes_to_make_balanced(schedule):
  stack = []

  for sched in schedule:
    if sched == '(':
      stack.append(sched)
    elif sched == ')' and stack:
      stack.pop()
    else:
      stack.append(sched)
  
  return len(stack)
  pass



print(min_changes_to_make_balanced("())"))
print(min_changes_to_make_balanced("(((")) 