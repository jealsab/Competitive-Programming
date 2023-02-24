class RecentCounter:

    def __init__(self):
        self.l=0
        self.st=[]
    def ping(self, t: int) -> int:
            self.st.append(t)
            cmp=[t-3000,t]
            if self.st[self.l] >=cmp[0] :
                return len(self.st)- self.l
            while self.st[self.l] < cmp[0]:
                self.l+=1
            return len(self.st)- self.l
                
            
        


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)