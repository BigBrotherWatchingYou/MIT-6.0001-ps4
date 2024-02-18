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

class get_permutations(s):
    data = str(s)
    permutation = []
    def permutate(data, i):
        if i >= len(data):
            permutation.append(data)
        else:
            for j in range[i:len(data)]:
                data[i],data[j] = data[j],data[i]
                i += 1
                permutate(data,i)
                data[i],data[j] = data[j],[i]
    
    
# Test the function with the string 'abc'
permutations(list('abc'))

