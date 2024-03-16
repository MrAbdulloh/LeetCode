def countSeniors(details: list[str]) -> int:
    count = 0
    for detail in details:
        if int(detail[-4:-2]) > 60:
            count += 1
    return count


# det = ["7868190130M7522", "5303914400F9211", "9273338290F4010"]
det = ["1313579440F2036","2921522980M5644"]
print(countSeniors(det))
