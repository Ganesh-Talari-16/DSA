class Solution:
    def nextGreaterElement(self, nums1, nums2):
        # nums1idx = {n:i for i,n in enumerate(nums1)}
        # res = [-1] * len(nums1)

        # for i in range(len(nums2)):
        #     if nums2[i] not in nums1idx:
        #         continue
        #     for j in range(i+1,len(nums2)):
        #         if nums2[j] > nums2[i]:
        #             idx = nums1idx[nums2[i]]
        #             res[idx] = nums2[j]
        #             break
        # return res
        nums1idx = {n:i for i,n in enumerate(nums1)}
        res = [-1] * len(nums1)
        stack = []

        for i in range(len(nums2)):

            while stack and nums2[i] > stack[-1]:
                val = stack.pop()

                if val in nums1idx:
                    idx = nums1idx[val]
                    res[idx] = nums2[i]

            stack.append(nums2[i])

        return res