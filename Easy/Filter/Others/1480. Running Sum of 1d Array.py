"""Given an array nums. We define a running sum of an array as
 runningSum[i] = sum(nums[0]…nums[i]).

Return the running sum of nums.

"""


def running_sum(nums):
    running_sum = [0] * len(nums)
    current_sum = 0

    for i in range(len(nums)):  # 0,1,2,3
        current_sum += nums[i]  #
        running_sum[i] = current_sum

    return running_sum


print(running_sum([1, 2, 3, 4]))
