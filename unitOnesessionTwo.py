# Problem 1: Transpose Matrix
# Write a function transpose() that accepts a 2D integer array matrix and returns the transpose of matrix. 
# The transpose of a matrix is the matrix flipped over its main diagonal, swapping the rows and columns.

def transpose(matrix):
    row = len(matrix)
    col = len(matrix[0])
    newMatrix = [[0 for _ in range(row)] for _ in range(col)]

    res = []

    for i in range(row):

        for j in range(col):
            
            if j == i:
                newMatrix[i][j] = matrix[i][j]
            else:
                newMatrix[j][i] = matrix[i][j]
    
    res.append(newMatrix)

    print(res)
    return

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transpose(matrix)

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]
transpose(matrix)

def reverse_list(lst):
    head = 0
    tail = len(lst)-1

    temp = ""

    while head < tail:
        
        temp = lst[tail]
        lst[tail] = lst[head]
        lst[head] = temp
        head += 1
        tail -= 1
    
    print(lst)
    return

 
lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore"]
reverse_list(lst)

lst = ["pooh", "christopher robin", "piglet", "roo", "eeyore", "tiger"]
reverse_list(lst)

def remove_dupes(items):
    
    left = 1

    for r in range(1, len(items)):
        if items[r] != items[r - 1]:
            items[left] = items[r]
            left += 1
        
    del items[left : ]
    
    print(items)
    return

items = ["extract of malt", "haycorns", "honey", "thistle", "thistle"]
remove_dupes(items)

items = ["extract of malt", "extract of malt", "haycorns", "honey", "thistle"]
remove_dupes(items)

def sort_by_parity(nums):
    left, right = 0, len(nums) - 1

    while left < right:
        # Move left forward until we find an odd number
        while left < right and nums[left] % 2 == 0:
            left += 1

        # Move right backward until we find an even number
        while left < right and nums[right] % 2 != 0:
            right -= 1

        # Now nums[left] is odd and nums[right] is even (if left < right), so swap them
        if left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    return nums

    
nums = [3,1,2,4]
print(sort_by_parity(nums))