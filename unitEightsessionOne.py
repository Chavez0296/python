class TreeNode:
    def __init__(self, value, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right

# def right_vine(root,lst=None):
#   if lst is None:
#     lst = []
#   if root is None:
#     return lst
#   lst.append(root.val)
#   return right_vine(root.right, lst)
  
#   pass

def right_vine(root):
  lst = []
  cur = root
  while cur:
    lst.append(cur.val)
    cur = cur.right
  return lst
  

ivy1 = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))
ivy2 = TreeNode("Root", TreeNode("Node1", TreeNode("Leaf1")))

print(right_vine(ivy1))
print(right_vine(ivy2))



# def survey_tree(root):
#   lst = []
#   def postOrd(root):
#      if not root:
#         return
#      postOrd(root.left)
#      postOrd(root.right)
#      lst.append(root.val)
#   postOrd(root)
#   return lst

def survey_tree(root):
  if not root:
    return []
  res = []
  stack = []
  curr = root
  lastvisit = None

  while stack or curr:
    if curr:
      stack.append(curr)
      curr = curr.left
    else:
      peek = stack[-1]
      if peek.right and lastvisit != peek.right:
        curr = peek.right
      else:
        res.append(peek.val)
        lastvisit = peek
        stack.pop()
  return res
            
  
magnolia = TreeNode("Root", 
                TreeNode("Node1", TreeNode("Leaf1")),
                        TreeNode("Node2", TreeNode("Leaf2"), TreeNode("Leaf3")))

print(survey_tree(magnolia))


# def sum_inventory(inventory):
#     sum = 0
#     def trav(inventory):
#         nonlocal sum
#         if not inventory:
#             return
#         trav(inventory.left)
#         trav(inventory.right)
#         sum += inventory.val
#     trav(inventory)
#     return sum
#     pass

def sum_inventory(root):
    total = 0
    # start with root on the stack (if it exists)
    stack = [root] if root else []
    
    # process until we’ve visited every node
    while stack:
        node = stack.pop()
        total += node.val

        # push children onto the stack
        # order doesn’t matter for summing, but if you
        # wanted pre-/in-/post-order you’d adjust pushes
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return total


inventory = TreeNode(40, 
                    TreeNode(5, TreeNode(20)),
                            TreeNode(10, TreeNode(1), TreeNode(30)))

print(sum_inventory(inventory))

def calculate_yield(root):
  if root is None:
    return 0

  if root.left is None and root.right is None:
    return root.val

  left_val  = calculate_yield(root.left)
  right_val = calculate_yield(root.right)
  
  if root.val == "+":
    return left_val + right_val
  elif root.val == "-":
    return left_val - right_val
  elif root.val == "*":
    return left_val * right_val
  elif root.val == "/":
    return left_val / right_val
  
  return 0
  pass

root = TreeNode("+")
root.left = TreeNode("-")
root.right = TreeNode("*")
root.left.left = TreeNode(4)
root.left.right = TreeNode(2)
root.right.left = TreeNode(10)
root.right.right = TreeNode(2)

print(calculate_yield(root))

def get_most_specific(taxonomy):
  
  if taxonomy is None:
    return []

  if taxonomy.left is None and taxonomy.right is None:
    return [taxonomy.val]

  left = get_most_specific(taxonomy.left)
  right = get_most_specific(taxonomy.right)

  return left + right
  pass

plant_taxonomy = TreeNode("Plantae", 
                          TreeNode("Non-flowering", TreeNode("Mosses"), TreeNode("Ferns")),
                                  TreeNode("Flowering", TreeNode("Gymnosperms"), 
                                          TreeNode("Angiosperms", TreeNode("Monocots"), TreeNode("Dicots"))))

print(get_most_specific(plant_taxonomy))

def count_old_growth(root, threshold):
  count = 0
  def dfs(root):
    nonlocal count
    if not root:
      return 
    dfs(root.left)
    dfs(root.right)
    if root.val > threshold:
      count += 1
  dfs(root)
  return count 
  pass 

forest = TreeNode(100, 
                  TreeNode(1200, TreeNode(20)),
                          TreeNode(1500, TreeNode(700), TreeNode(2600)))


def is_identical(root1, root2):
  if root1 is None and root2 is None:
    return True
  
  if root1 is None or root2 is None:
    return False
  
  if root1.val != root2.val:
    return False
  
  return (is_identical(root1.left, root2.left) and is_identical(root1.right, root2.right))  

  pass 

print(count_old_growth(forest, 1000))

"""
      1                1
     / \\              / \\
    2   3            2   3  
"""
root1 = TreeNode(1, TreeNode(2), TreeNode(3))
root2 = TreeNode(1, TreeNode(2), TreeNode(3))

"""
      1                1
     /                  \\
    2                    2  
"""

root3 = TreeNode(1, TreeNode(2))
root4 = TreeNode(1, None, TreeNode(2))

print(is_identical(root1, root2))
print(is_identical(root3, root4))