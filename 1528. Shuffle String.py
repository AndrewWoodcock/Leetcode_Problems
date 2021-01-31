
# my solution - slow
def restoreString(s: str, indices: list) -> str:
    char_inds = []
    for char, ind in zip(s, indices):
        char_inds.append((char, ind))
    char_inds = sorted(char_inds, key=lambda tup: tup[1])

    return "".join([x[0] for x in char_inds])


print(restoreString("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))

# leetcode discussion solution O(n)

def restoreString2(s: str, indices: list) -> str:
    res = [''] * len(s)
    for index, char in enumerate(s):
        res[indices[index]] = char
    return "".join(res)


print(restoreString2("codeleet", [4, 5, 6, 7, 0, 2, 1, 3]))