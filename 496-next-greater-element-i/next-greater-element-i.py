class Solution(object):
    def nextGreaterElement(self, nums1, nums2):
        res = []
        for ele in nums1:
            nxtge = -1
            for i in range(len(nums2)):
                
                if ele == nums2[i]: 
                    for j in range(i+1,len(nums2))  :
                        if nums2[j] > ele:
                            nxtge = nums2[j]
                            break
            res.append(nxtge)
        return res