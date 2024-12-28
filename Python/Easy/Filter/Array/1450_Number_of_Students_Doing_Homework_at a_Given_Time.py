def busyStudent(startTime: list[int], endTime: list[int], queryTime: int) -> int:
    # count = 0
    # for s in startTime:
    #     for e in endTime:
    #         if e - s == queryTime:
    #             count += 1
    # return count
    count = 0
    for start, end in zip(startTime, endTime):
        if start <= queryTime <= end:
            count += 1
    return count


startTime = [1, 2, 3]
endTime = [3, 2, 7]
queryTime = 4
print(busyStudent(startTime, endTime, queryTime))
