class DataStructureCourse:
    def merge_two_sorted_arrays(self, array1, array2):
        return "will be implemented"
    # [[], [], [], [].....[]] m arrays with n elements -> merge them into one big array.
    def mergeArrays(self, A, num):
        if num == 1:
            return A[0] #first array
        else:
            merged1 = self.mergeArrays(A[ : num/2], num/2)
            merged2 = self.mergeArrays(A[num/2 : ], num/2)
            return self.merge_two_sorted_arrays(merged1, merged2)
    
    # A: array of integers
    # left, right: int pointers 
    # Algorithm is O(nlogn)
    def minSumSubarray(self, A, left, right):
        if left == right:
            return A[left]
        
        mid = left + (right - left // 2)
        l = self.minSumSubarray(A, left, mid)
        r = self.minSumSubarray(A, mid+1, right)
        c = self.crossing_sum(A, left, mid, right)

        return min(l, r, c)

    
    def crossing_sum(self, A, left, mid, right):
        i = mid - 1
        left_sum = A[mid]
        left_sum_temp = A[mid]

        while(left <= i):
            if left_sum_temp + A[i] < left_sum:
                left_sum = left_sum_temp + A[i]
            left_sum_temp += A[i]
            i -= 1
        
        j = mid + 2
        right_sum = A[mid + 1]
        right_sum_temp = A[mid+1]

        while right <= j:
            if right_sum_temp + A[j] < right_sum:
                right_sum = right_sum_temp + A[j]
            
            right_sum_temp += A[j]
            j += 1 
        
        return left_sum + right_sum



