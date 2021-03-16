
def countMatches(items: list, ruleKey: str, ruleValue: str) -> int:
    pos_dict = {"type": 0,
                "color": 1,
                "name": 2}

    key_no = pos_dict[ruleKey]
    mtch_cnt = 0
    for element in items:
        if element[key_no] == ruleValue:
            mtch_cnt += 1

    return mtch_cnt


print(countMatches([["phone", "blue", "pixel"], ["computer", "silver", "phone"], ["phone", "gold", "iphone"]], "type", "phone"))

