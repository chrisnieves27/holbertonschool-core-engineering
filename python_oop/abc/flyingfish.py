#!/usr/bin/env python3
"""Demonstrate multiple inheritance with a flying fish."""


class Fish:
    """Represent a fish."""

    def swim(self):
        """Print how a fish swims."""
        print("The fish is swimming")

    def habitat(self):
        """Print where a fish lives."""
        print("The fish lives in water")


class Bird:
    """Represent a bird."""

    def fly(self):
        """Print how a bird flies."""
        print("The bird is flying")

    def habitat(self):
        """Print where a bird lives."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """Represent a flying fish using multiple inheritance."""

    def fly(self):
        """Print how a flying fish flies."""
        print("The flying fish is soaring!")

    def swim(self):
        """Print how a flying fish swims."""
        print("The flying fish is swimming!")

    def habitat(self):
        """Print where a flying fish lives."""
        print("The flying fish lives both in water and the sky!")
