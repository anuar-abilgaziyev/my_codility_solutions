def solution(N, A):
    main_freq = 0
    fin_index = 0
    max_indexes = [index for index, value in enumerate(A) if value == N+1]
    #print([i for i in range(len(max_indexes))])
    for i in range(len(max_indexes)):
        if i == 0 or len(max_indexes) == 1:
            fin_index = max_indexes[i]
            slice_A = A[0:fin_index]
        else:
            init_index = max_indexes[i-1]+1 
            fin_index = max_indexes[i]
            slice_A = A[init_index:fin_index]
        if len(slice_A) != 0:
            freq_elem = max(set(slice_A), key = slice_A.count) 
            max_freq = slice_A.count(freq_elem)    
            main_freq += max_freq
    result = [main_freq]*N
    for element in tuple(A[fin_index:]):
        if element <= N:
            result[element-1] += 1
        else:
            keymax = max(result)
            result = [keymax]*N
    return result