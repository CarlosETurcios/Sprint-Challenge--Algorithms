'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):
    # need to use recursion to find "th"
    # set index
    # need to sort the count of how many times "th" occurs mybe in a list
    # capital Th, TH,tH does not count
    # need a base case, should equal 0
    # recursive case
    #
    w = "th"
    l = len("th")

    # base case
    if word == "":
        return 0
        # recurtion
    if word[0:l] == w:
        return 1 + count_th(word[1:])
    else:
        return count_th(word[1:])

    # TBC

    pass
