n = int(input())
 
for i in range(n):
    
    first, second = input().split()
    
    dict = {"S":0, "M":1, "L":2}
    
    if dict[first[-1]] > dict[second[-1]]:
        print(">")
    elif dict[first[-1]] < dict[second[-1]]:
        print("<")
    else:
        if len(first) == len(second):
            print("=")
        elif first[-1] == "S":
            if len(first)> len(second):
                print("<")
            else:
                print(">")
        else:
            if len(first)> len(second):
                print(">")
            else:
                print("<")