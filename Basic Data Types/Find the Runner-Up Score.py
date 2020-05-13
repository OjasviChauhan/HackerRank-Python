if __name__ == '__main__':
    n = int(input())
    lst=[int(i) for i in input().split()] #List Comprehension
    lst.sort()
    
    for i in range(len(lst)-2,-1,-1):
        if lst[i] != lst[-1]:
            print(lst[i])
            break
        else:
            continue
