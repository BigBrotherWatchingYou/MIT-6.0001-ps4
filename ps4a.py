# Problem Set 4A
# Name: <your name here>
# Collaborators: no
# Time Spent: x:xx

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
    permutations = []
    if len(sequence) == 1:
        # every  'else'loop starts from the second letter
        permutations.append(sequence)
        return permutations
    else:
        permutations = get_permutations(sequence[1:])
        permutations_new = []
        for element in permutations:
            # get "abc" from permutations["abc","acb"]
            i = 0
            for char in element:
                # get "a", "b", "c"from "abc"
                permutations_new.append(element[0:i]  + sequence[0] + element[i:])
                ''' when i = 0
                sequence= 'bc'
                 append= None + 'a' + 'b' '''
                i += 1
            permutations_new.append(element + sequence[0])
            ''' append= 'a'+'b'+'bc'+'b' '''
        return permutations_new
def get_permutations(s):
    if len(s) <= 1:
        return [s]
    else:
        perm_list = []
        for i in range(len(s)):
            for char in permutations(s[:i] + s[i+1:]):
                perm_list.append(s[i] + char)
        return perm_list

# Test the function with the string 'abc'
permutation_list = permutations('abc')
for perm in permutation_list:
    print(perm)

# Test the function with the string 'abc'
permutations(list('abc'))

