class Solution:
    #ganesh
    def findMaxLength(self, nums: List[int]) -> int:
        seen = {}
        # Array modfification kosam
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        
        prefix_sum = []
        prefix = 0
        res = 0

        for i in range(len(nums)):
            prefix += nums[i]
            prefix_sum.append(prefix)
    
            if prefix == 0:  # balanced from start
                res = max(res, i+1)

            if prefix not in seen:
                seen[prefix] = i
            else:
                res = max(res, i - seen[prefix])
        return res

        