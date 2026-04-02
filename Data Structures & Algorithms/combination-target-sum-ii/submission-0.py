class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        candidates.sort()
        self.backtracking(0, candidates, [], target)

        return self.result
    
    def backtracking(self, idx: int, candidates: List[int], current_candidate: List[int], target: int):
        if (target == 0):
            self.result.append(current_candidate[::])
        if (idx == len(candidates) or candidates[idx] > target):
            return
        
        current_candidate.append(candidates[idx])
        self.backtracking(idx+1, candidates, current_candidate, target-candidates[idx])
        current_candidate.pop()
        while (idx+1 < len(candidates) and candidates[idx] == candidates[idx+1]):
            idx+=1
        self.backtracking(idx+1, candidates, current_candidate, target)
