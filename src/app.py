def find_refs(x):
    # changed behavior
    return x * 3


def use():
    # call moved to a different line to produce a ref change
    return


def other():
    # second caller (new reference)
    return find_refs(5)
