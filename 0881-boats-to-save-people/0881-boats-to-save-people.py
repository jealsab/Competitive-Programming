class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        
        n,i= 0,0
        j = len(people)-1
        while i <= j:
            if people[i]+people[j]<=limit:
                i+=1
                j-=1
            else:
                j-=1
            n+=1
        return n