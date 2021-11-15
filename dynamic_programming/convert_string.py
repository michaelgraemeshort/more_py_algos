# here is the naive recursive implementation


def edits_needed(s1, s2, index_1=0, index_2=0):
    if index_1 == len(s1):          # end of s1
        return len(s2) - index_2    # so deletions from s2 needed for equality
    if index_2 == len(s2):          # end of s2
        return len(s1) - index_1    # so insertions needed
    if s1[index_1] == s2[index_2]:  # no edits required so
        # move on to next index
        return edits_needed(s1, s2, index_1 + 1, index_2 + 1)
    else:   # see divide_and_conquer/convert_string.py for explanation
        delete_ = 1 + edits_needed(s1, s2, index_1, index_2 + 1)
        insert_ = 1 + edits_needed(s1, s2, index_1 + 1, index_2)
        replace_ = 1 + edits_needed(s1, s2, index_1 + 1, index_2 + 1)
        return min(delete_, insert_, replace_)


# top down, with memoization
# to avoid calculating e.g. edits_needed(s1, s2, 1, 1) repeatedly
# as ever, make a dict, store results of subproblems in it


def edits_needed_2(s1, s2, memo_dict, index_1=0, index_2=0):
    if index_1 == len(s1):
        return len(s2) - index_2
    if index_2 == len(s2):
        return len(s1) - index_1
    if s1[index_1] == s2[index_2]:
        return edits_needed_2(s1, s2, memo_dict, index_1 + 1, index_2 + 1)
    else:
        key = str(index_1) + str(index_2)
        if key not in memo_dict:
            delete_ = 1 + edits_needed_2(s1, s2, memo_dict, index_1, index_2 + 1)
            insert_ = 1 + edits_needed_2(s1, s2, memo_dict, index_1 + 1, index_2)
            replace_ = 1 + edits_needed_2(s1, s2, memo_dict, index_1 + 1, index_2 + 1)
            memo_dict[key] = min(delete_, insert_, replace_)
        return memo_dict[key]


# bottom-up
# return to this. cannot see any advantage over top-down


def edits_needed_3(s1, s2, index_1=0, index_2=0):
    pass
           
            
# memo_dict = {}
# print(edits_needed_2("abcdefg", "hijklmn", memo_dict))
