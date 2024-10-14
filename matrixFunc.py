def matrixAdd(A, B, SUM):
    # Get the number of rows and columns
    rows = len(A)
    cols = len(A[0])
    
    # Add the corresponding elements of matrices A and B
    for i in range(rows):
        for j in range(cols):
            SUM[i][j] = A[i][j] + B[i][j]

def matrixAddAsString(A, B, SUM):
    # Get the number of rows and columns
    rows = len(A)
    cols = len(A[0])
    
    # Add the corresponding elements of matrices A and B as strings
    for i in range(rows):
        for j in range(cols):
            SUM[i][j] = str(A[i][j]) + str(B[i][j])

def printMatrix(matrix):
    for row in matrix:
        print(row)

# Example matrices A and B
A = [
    [1, 2, -3],
    [-4, 5, 6],
    [7, 8, -9]
]

B = [
    [0, 1, 2],
    [3, 0, -4],
    [-1, 5, 6]
]

# Initialize SUM matrix to store the result
SUM = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0]
]

# Perform matrix addition
matrixAdd(A, B, SUM)
print("Matrix Addition (numeric):")
printMatrix(SUM)

# Perform matrix addition as string concatenation
matrixAddAsString(A, B, SUM)
print("\nMatrix Addition (as strings):")
printMatrix(SUM)