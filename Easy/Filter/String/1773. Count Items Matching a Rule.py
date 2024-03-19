"""
https://leetcode.com/problems/count-items-matching-a-rule/description/
"""


def countMatches(items: list[list[str]], ruleKey: str, ruleValue: str) -> int:
    count = 0
    for item in items:
        if ruleKey == 'type' and item[0] == ruleValue:
            count += 1
        elif ruleKey == 'color' and item[1] == ruleValue:
            count += 1
        elif ruleKey == 'name' and item[2] == ruleValue:
            count += 1
    return count


items = [["phone", "blue", "pixel"], ["computer", "silver", "lenovo"], ["phone", "gold", "iphone"]]
ruleKey = "color"
ruleValue = "silver"
print(countMatches(items, ruleKey, ruleValue))
