#!/usr/bin/python3
'''my list'''


class MyList(list):
    """modify list and sorted list"""

    def print_sorted(self):
        print(sorted(self))
