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

def find_max(head):
    curr = head
    max_val = 0
    while curr:
        if curr.value > max_val:
            max_val = curr.value
        curr = curr.next
    return max_val
    pass

def remove_tail(head):
    if head is None:
        return None
    if head.next is None:
        return None 
        
    current = head
    while current.next.next: 
        current = current.next

    current.next = None 
    return head

def delete_dupes(head):
    #two pointers 


    prev_l = Node(0)
    left = head
    right = head.next

    while right:
        if left.value != right.value:
            prev_l = left
            left = left.next
            right = right.next
            continue
        while right != None and left.value == right.value:
            right = right.next
        
        left = prev_l
        prev_l.next = right   
        right = right.next

    return head
    pass


def has_cycle(head):
    slow = head
    fast = head

    while fast.next and fast.next.next:
        if slow == fast:
            return True
        slow = slow.next
        fast = fast.next.next
    return False
    pass



head1 = Node(5, Node(6, Node(7, Node(8))))

# Linked List: 5 -> 6 -> 7 -> 8
print(find_max(head1))

head2 = Node(5, Node(8, Node(6, Node(7))))

# Linked List: 5 -> 8 -> 6 -> 7
print(find_max(head2))

head = Node("Isabelle", Node("Alfonso", Node("Cyd")))

# Linked List: Isabelle -> Alfonso -> Cyd
print_linked_list(remove_tail(head))

head = Node(1, Node(2, Node(3, Node(3, Node(4, Node(5))))))

# Linked List: 1 -> 2 -> 3 -> 3 -> 4 -> 5
print_linked_list(delete_dupes(head))

peach = Node("Peach", Node("Luigi", Node("Mario", Node("Toad"))))

# Toad.next = Luigi
peach.next.next.next = peach.next

print(has_cycle(peach))