array = [0,1,2,3]

def getPerm(array):
    if len(array) == 1:
        return [array]
    perms = []
    for i in range(len(array)):
        permu = getPerm(array[:i] + array[i+1:])
        for j in permu:
            perms.append([array[i], *j])
    return perms
print(array)
print("===============================")
print(getPerm(array))