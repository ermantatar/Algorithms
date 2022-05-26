from ast import List
import turtle


class Solution:
    # Floyd's Tortoise and Hare (Cycle Detection)
    # Find the intersection point of the two runners.
    # t: O(N)
    # s: O(1)
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        
        # First meet will be in the cycle's loop
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break 
        
        # Second meet will be the entrance of the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return fast 
    
    


    ''' Below Solutions but can't pass question strict time constraints '''
    ''' You must solve the problem without modifying the array nums and uses only constant extra space.'''

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

    # Negative signing to seen indexes. 
    # t: O(n)
    # s: O(1)
    def findDuplicate3(self, nums: List[int]) -> int:

        for num in nums:
            cur = abs(num)
            if nums[cur] < 0:
                duplicate = cur
                break
            nums[cur] = -1 * nums[cur]

        # restore the numbers
        for i in range(len(nums)):
            nums[i] = abs(nums[i])

        return duplicate

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
















