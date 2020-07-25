# 呵呵 还没有get
def countSmaller(nums):
        def sort(enum):
            half = int(len(enum) / 2)
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        enum = sort(list(enumerate(nums)))
        print(enum)
        return smaller

nums = [5, 2, 6, 1]
print(countSmaller(nums))