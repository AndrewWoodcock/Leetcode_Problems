
def runningSum(nums: list) -> list:
    running = 0
    sum_arr = []
    for element in nums:
        running += element
        sum_arr.append(running)

    return sum_arr


print(runningSum([3, 1, 2, 10, 1]))
