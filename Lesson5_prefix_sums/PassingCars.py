def solution(A):
    ones_count = A.count(1)
    result = 0
    for i in range(len(A)):
        if A[i] == 0:
            result += ones_count
        else:
            ones_count -= 1
        if result > 1000000000:
            return -1
    return result