# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = map(int,input().split()) 
array = list(map(int,input().split()))
a=set(list(map(int,input().split())))
b=set(list(map(int,input().split())))
happiness=0
i=0

while i < n:
    if array[i] in a:
        happiness+=1
    elif array[i] in b:
        happiness-=1
    i+=1
print(happiness)
