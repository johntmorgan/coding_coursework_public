# Could use some refactoring, but going to move on
def count_anagram_substrings(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    A = []
    k = len(S[0])
    H = {}
    freq_table = [0] * 26
    for start in range(len(T)):
        if start == 0:
            for char in range(start, start + k):
                if start + k < len(T):
                    int_val = ord(T[char]) - ord('a')
                    freq_table[int_val] += 1
        elif start + k < len(T):
            lost_letter = T[start - 1]
            int_lost = ord(lost_letter) - ord('a')
            freq_table[int_lost] -= 1
            new_letter = T[start + k - 1]
            int_new = ord(new_letter) - ord('a')
            freq_table[int_new] += 1
        if start + k < len(T):
            tuple_freq = tuple(freq_table)
            if tuple_freq in H:
                H[tuple_freq] += 1
            else:
                H[tuple_freq] = 1
    for substr in S:
        freq_table = [0] * 26
        for char in substr:
            int_val = ord(char) - ord('a')
            freq_table[int_val] += 1
        tuple_freq = tuple(freq_table)
        if tuple_freq in H:
            A += [H[tuple_freq]]
        else:
            A += [0]
    return tuple(A)

T = "esleastealaslatet"
S = ("eslea", "tesla", "tasla")
print(count_anagram_substrings(T, S))

# Suboptimal - uses O(nk) time to build H, not O(|T|)
def count_anagram_substrings_slow(T, S):
    '''
    Input:  T | String
            S | Tuple of strings S_i of equal length k < |T|
    Output: A | Tuple of integers a_i:
              | the anagram substring count of S_i in T
    '''
    A = []
    k = len(S[0])
    H = {}
    for start in range(len(T)):
        freq_table = [0] * 26
        for char in range(start, start + k):
            if start + k < len(T):
                int_val = ord(T[char]) - ord('a')
                freq_table[int_val] += 1
        tuple_freq = tuple(freq_table)
        if tuple_freq in H:
            H[tuple_freq] += 1
        else:
            H[tuple_freq] = 1
    for substr in S:
        freq_table = [0] * 26
        for char in substr:
            int_val = ord(char) - ord('a')
            freq_table[int_val] += 1
        tuple_freq = tuple(freq_table)
        if tuple_freq in H:
            A += [H[tuple_freq]]
        else:
            A += [0]
    return tuple(A)