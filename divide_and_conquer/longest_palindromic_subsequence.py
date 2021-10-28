# find THE LENGTH OF the longest palindromic subsequence of a given string

def longest_palindromic_subsequence(s, start, end):
    # start exceeds end
    if start > end:
        return 0
    # start and end meet
    if start == end:
        return 1
    # start and end point to same character
    if s[start] == s[end]:
        return 2 + longest_palindromic_subsequence(s, start + 1, end - 1)
    # else
    branch_1 = longest_palindromic_subsequence(s, start + 1, end)
    branch_2 = longest_palindromic_subsequence(s, start, end - 1)
    return max(branch_1, branch_2)


# pointer at each end of given string
# if each points at the same character, add that to the result, move both pointers in
# otherwise, LPS is in s[1:] OR s[:-1]
# so test both of those and return whichever returns the LPS

s = "flebble"

print(longest_palindromic_subsequence(s, 0, len(s) - 1))
