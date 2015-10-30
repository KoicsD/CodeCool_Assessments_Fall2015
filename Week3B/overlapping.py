__author__ = 'KoicsD'


# Creating a function wich takes 2 lists as arguments
# and returns if there are common elements.


def overlapping(list1: list, list2: list):
    for item_a in list1:
        for item_b in list2:
            if item_a == item_b:
                return True
    return False

# Besides: There must be a loop-omitting solution with 'set'.
