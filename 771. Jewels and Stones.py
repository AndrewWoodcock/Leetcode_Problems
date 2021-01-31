
# https://leetcode.com/problems/jewels-and-stones/

def numJewelsInStones(jewels: str, stones: str) -> int:
    jwl_cnt = 0
    for char in stones:
        if char in jewels:
            jwl_cnt += 1
    return jwl_cnt


print(numJewelsInStones("aA", "aAAbbbb"))
