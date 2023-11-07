class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        sum_of_nums = sum(nums)

        if sum_of_nums % 2 != 0:
            return False

        target = sum_of_nums // 2

        dp = set()
        dp.add(0)

        for i in nums:
            next_dp = set()
            for j in dp:
                if j <= target:
                    next_dp.add(j)
                if i + j <= target:
                    next_dp.add(i + j)

            dp = next_dp

        return target in dp
