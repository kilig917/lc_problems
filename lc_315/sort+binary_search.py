def countSmaller(nums):
    counts = [0] * len(nums)
    arr = []
    for i in range(len(nums))[::-1]:
        counts[i] += binarySearchSmaller(arr, nums[i])
        arr = insert(arr, nums[i])
    return counts
    
def insert(arr, num):
    ind = int(len(arr) / 2)
    if len(arr) == 0:
        arr.append(num)
    elif len(arr) == 1:
        if arr[0] < num:
            arr.append(num)
        else:
            arr.insert(0, num)
    elif arr[ind] == num:
        arr.insert(ind, num)
    elif arr[ind] > num:
        return insert(arr[:ind], num) + arr[ind:]
    else:
        return arr[:ind+1] + insert(arr[ind+1:], num)
    return arr
    
def binarySearchSmaller(arr, num):
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        if arr[0] < num:
            return 1
        else:
            return 0
    ind = int(len(arr) / 2)
    if arr[ind] == num:
        while arr[ind] == num:
            if ind == 0:
                return 0
            ind -= 1
        return ind + 1
    elif arr[ind] > num:
        if ind != 0 and arr[ind-1] < num:
            return ind
        return binarySearchSmaller(arr[:ind], num)
    else:
        if ind != len(arr) - 1 and arr[ind+1] > num:
            return ind + 1
        return binarySearchSmaller(arr[ind+1:], num) + ind + 1 

nums = [5, 2, 6, 1]
print(countSmaller(nums))
    