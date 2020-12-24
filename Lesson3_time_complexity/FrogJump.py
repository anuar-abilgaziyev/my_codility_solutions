# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, Y, D):
    num_jump = (Y-X)/D
    if num_jump > int(num_jump):
        return int(num_jump)+1
    else:
        return int(num_jump)