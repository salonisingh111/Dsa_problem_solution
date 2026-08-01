class Solution(object):
    def intersect(self, nums1, nums2):
        result=[]

        for i in range(len(nums1)):
            if nums1[i] in nums2:
                result.append(nums1[i])
                nums2.remove(nums1[i])
        return result