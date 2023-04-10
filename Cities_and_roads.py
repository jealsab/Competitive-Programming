from collections import defaultdict
n = int(input())
res= 0
graph = defaultdict(list)
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(i+1,len(row)):
        if row[j]==1:
            res+=1
        # graph[i].append((j, row[j]))
        
    
        
print(res)