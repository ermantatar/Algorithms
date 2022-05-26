def edit_distance(str1, str2):

	dp = [len(str1) + 1 * 0][len(str2) + 1 * 0]

	for i in range(len(str1)):
		for j in range(len(str2)):

			if i == 0:
				dp[i][j] = j

			if j == 0:
				dp[i][j] = i

			elif str1[i-1] == str2[j-1]:
				dp[i][j] = dp[i-1][j-1]

			else:
				dp[i][j] = 1 + min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1])

	return dp[m][n]

# Run time O(n * m)