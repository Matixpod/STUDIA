def selection_sort(A):
    N = len(A)
    count = 0
    for i in range(N):
        min_index = i
        count += 1

        for j in range(i+1, N):
            if A[j] < A[min_index]:
                min_index = j
        if i != min_index:
            A[i], A[min_index] = A[min_index], A[i]
   
    return A,i


selection_sort([6,5,4,3,2,1])
