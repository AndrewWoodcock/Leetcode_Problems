
def reverse(x: int) -> int:
    if x > 0:
        out = int(str(x)[::-1])
    else:
        out = -int(str(abs(x))[::-1])

    if (out <= -2147483647) or (out >= 2147483647):
        return 0
    else:
        return out


print(reverse(1534236469))
print(reverse(-123))
