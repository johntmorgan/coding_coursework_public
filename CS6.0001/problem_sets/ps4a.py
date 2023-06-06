# Problem Set 4A
# Name: John "JMo" Morgan
# Collaborators: None
# Time Spent: 0:45

def get_permutations(sequence):
    '''
    Enumerate all permutations of a given string

    sequence (string): an arbitrary string to permute. Assume that it is a
    non-empty string.  

    You MUST use recursion for this part. Non-recursive solutions will not be
    accepted.

    Returns: a list of all permutations of sequence

    Example:
    >>> get_permutations('abc')
    ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']

    Note: depending on your implementation, you may return the permutations in
    a different order than what is listed here.
    '''
    if len(sequence) == 1:
        return [sequence]
    else:
        other_perms = get_permutations(sequence[1:])
        insertion_array = []
        for perm in other_perms:
            for position in range(0, len(perm) + 1):
                insertion_array += [perm[0:position] + sequence[0] + \
                    perm[position:len(perm) + 1]]
        return sorted(insertion_array)

if __name__ == '__main__':
    first_test = "abc"
    expected_first_test_output = ['abc', 'acb', 'bac', 'bca', 'cab', 'cba']
    first_permutations_output = get_permutations(first_test)
    print('Input:', first_test)
    print('Expected Output:', expected_first_test_output)
    failure = False
    if first_permutations_output != expected_first_test_output:
        print('FAILURE: get_permutations(' + first_test + ')')
        print('Returned: ', first_permutations_output)
        failure = True
    second_test = "cat"
    expected_second_test_output = ['act', 'atc', 'cat', 'cta', 'tac', 'tca']
    second_permutations_output = get_permutations(second_test)
    if second_permutations_output != expected_second_test_output:
        print('FAILURE: get_permutations(' + second_test + ')')
        print('Returned: ', second_permutations_output)
        failure = True
    third_test = "main"
    expected_third_test_output = ['aimn', 'ainm', 'amin', 'amni', 'anim', \
        'anmi', 'iamn', 'ianm', 'iman', 'imna', 'inam', 'inma', \
        'main', 'mani', 'mian', 'mina', 'mnai', 'mnia',    
        'naim', 'nami', 'niam', 'nima', 'nmai', 'nmia']
    third_permutations_output = get_permutations(third_test)
    if third_permutations_output != expected_third_test_output:
        print('FAILURE: get_permutations(' + third_test + ')')
        print('Returned: ', third_permutations_output)
        failure = True
    if not failure:
        print("All tests passing!")