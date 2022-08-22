class Solution:
    
    # Sorting
    # best t: O(N), worst t: O(n^2),  s: O(1)
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # lets formulize the desired index
        k = len(nums) - k
        
        def quick_select_algorithm(l, r):
            
            pivot, p = nums[r], l
            
            for i in range(l, r):
                if nums[i] <= pivot:
                    nums[p], nums[i] = nums[i], nums[p]
                    p += 1
            # Take the pivot into its correct index
            nums[p], nums[r] = nums[r], nums[p]
            
            if p > k: return quick_select_algorithm(l, p-1)
            elif p < k: return quick_select_algorithm(p+1, r)
            else:   return nums[p]
        
        return quick_select_algorithm(0, len(nums)-1)
            
                    
    # Sorting
    # t: O(NlogN), s: O(N)
    def findKthLargest_easy(self, nums: List[int], k: int) -> int:
        nums.sort()
        return nums[len(nums) - k]
    
    
    # Heap Algorithm
    # t: O(N) + O(NlogK), s: O(N)
        