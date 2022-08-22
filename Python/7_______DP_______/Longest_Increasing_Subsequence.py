class Solution:
    # t: O(n^2), s: O(N)
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp = [1] * len(nums)
        for i in range(1, len(nums)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[i], dp[j] + 1)

        return max(dp)


    # t: NlogN, s: N
	def lengthOfLIS(self, nums: List[int]) -> int:
		ans = [nums[0]]
		for i in range(1,len(nums)):
			if nums[i] > ans[-1]: ans.append(nums[i])
			else: 
				ans[bisect_left(ans,nums[i])]=nums[i]
		return len(ans)