#!/usr/bin/env python3
"""Extend list with notifications for changes."""


class VerboseList(list):
    """Print notifications when items are added or removed."""

    def append(self, item):
        """Append an item and print a notification."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """Extend the list and report the number of added items."""
        items = list(iterable)
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items.")

    def remove(self, item):
        """Print a notification and remove the first matching item."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Print a notification and return the item removed by index."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
