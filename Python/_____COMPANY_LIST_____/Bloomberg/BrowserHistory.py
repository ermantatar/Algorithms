class Node:
    def __init__(self, url):
        self.url = url 
        self.next = None 
        self.prev = None 

class BrowserHistory:

    def __init__(self, homepage: str):
        self.curr = Node(homepage)
    
    def visit(self, url: str) -> None:

        if not url:
            raise ValueError("Invalid Url!")
        
        # connect new page with class curr page 
        newNode = Node(url)
        newNode.prev = self.curr
        self.curr.next = newNode 

        # move class curr page to the next new page 
        self.curr = self.curr.next 
    
    def back(self, steps: int) -> str:
        while self.curr.prev != None and steps > 0:
            self.curr = self.curr.prev
            steps -= 1
        
        return self.curr.url 
    
    def forward(self, steps: int) -> str:
        while self.curr.next != None and steps > 0:
            self.curr = self.curr.next 
            steps -= 1
        
        return self.curr.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)