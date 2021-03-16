
def createTargetArray(nums: list, index: list) -> list:
    target = []
    for i, j in zip(nums, index):
        target.insert(j, i)

    return target


print(createTargetArray([1, 2, 3, 4, 0], [0, 1, 2, 2, 1]))
