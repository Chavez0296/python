from collections import deque 

# Tree Node class
class TreeNode:
  def __init__(self, value, key=None, left=None, right=None):
      self.key = key
      self.val = value
      self.left = left
      self.right = right

def build_tree(values):
  if not values:
      return None

  def get_key_value(item):
      if isinstance(item, tuple):
          return item[0], item[1]
      else:
          return None, item

  key, value = get_key_value(values[0])
  root = TreeNode(value, key)
  queue = deque([root])
  index = 1

  while queue:
      node = queue.popleft()
      if index < len(values) and values[index] is not None:
          left_key, left_value = get_key_value(values[index])
          node.left = TreeNode(left_value, left_key)
          queue.append(node.left)
      index += 1
      if index < len(values) and values[index] is not None:
          right_key, right_value = get_key_value(values[index])
          node.right = TreeNode(right_value, right_key)
          queue.append(node.right)
      index += 1

  return root

def sort_plants(collection):
    lst = []
    def inOrder(node):
        if node is None:
            return []
        inOrder(node.left)
        lst.append((node.key,node.val))
        inOrder(node.right)
        return lst
    return inOrder(collection)
    pass

"""
         (3, "Monstera")
        /               \\
   (1, "Pothos")     (5, "Witchcraft Orchid")
        \\                 /
  (2, "Spider Plant")   (4, "Hoya Motoskei")
"""

# Using build_tree() function at the top of page
values = [(3, "Monstera"), (1, "Pothos"), (5, "Witchcraft Orchid"), None, (2, "Spider Plant"), (4, "Hoya Motoskei")]
collection = build_tree(values)

print(sort_plants(collection))

def find_flower(inventory, name):
    
    def trav(node):
        
        if node is None:
            return False
        if node.val == name:
            return True
        
        return trav(node.left) or trav(node.right)
        
    return trav(inventory)
    pass

values = ["Rose", "Lily", "Tulip", "Daisy", "Lilac", None, "Violet"]
garden = build_tree(values)

print(find_flower(garden, "Lilac"))  
print(find_flower(garden, "Sunflower")) 

def print_tree(root):
    if not root:
        return "Empty"
    result = []
    queue = deque([root])
    while queue:
        node = queue.popleft()
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    while result and result[-1] is None:
        result.pop()
    print(result)

def add_plant(collection, name):
    
    def insert(node, name):
        if node is None:
            return TreeNode(name)
        
        if name < node.val:
            node.left = add_plant(node.left,name)

        else:
            node.right = add_plant(node.right,name)

        return node
    
    return insert(collection,name)
    pass

"""
            Money Tree
        /              \\
Fiddle Leaf Fig    Snake Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Fiddle Leaf Fig", "Snake Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(add_plant(collection, "Aloe"))

def remove_plant(collection, name):
    if collection is None:
        return None
    if name < collection.val:
        collection.left = remove_plant(collection.left,name)

    elif name > collection.val:
        collection.right = remove_plant(collection.right,name)

    else: 
        if collection.left is None and collection.right is None:
            return None
        if collection.left is None:
            return collection.right
        if collection.right is None:
            return collection.left
        
        predecessor = collection.left
        while predecessor.right:
            predecessor = predecessor.right
        collection.val = predecessor.val

        collection.left = remove_plant(collection.left, predecessor.val)

    return collection
    pass


"""
              Money Tree
             /         \\
           Hoya        Pilea
              \\        /   \\
             Ivy    Orchid  ZZ Plant
"""

# Using build_tree() function at the top of page
values = ["Money Tree", "Hoya", "Pilea", None, "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of page
print_tree(remove_plant(collection, "Pilea"))
from collections import defaultdict
def find_most_common(root):
    
    if root is None:
        return []

    freq = defaultdict(int)

    def dfs(node):
        if node is None:
            return
        freq[node.val] += 1
        dfs(node.left)
        dfs(node.right)
    
    dfs(root)

    maxCount = max(freq.values())

    return [name for name, count in freq.items() if count == maxCount]
    pass


"""
    Hoya
      \\ 
      Pothos
      /
    Pothos
"""

# Using build_tree() function at top of page
values = ["Hoya", None, "Pothos", "Pothos"]
collection1 = build_tree(values)

"""
      Hoya
    /      \\ 
  Aloe    Pothos
  /        /
 Aloe   Pothos
"""
values = ["Hoya", "Aloe", "Pothos", "Aloe", None, "Pothos"]
collection2 = build_tree(values)

print(find_most_common(collection1))
print(find_most_common(collection2))


def split_collection(collection, target):
    
    if collection is None:
        return (None,None)
    
    if collection.val <= target:
        
        leftSub, rightSub = split_collection(collection.right, target)
        
        collection.right = leftSub
        return (collection, rightSub)
    else:
        
        leftSub, rightSub = split_collection(collection.left, target)

        collection.left = rightSub
        return (leftSub, collection)
    pass

"""
              Money Tree
             /         \\
           Hoya        Pilea
           /  \\        /   \\
        Aloe   Ivy    Orchid  ZZ Plant
"""

# Using build_tree() function at the top of the page
values = ["Money Tree", "Hoya", "Pilea", "Aloe", "Ivy", "Orchid", "ZZ Plant"]
collection = build_tree(values)

# Using print_tree() function at the top of the page
left, right = split_collection(collection, "Hoya")
print_tree(left)
print_tree(right)

def prune(root: TreeNode, target) -> TreeNode:
    """
    Remove all leaves with val == target.  After pruning children,
    if this node becomes a leaf with val == target, remove it too.
    """
    if root is None:
        return None

    # First prune subtrees
    root.left  = prune(root.left,  target)
    root.right = prune(root.right, target)

    # Then decide whether to keep this node
    # If it’s now a leaf AND matches target, drop it
    if root.left is None and root.right is None and root.val == target:
        return None

    return root

values = ["Healthy", "Dying", "Healthy", "Dying", None, "Dying", "New Growth"]
pothos1 = build_tree(values)

# Using print_tree() function at the top of the page
print_tree(prune(pothos1, "Dying"))


values = ["Healthy", "Aphids", "Aphids", "Aphids", "New Growth"]
pothos2 = build_tree(values)

print_tree(prune(pothos2, "Aphids"))