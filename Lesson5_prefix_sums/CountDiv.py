def solution(A, B, K):
    b = int(B/K)
    if A%K == 0:
        a = int(A/K) - 1
    else:
        a = int(A/K)
    
    return b-a