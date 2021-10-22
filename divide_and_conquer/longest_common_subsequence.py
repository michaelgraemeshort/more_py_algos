# subsequence: a sequence that can be derived from another sequence by deleting one or more elements,
# without changing the order
# unlike substrings, subsequences are not required to occupy consecutive positions within the parent sequence
# so ACE is a valid subsequence of ABCDE

# find the length of the longest common subsequence that is common to two given strings

# naive recursive implementation:
# compare the characters at index 0
# if they are the same, add one to the length of the LCS, then compare the characters at index 1
# otherwise, the LCS is composed of characters from either s1[:] and s2[1:], or s1[1:] and s2[:]
# so find out which of those has the longest

def longest_common_subsequence(s1, s2, i1=0, i2=0):
    # if at end of either string, no further additions to subsequence possible
    if i1 >= len(s1) or i2 >= len(s2):
        return 0
    if s1[i1] == s2[i2]:
        return 1 + longest_common_subsequence(s1, s2, i1 + 1, i2 + 1)
    branch_1 = longest_common_subsequence(s1, s2, i1, i2 + 1)
    branch_2 = longest_common_subsequence(s1, s2, i1 + 1, i2)
    return max(branch_1, branch_2)


s1 = "elephant"
s2 = "eretpat"

print(longest_common_subsequence(s1, s2))
