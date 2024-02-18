
def get_permutations(s):
    if len(s) <= 1:
        return [s]
    else:
        perm_list = []
        for i in range(len(s)):
            for char in get_permutations(s[:i] + s[i+1:]):
                perm_list.append(s[i] + char)
        return perm_list
# Test the function with the string 'abc'
permutation_list = get_permutations(str('abc'))
for perm in permutation_list:
    print(perm)