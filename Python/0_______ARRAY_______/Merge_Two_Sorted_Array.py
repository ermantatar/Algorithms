# Algorithm
# First of all, save two pointers which point to the end of each array, p1 = m-1, p2 = n- 1. 
# Create a main pointer to fill result, ptr m + n - 1, then compare the p1 ~ p2 relationship and fill the spot for ptr, then -1 reduce two pointers every loop.
# P1, and array1, is fine, since it has enough space and we are iterating over it, even though items left, they will be already located at array 1 itself
# Make sure, if p2 and array2 items are done, if not go over p2 and array2 until p2 is come to 0. 


class Solution:
    # t: O(m + n)
    # s: O(1)
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        
        # point the last index of both list
        p1, p2 = m - 1, n - 1
        # main pointer will point the last index of nums1 array. 
        ptr = n + m - 1
        
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[ptr] = nums1[p1]
                p1 -= 1
            else:
                nums1[ptr] = nums2[p2]
                p2 -=1
            
            ptr -= 1
        
        while p2 >= 0:
            nums1[ptr] = nums2[p2]
            p2 -= 1
            ptr -= 1
    
    # t: O(m + n)
    # s: O(1)
    def merge_2(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # Set p1 and p2 to point to the end of their respective arrays.
        p1 = m - 1
        p2 = n - 1
    
        # And move p backwards through the array, each time writing
        # the smallest value pointed at by p1 or p2.
        for p in range(n + m - 1, -1, -1):
            if p2 < 0:
                break
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1