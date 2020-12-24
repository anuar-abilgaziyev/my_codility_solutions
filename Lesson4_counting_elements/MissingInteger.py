def solution(A):
    set_A = set(A)
    max_int = max(set_A)
    
    if max_int < 0:
        return 1

    for i in range(1, max_int):
        if i not in set_A:
            return i
    return max_int+1