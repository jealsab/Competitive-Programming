t = int(input())
 
for i in range(t):
    word = input()
    l = len(word)-2
    if l < 9:
        print(word)
    else:
        l = str(l)
        print(word[0]+l+word[-1])
    