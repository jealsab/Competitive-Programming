# Enter your code here. Read input from STDIN. Print output to STDOUT

from collections import defaultdict
dict = defaultdict(list)
n,m=map(int,input().split())
# print(n)
for i in range(n):
    A=input()
    dict[A].append(str(i+1))
for j in range(m):
    B=input()
    if B in dict:
        print(" ".join(dict[B]))
    else: print (-1)
  
    
    
    
    
