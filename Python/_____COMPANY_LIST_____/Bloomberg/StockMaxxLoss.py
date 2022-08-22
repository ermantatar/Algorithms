Maximum Draw Down: largest loss over some period of time

t   value  -> Maximum draw down
[0.  100]   0]
[1.  150]   0]
[2   100]   50 
[3.  90.]    60
[4.  100].   60
[5.  89]     61
[59. 89].    61
[60. 89].    61
[61. 89]     61
[62.  1].    99

while: 62, 63
[(100, 0), (150, 1), () ]


"""
[0.  100.]   0]
1.  150    0

"""

"""
# I dont previous data 

"""

# max_price = 150
# max_loss = 50, 60....60, 61 





# return largest loss
def calculateLargetLoss(streamOfData):
    
    if not streamOfData:
        return 0
    
        
    queue = deque()
    
    prev_price = 0
    max_loss = 0
    max_price_so_far = float("-inf")
    
    for t, curr_price in streamOfData):
        
        
        self.queue = []
        
        
def calculate(t, value):        
        
        # remove the stale data
        if queue:
            # pop the stale values 
            while t - queue[0][1] < 60 or curr_price > queue[-1][0]:
                queue.popleft()
            
        queue.append((curr_price, t))
        
        
        # Updated Queue
        # max_price_so_far = max(max_price_so_far, curr_price)
        # remove the highest value which is smaller than current maximum
        if max_price_so_far > queue[0][0]:
            queue.popleft() 
        queue.append((max_price_so_far, t))
        
    
        if curr_price >= queue[0][0]:
            continue
        
        # give me the max price so far! 
        max_price_so_far = queue[0][0]
            
        # There is loss here! 
        today_loss = max_price_so_far - curr_price
        max_loss = max(max_loss, today_loss)
    
        
    return max_loss
    
    curr_price = 110
-> [150, 100, 100, 110, 100]
    
    
    

[1.  150]   0]
[2   100]   0
[3.  100]   0]
[4.  110]   0]
[5.  100]   0]
[6.  10]   100]

    
    
    150-  100 100. 110 100 10
    
    
    
    
    