class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        def backtrack(combination, start, target):
            if target == 0:
                result.append(combination[:])
                return
            if target < 0:
                return

            for i in range(start, len(candidates)):
                combination.append(candidates[i])
                backtrack(combination, i, target - candidates[i])
                combination.pop()

        backtrack([], 0, target)
        return result
