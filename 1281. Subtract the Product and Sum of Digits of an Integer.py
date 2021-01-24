
def subtractProductAndSum(n: int) -> int:
    n = list(str(n))
    my_sum = sum([int(digit) for digit in n])

    product = 1
    for element in n:
        product = int(element) * product

    return product - my_sum


print(subtractProductAndSum(4421))
