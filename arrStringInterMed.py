def words_with_char(words, x):
	
    res = []
	
    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j] == x and i not in res:
                res.append(i)

    print(res)
    return
	


words = ["batman", "superman"]
x = "a"
words_with_char(words, x)

words = ["black panther", "hulk", "black widow", "thor"]
x = "a"
words_with_char(words, x)

words = ["star-lord", "gamora", "groot", "rocket"]
x = "z"
words_with_char(words, x)

def hulk_smash(n):
    count = 1
    res = []
    
    while count <= n:
        if count % 3 == 0 and count % 5 == 0:
            res.append("HulkSmash")
            count +=1
        elif count % 3 == 0:
            res.append("Hulk")
            count +=1
        elif count % 5 == 0:
            res.append("Smash")
            count += 1
        else:
            res.append(str(count))
            count +=1

    print(res)
    return

    pass

n = 3
hulk_smash(n)

n = 5
hulk_smash(n)

n = 15
hulk_smash(n)

def shuffle(message, indices):
	
    res = ""
    for i in range(len(message)):
        res += message[indices[i]]

    print(res)
    pass


message = "evil"
indices = [3, 1, 2, 0]
shuffle(message, indices)

message = "findme"
indices = [0, 1, 2, 3, 4, 5]
shuffle(message, indices)

def minimum_boxes(meals, capacity):
    
    total_meals = sum(meals)   

    capacity_sort = sorted(capacity, reverse=True)

    acc = 0

    for i, cap in enumerate(capacity_sort, start=1):
        acc  += cap
        if acc >= total_meals:
            print(i)
            return
    print(-1)
    return
    
    pass


meals = [1, 3, 2]
capacity = [4, 3, 1, 5, 2]
minimum_boxes(meals, capacity)

meals = [5, 5, 5]
capacity = [2, 4, 2, 7]
minimum_boxes(meals, capacity)

def wealthiest_customer(accounts):

    row = len(accounts)

    w = 0
    loc = 0
    wealthiest = []
    for i in range(row):
        if sum(accounts[i]) > w:
            w = sum(accounts[i])
            loc = i
        
    wealthiest.append(loc)
    wealthiest.append(w)
    print(wealthiest)
    return
    pass


accounts = [
	[1, 2, 3],
	[3, 2, 1]
]
wealthiest_customer(accounts)

accounts = [
	[1, 5],
	[7, 3],
	[3, 5]
]
wealthiest_customer(accounts)

accounts = [
	[2, 8, 7],
	[7, 1, 3],
	[1, 9, 5]
]
wealthiest_customer(accounts)

def smaller_than_current(nums):
    res = []
    count = 0
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[j] < nums[i]:
                count +=1
        res.append(count)
        count = 0
    print(res)
    return
    pass

nums = [8, 1, 2, 2, 3]
smaller_than_current(nums)

nums = [6, 5, 4, 8]
smaller_than_current(nums)

nums = [7, 7, 7, 7]
smaller_than_current(nums)

def diagonal_sum(grid):
    n = len(grid)
    total = 0
    
    for i in range(n):
        # primary diagonal: (i, i)
        total += grid[i][i]
        # secondary diagonal: (i, n-1-i), but skip if it's the same cell
        j = n - 1 - i
        if j != i:
            total += grid[i][j]
    
    print(total)
    return
    pass


grid = [
	[1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
diagonal_sum(grid)

grid = [
	[1, 1, 1, 1],
    [1, 1, 1, 1],
	[1, 1, 1, 1],
    [1, 1, 1, 1]
]
diagonal_sum(grid)

grid = [
	[5]
]
diagonal_sum(grid)