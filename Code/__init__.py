# <QUESTION 7>

# Given three ints, a b c, one of them is small, one is medium and one is large.

# Return the boolean True if the three values are evenly spaced, so the
# difference between small and medium is the same as the difference between
# medium and large.

# Do not assume the ints will come to you in a reasonable order.

# <EXAMPLES>

# seven(2, 4, 6) → True
# seven(4, 6, 2) → True
# seven(4, 6, 3) → False
# seven(4, 60, 9) → False

# <HINT>
# There is a function for lists called sort.
# Use the cli to access the documentation help(list.sort)




def seven(a, b, c):
    num = [a, b, c]
    num.sort()
    spaced = 0
    spaced = num_list[1] - num_list[0]
    spaced -= num_list[2] - num_list[1]
    if spaced == 0:
        return True
    else:
        return False
