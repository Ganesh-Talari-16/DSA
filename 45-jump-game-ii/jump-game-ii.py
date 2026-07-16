class Solution:
    def jump(self, nums: List[int]) -> int:
        goal = 0
        jumps = 0
        end = 0

        for i in range(len(nums)-1):
            goal = max(goal,i + nums[i])
            if i == end:
                jumps += 1
                end = goal
        return jumps