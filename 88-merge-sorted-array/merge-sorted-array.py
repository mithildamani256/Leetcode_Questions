class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        nums3 = nums1[:m]
        i = 0
        j = 0
        index = 0

        while i < m or j < n:
            if i == m:
                nums1[index] = nums2[j]
                j += 1
            elif j == n:
                nums1[index] = nums3[i]
                i += 1
            else:
                if nums3[i] > nums2[j]:
                    nums1[index] = nums2[j]
                    j += 1
                else:
                    nums1[index] = nums3[i]
                    i += 1
            
            index += 1
        
