def numberOfEmployeesWhoMetTarget(hours: list[int], target: int) -> int:
    ans = 0
    for hour in hours:
        if hour >= target:
            ans += 1
    return ans


hours = [5,1,4,2,2]
target = 6
print(numberOfEmployeesWhoMetTarget(hours, target))
