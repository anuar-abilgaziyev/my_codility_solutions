'''
The functions checks if the array A is permutation.
A permutation is a sequence containing each element from 1 to N once, and only once.
'''


def solution(A):
    dictionary = {}
    size = len(A)
    if size != max(A):
        return 0
    for i in range(size):
        dictionary[A[i]] = 1
        if len(dictionary) == size:
            return 1
    return 0