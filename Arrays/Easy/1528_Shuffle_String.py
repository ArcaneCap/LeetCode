'''
You are given a string s and an integer array indices of the same length. 
The string s will be shuffled such that the character at the ith position moves to indices[i] in the shuffled string.

Return the shuffled string.
'''

def restoreString(s: str, indices: list[int]) -> str:
    ans = list(s)

    for index, char in enumerate(s):
            ans[indices[index]] = char
    return "".join(ans)

# Exp. out: 'leetcode'
print(restoreString(s = "codeleet", indices = [4,5,6,7,0,2,1,3]))
