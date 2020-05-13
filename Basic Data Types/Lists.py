if __name__ == '__main__':
    N = int(input())
    List = []
    for i in range(N):
        L = input().split(" ")
        #print(L)
        if L[0] == 'insert':
            List.insert(int(L[1]), int(L[2]))
        if L[0] == 'print':
            print(List)
        if L[0] == 'remove':
            List.remove(int(L[1]))
        if L[0] == 'append':
            List.append(int(L[1]))
        if L[0] == 'sort':
            List.sort()
        if L[0] == 'pop':
            List.pop()
        if L[0] == 'reverse':
            List.reverse()
