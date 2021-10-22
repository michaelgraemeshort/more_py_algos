# find the minimum number of edit operations (delete, insert or replace) needed to convert string s2 to string s1
# NOT s1 to s2. don't get caught out again

string_1 = "ffs"
string_2 = "y"


def edits_needed(s1, s2, index_1=0, index_2=0):
    if index_1 == len(s1):          # end of s1
        return len(s2) - index_2    # so deletions from s2 needed for equality
    if index_2 == len(s2):          # end of s2
        return len(s1) - index_1    # so insertions needed
    if s1[index_1] == s2[index_2]:  # no edits required so
        # move on to next index
        return edits_needed(s1, s2, index_1 + 1, index_2 + 1)
    else:   # see below
        delete_ = 1 + edits_needed(s1, s2, index_1, index_2 + 1)
        insert_ = 1 + edits_needed(s1, s2, index_1 + 1, index_2)
        replace_ = 1 + edits_needed(s1, s2, index_1 + 1, index_2 + 1)
        return min(delete_, insert_, replace_)

# compare the characters
# if you aren't at the end of either string,
# and the characters do not match,
# you have three ways to rectify the situation:
# 1. delete the offending character from s2
# now compare the character you were looking at from s1, with the NEXT one from s2
# 2. insert the appropriate character into s2 IN YOUR IMAGINATION (ab, c -> ab, ac)
# now increment the index for s1 TO ACCOUNT FOR THE IMAGINARY INSERTION (watch the video to make sense of this)
# 3. replace the offending character with the correct one
# then increment both indices
# so every time you do not have a match or end-of-string situation, this branches into three
# which is what, O(n^3)?

print(edits_needed(string_1, string_2))
