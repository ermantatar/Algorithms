def get_k_nodes(booting_power,processing_power,max_power):
	if len(booting_power) != len(processing_power) or len(booting_power) == 0 or len(processing_power) == 0:
		return 0
	if len(booting_power) == 1 and len(processing_power) == 1 and booting_power[0] + processing_power[0] <= max_power:
		return 1
	min_k = 1
	max_k = len(booting_power)
	max_power_k = 0
	for k in range(min_k, max_k+1):
		i = 0
		while i <= max_k-k:
			power_k = (sum(processing_power[i:i+k]) * k) + max(booting_power[i:i+k])
			if power_k <= max_power:
				max_power_k = max(k, max_power_k)
			i += 1
	return max_power_k


def maximumQuality(packets, channels):
    res = 0
    packets.sort()
    print(packets)
    n = len(packets)
    for i in range(n-1, n-channels,-1):
        res += packets[i]
        # print(res)

    window = n - channels + 1
    if window % 2 == 1:
        res += packets[window // 2]
    else:
        res += (packets[window//2] + packets[window//2 - 1])/2
    return res



"""
# [1,2,3,4,5,6]

def calculateTheMedian(array):
    if not array:
        return -1
    
    length = len(array)
    
    median = 0
    if length % 2 == 1:
        median = array[length // 2]
    else:
        median = math.ceil((array[(length // 2) -1] + array[length // 2] )/2)
    
    return median

def maximumQuality(packets, channels):
    res = 0
    packets.sort()
    
    n = len(packets)
    
    for i in range(n-1, n-channels, -1):
        res += packets[i]
    
    window = n - channels + 1
    
    if window % 2 == 1:
        res += packets[window//2]
    else:
        res += (packets[window//2] + packets[window//2-1]) / 2
    
    return math.ceil(res)
"""


from collections import deque 

def maxProcessPower(processingPowers, boostingPowers, powerMax):
    n = len(processingPowers)
    i, j = 0, 0
    
    q = deque([])
    sum = 0
    ans = 0
    while j < n:
        sum += processingPowers[j]
        while not len(q) == 0 and q[0][0] <= boostingPowers[j]:
            q.popleft()

        q.append((boostingPowers[j], j))
        
        while i <= j and q[-1][0] + sum * (j-i+1) > powerMax:
            if q[-1][1] == i:
                q.pop()
            
            sum -= processingPowers[i]
            i += 1
        
        ans = max(ans, j-i+1)
        j += 1
    
    return ans