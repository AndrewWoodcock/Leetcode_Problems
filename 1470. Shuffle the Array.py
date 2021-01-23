

def shuffle(nums: list, n: int) -> list:
    out = []
    for i, j in zip(nums[:n], nums[n:]):
        out.append(i)
        out.append(j)
    return out


print(shuffle([2, 5, 1, 3, 4, 7], 3))
