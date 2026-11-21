#!/usr/bin/env python3
"""Combine swimming and flying mixins in a dragon class."""


class SwimMixin:
    """Provide swimming behavior."""

    def swim(self):
        """Print the swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Provide flying behavior."""

    def fly(self):
        """Print the flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """Combine swimming and flying with a dragon's roar."""

    def roar(self):
        """Print the dragon's roar."""
        print("The dragon roars!")
