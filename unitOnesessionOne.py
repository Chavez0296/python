def welcome():
    print("Welcome to The Hundred Acre Wood!")

welcome()

def greeting(name):
    print(f"Welcome to The Hundred Acre Wood {name}! My name is Christopher Robin.")

greeting("Luis")

def print_catchphrase(character):
    match character:
        case "Pooh":
            return "Oh brother!"
        case "Tigger":
            return "TTFN: Ta=ta for now!"
        case "Eeyore":
            return "Thanks for noticing me."
        case "Christopher Robin":
            return "Silly old bear."
        case default:
            return "Sorry! I don't know Piglet's catchphrase!"
character = "Pooh"
print(print_catchphrase(character))

character = "Piglet"
print(print_catchphrase(character))

def local_maximums(grid):
    n = len(grid)

    if n < 3:
        return []
    
    row_max = [[0]*(n-2) for _ in range(n)]
    for r in range(n):
        for c in range(n-2):
            a,b,d = grid[r][c], grid[r][c+1], grid[r][c+2]
            row_max[r][c] = a if a >= b and a >= d else(b if b >= c else c)

    m = n - 2
    local_maxes = [[0]*m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            x,y,z = row_max[i][j], row_max[i+1][j], row_max[i+2][j]
            local_maxes[i][j] = x if x >= y and x >= z else (y if y >= z else z)

    return local_maxes

grid1 = [
    [9, 9, 8, 1],
    [5, 6, 2, 6],
    [8, 2, 6, 4],
    [6, 2, 2, 2]
]

grid2 = [
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 2, 1, 1],
    [1, 1, 1, 1, 1],
    [1, 1, 1, 1, 1]
]

# Compute and display results:
print(local_maximums(grid1))
print(local_maximums(grid2))