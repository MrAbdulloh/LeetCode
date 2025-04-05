# https://leetcode.com/problems/sum-of-all-subset-xor-totals/?envType=daily-question&envId=2025-04-05

def subsetXORSum(nums):
    def dfs(i, current_xor):
        if i == len(nums):
            return current_xor

        return dfs(i + 1, current_xor ^ nums[i]) + dfs(i + 1, current_xor)

    return dfs(0, 0)


print(subsetXORSum([1, 3]))
