

def twoSum(nums: list[int], target: int) -> list[int]: # -> List[int] describes the return type of the function
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i,j]
    return []
llist = [2,7,11,15]    
ans = twoSum(llist, 9)

print(ans)