#!/usr/bin/env python3
"""
class
"""


class VerboseList(list):
    def append(self, item):
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, x):
        super().extend(x)
        print(f"Extended the list with [{len(x)}] items.")

    def remove(self, item):
        super().remove(item)
        print(f"Removed [{item}] from the list.")

    def pop(self, item=-1):
        item = super().pop(item)
        print(f"Popped [{item}] from the list.")
        return item
