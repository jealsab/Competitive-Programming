# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
n=int(input())
s=list(map(int,input().split()))
c=Counter(s)
for l ,d in c.items():
    if d==1:
        print(int(l))
    