
def smallerNumbersThanCurrent(nums: list) -> list:
    return [(sum(i < x for i in nums)) for x in nums]


print(smallerNumbersThanCurrent([6, 5, 4, 8]))
