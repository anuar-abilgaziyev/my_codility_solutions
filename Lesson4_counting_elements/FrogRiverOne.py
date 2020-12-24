def solution(X, A):
    dictionary = {}
    size = len(A)
    for i in range(size):
        dictionary[A[i]] = 1
        if len(dictionary) == X:
            return i
    return -1

