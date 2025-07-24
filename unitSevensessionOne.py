def count_layers(sandwich, i=0):
    if i >= len(sandwich):
        return 0
    
    item = sandwich[i]

    if isinstance(item,list):
        here = count_layers(item,0)
    else:
        here = 1

    return here + count_layers(sandwich,i+1)
    pass


sandwich1 = ["bread", ["lettuce", ["tomato", ["bread"]]]]
sandwich2 = ["bread", ["cheese", ["ham", ["mustard", ["bread"]]]]]

print(count_layers(sandwich1))
print(count_layers(sandwich2))

def reverse_orders(orders):
    words = orders.split(' ')

    def helperFunc(i):
        if i == len(words):
            return []
        tail = helperFunc(i+1)
        tail.append(words[i])
        return tail
    
    reversed_list = helperFunc(0)

    return ' '.join(reversed_list)
    pass


print(reverse_orders("Bagel Sandwich Coffee"))

def can_split_coffee(coffee, n):

  total = sum(coffee)

  if total % n != 0:
    return False
  
  target = total // n

  coffee.sort(reverse=True)
  if coffee[0] > target:
    return False
  
  checked = [False] * len(coffee)

  def backtrack(remaining, start, curr):
    if remaining == 1:
      return True
      
    if curr == target:
      return backtrack(remaining - 1, 0, 0)
      
    prev = -1

    for i in range(start, len(coffee)):
      hold = coffee[i]

      if not checked[i] and curr + hold <= target and hold != prev:
        checked[i] = True

        if backtrack(remaining, i + 1, curr + hold):
          return True
        
        checked[i] = False
        prev = hold

        if curr == 0:
          break

        if curr + hold == target:
          break

    return False
  
  return backtrack(n,0,0)
  pass

print(can_split_coffee([4, 4, 8], 2))
print(can_split_coffee([5, 10, 15], 4))

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

# For testing
def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> " if current.next else "\n")
        current = current.next

def merge_orders(sandwich_a, sandwich_b):
    if sandwich_a is None:
      return sandwich_b
    if sandwich_b is None:
      return sandwich_a
    
    a_nxt = sandwich_a.next
    b_nxt = sandwich_b.next

    sandwich_a.next = sandwich_b
    sandwich_b.next = merge_orders(a_nxt, b_nxt)

    return sandwich_a
    pass


sandwich_a = Node('Bacon', Node('Lettuce', Node('Tomato')))
sandwich_b = Node('Turkey', Node('Cheese', Node('Mayo')))
sandwich_c = Node('Bread')

print_linked_list(merge_orders(sandwich_a, sandwich_b))
print_linked_list(merge_orders(sandwich_a, sandwich_c))
