# see https://medium.com/outco/how-to-solve-power-set-c8ef7d1382ee

def power_set(s):   # "abc"
    # a set of all possible subsets
    # including, weirdly, an empty set
    subsets = {""}
    # add "a" to subsets -> {"", "a"}
    # then add "b" -> {"", "a", "b", "ab"}
    # then add "c" -> {"", "a", "b", "ab", "c", "ac", "bc", "abc"}
    for character in s:  # "abc"
        combinations = subsets.copy()
        for subset in combinations:
            subsets.add(subset + character)
    return subsets


# now recursively, for the exercise
# difficult, so translated this from above article
def recursive_power_set(s):
    subsets = set()

    def make_subsets(subset, index):
        if (index == len(s)):
            subsets.add(subset)
            return
        make_subsets(subset, index + 1)
        make_subsets(subset + s[index], index + 1)

    make_subsets("", 0)
    return subsets

    # this is horrible
    # anyway: what does make_subsets do?
    # adds subsets to the set "subsets"
    # but only when index == len(s)
    # that is, when you have added every character and therefore have made all of the subsets
    # so base case is "nothing more to add"
    # return prevents further recursion, which would otherwise be infinite
    # what about those two recursive calls?
    # (do it on paper!)
    # the first adds the subset passed to it to subsets
    # the second adds the next character to the subset passed to it, so the combination is added to subsets
    # if you take the "recursiveness" out of make_subsets(subset, index + 1)...
    # you get subsets.add(subset)
    # likewise, make_subsets(subset + s[index], index + 1) ->
    # subsets.add(subset + s[index])


print(power_set("abc"))

# print(recursive_power_set("abc"))
