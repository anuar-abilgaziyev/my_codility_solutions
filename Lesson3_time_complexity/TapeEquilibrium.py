# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    total_sum = sum(A)
    min_diff = 1000000000
    for i in range(len(A)-1):
        total_sum -= 2*A[i]
        if abs(total_sum) < min_diff:
            min_diff = abs(total_sum)

    return min_diff