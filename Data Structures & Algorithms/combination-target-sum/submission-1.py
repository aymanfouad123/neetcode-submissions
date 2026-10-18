class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        '''
        the dfs recursive logic is,
            # take one
            # explore with it
            # undo the one we added
            # explore without it
        '''
        res = []

        def dfs(i, curr, total):
            if total == target:
                # we found a target combination
                res.append(curr.copy())
                return

            # exceeded target
            if total > target: return

            # exhausted list 
            if i >= len(nums): return

            curr.append(nums[i])
            # i: we can take the same ele in combo again
            # total needs to be added since we want to compare with target
            dfs(i, curr, total+nums[i])
            
            # restore the combination
            curr.pop()

            # check the other case, where we dont take the extra i
            dfs(i+1, curr, total)

        # starting with no numbers chosen, considering the first candidate.
        dfs(0, [], 0)

        return res