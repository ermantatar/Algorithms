from ast import List
import turtle

#  Question:
# Given an array of integers nums, containing n + 1 integers  (in range [1, n]), 
# there is one repeated number in nums, return it. 

"""
Negating and Signing to seen indexes. 
t: O(N) and s: O(1)
"""
def findDuplicate_Negate(nums: List[int]) -> int:

    duplicate = 0
    for cur in nums:
        if nums[abs(cur) - 1] < 0:
            duplicate = abs(cur)
            break

        nums[abs(cur)-1] *= -1

    for i in range(len(nums)):
        nums[i] = abs(nums[i])

    return duplicate

"""
Floyd's Tortoise and Hare (Cycle Detection)
Find the intersection point of the two runners.
t: O(N), s: O(1)
"""
def findDuplicate_FloydTortoise(nums: List[int]) -> int:

    slow, fast = nums[0], fast[0]

    # First, start while True, unless they meet with each other. Cycle detection
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Detect the beginning of the cycle! 
    slow = nums[0]
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]
    
    return fast

    """
    Binary Search - Two Pointer
    """
    # t: O(NlogN), s: O(N) 
    def findDuplicate(self, nums: List[int]) -> int:
        # 'low' and 'high' represent the range of values of the target
        low = 1
        high = len(nums) - 1
        
        while low <= high:
            cur = (low + high) // 2
            count = 0

            # Count how many numbers are less than or equal to 'cur'
            count = sum(num <= cur for num in nums)
            if count > cur:
                duplicate = cur
                high = cur - 1
            else:
                low = cur + 1
                
        return duplicate

    


    # Below Solutions but can't pass question strict time constraints '''
    # You must solve the problem without modifying the array nums and uses only constant extra space.'''

    # t: O(NlogN)
    # s: O(logN) (Java) or O(N) (Python, sorting uses timsort algo, and its worst case space O(N))
    def findDuplicate1(self, nums: List[int]) -> int:
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return nums[i]
    
    # HashSet
    # t: O(N)
    # s: O(N)
    def findDuplicate2(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            if num in seen:
                return num
            seen.add(num)

    # Recursive of using Array like a Hashmap 
    # t: O(N)
    # s: O(N) -> N recursive call at the memory stack. 
    def findDuplicate4(self, nums: List[int]) -> int:

        def store(nums: List[int], cur: int) -> int:
            if cur == nums[cur]:
                return cur #duplicate
            nxt = nums[cur]
            nums[cur] = cur
            return store(nums, nxt)

        return store(nums, 0)

    # Array like a hashmap, use the index = number mapping
    # t: O(N)
    # s: O(N)
    def findDuplicate5(self, nums: List[int]) -> int:

        while nums[0] != nums[nums[0]]:
            nums[nums[0]], nums[0] = nums[0], nums[nums[0]]

        return nums[0]


    # Binary Search
    # t: O(NlogN)
    # s: O(1)
    def findDuplicate5(self, nums: List[int]) -> int:
        # 'low' and 'high' represents the range of values of the target.
        low = 1 
        high = len(nums)-1

        while low <= high:
            mid = low + (high-low) // 2
            
            count = 0
            count = sum(num <= mid for num in nums)

            if count > mid:
                duplicate = mid 
                high = mid - 1
            else:
                low = mid + 1

        return duplicate
















