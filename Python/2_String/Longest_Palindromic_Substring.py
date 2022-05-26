class Solution:
	def longestPalindromicSubstring(self, s: 'List[str]')-> int:
		if len(s) <= 1:
			return s
		
		max_len, start, end = 0, 0, 0
	
		for i in range(len(s)):
			odd_max_len = self.expandAroundCenter(s, i, i) 
			even_max_len = self.expandAroundCenter(s, i, i + 1)
			max_len = max(odd_max_len, even_max_len)
			if max_len > end - start:
				start = i - (max_len - 1) // 2
				end = i + ( max_len // 2 )
		
		return s[start: end + 1]


	def expandAroundCenter(self, s: str, L: int, R: int) -> int:
		
		i = 0
		while(0 <= L and R < len(s) and L[i] == R[i]):
			L-=1
			R+=1
		
		return R-L-1
		 

'''

[a][b][c][d][e][f][g][f][e][d][t][y][u]

'''