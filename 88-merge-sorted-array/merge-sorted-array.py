class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        lst3 = []

        i = 0
        j = 0

        while i < m and j < n:
            if nums1[i] < nums2[j]:
                lst3.append(nums1[i])
                i += 1
            else:
                lst3.append(nums2[j])
                j += 1
        
        while i < m:
            lst3.append(nums1[i])
            i += 1

        while j < n:
            lst3.append(nums2[j])
            j += 1

        print(lst3)

        for i in range(m+n):
            nums1[i] = lst3[i]

