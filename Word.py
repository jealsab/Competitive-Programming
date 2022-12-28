# Enter your code here. Read input from STDIN. Print output to STDOUT
n=int(input())
words=[input() for i in range(n)]
freq={}
for word in words:
    freq[word]=0
for word in words:   
    freq[word]+=1  
print(len(freq))
result=freq.values()
for i in result:
    print(i,end=" ")
