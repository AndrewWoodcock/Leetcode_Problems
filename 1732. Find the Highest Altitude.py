
def largestAltitude(gain: list) -> int:
    highest, current = 0, 0
    for altitude in gain:
        current += altitude
        if current > highest:
            highest = current
    return highest


print(largestAltitude([-5, 1, 5, 0, -7]))
