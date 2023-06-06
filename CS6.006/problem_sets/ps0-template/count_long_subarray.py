def count_long_subarray(A):
    '''
    Input:  A     | Python Tuple of positive integers
    Output: count | number of longest increasing subarrays of A
    '''
    count = 0
    current_length = None
    longest_sub_length = find_longest_subarray(A)
    for idx, elem in enumerate(A):
        if idx > 0 and elem > A[idx - 1]:
            current_length += 1
            if idx == len(A) - 1 and current_length == longest_sub_length:
                count += 1
        else:
            if current_length == longest_sub_length:
                count += 1
            current_length = 1
    return count

def find_longest_subarray(A):
    longest_length = 0
    current_length = 0
    for idx, elem in enumerate(A):
        if idx > 0 and elem > A[idx - 1]:
            current_length += 1
        else:
            current_length = 1
        if current_length > longest_length:
            longest_length = current_length
    return longest_length
