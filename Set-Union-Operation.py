# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
A = set(map(int,input().split()))
n = int(input())
B= set(map(int,input().split()))
res = A.union(B) 
print(len(res))
