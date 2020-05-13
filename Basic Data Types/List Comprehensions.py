if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    print([[i,j,k] for i in range(x+1) for j in range(y+1) for k in range(z+1) if (i+j+k)!=n])
    
    
"""
A list comprehension consists of brackets containing an expression followed by a for clause, then zero or more for or if clauses. 
The result will be a new list resulting from evaluating the expression in the context of the for and if clauses which follow it. 
For example, this listcomp combines the elements of two lists if they are not equal:


>>> [(x, y) for x in [1,2,3] for y in [3,1,4] if x != y]
>>> [(1, 3), (1, 4), (2, 3), (2, 1), (2, 4), (3, 1), (3, 4)]
"""
