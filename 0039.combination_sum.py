class Solution:
    def backtrack(self, target, candidates, start, combo):
        if target == 0:
            self.res.append(copy.deepcopy(combo))
        if target < 0:
            return
        for i in range(start, len(candidates)):
            combo.append(candidates[i])
            self.backtrack(target - candidates[i], candidates, i, combo)
            combo.pop()

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        self.res = []
        self.backtrack(target, candidates, 0, [])
        return self.res
