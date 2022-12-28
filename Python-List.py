if __name__ == '__main__':
    list=[]
    N = int(input()) 
    for i in range(N):
        instruction=input().split()
        if instruction[0]=="print":
            print(list)
        elif instruction[0]=="append":
            list.append(int(instruction[1]))
        elif instruction[0]=="insert":
            list.insert(int(instruction[1]),int(instruction[2]))
        elif instruction[0]=="pop":
            list.pop()
        elif instruction[0]=="sort":
            list.sort()
        elif instruction[0]=="reverse":
            list.reverse()
        else:
            list.remove(int(instruction[1]))
        