
# my solution
def decompressRLElist(nums: list) -> list:
    output = []
    for i in range(0, len(nums), 2):
        pair = nums[i], nums[i+1]
        for x in range(0, pair[0]):
            output.append(pair[1])
    return output


print(decompressRLElist([1, 2, 3, 4]))
print(decompressRLElist([1, 1, 2, 3]))


# Leetcode discussion suggested solution:
def decompressRLElist_2(nums: list) -> list:
    l, a = len(nums), []
    for i in range(0, l, 2):
        a.extend(nums[i] * [nums[i + 1]])
    return a


print(decompressRLElist_2([1, 2, 3, 4]))
print(decompressRLElist_2([1, 1, 2, 3]))
