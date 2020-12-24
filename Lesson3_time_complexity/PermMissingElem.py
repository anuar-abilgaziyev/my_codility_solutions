# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    if A == []:
        return 1
    
    A.sort()
    size = len(A)
    if A[0] != 1:
        return 1
    elif A[size-1] != size+1:
        return size+1
    
    for i in range(size-1):
        if A[i+1]-A[i]==2:
            return A[i]+1