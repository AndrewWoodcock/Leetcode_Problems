
def twoSum(nums: list, target: int) -> list:

    # brute force
    # for i in range(len(nums)):
    #     for j in range(i+1, len(nums)):
    #         x_sum = nums[i] + nums[j]
    #         if x_sum == target:
    #             return [i, j]

    complement_map = dict()

    for i in range(len(nums)):
        num = nums[i]
        complement = target - num
        if num in complement_map:
            return [complement_map[num], i]
        else:
            complement_map[complement] = i


print(twoSum([3, 2, 4], 6))
