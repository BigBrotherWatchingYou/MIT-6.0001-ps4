'''def permutations(s):
    result = []

    def permute(s, current=""):
        if len(s) == 0:
            result.append(current)
            return
        for i in range(len(s)):
            permute(s[:i] + s[i+1:], current + s[i])

    permute(s)
    return result

string = 'abc'
permutations_list = permutations(string)
print("Permutations of '{}' are:".format(string))
for perm in permutations_list:
    print(perm)
'''

def permutations_2(input):
    if len(input) <= 1:
 
        return [input]
    
    else:
        perms = []
        for char in input:
            for perm in permutations_2(input.replace(char, '', 1)):
                perms.append(char + perm)
        return perms

string = 'abc'
print("Permutations of '{}' are:".format(string))
print(permutations_2(string))
       