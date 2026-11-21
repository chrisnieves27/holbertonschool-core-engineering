#!/usr/bin/env python3
"""Define an abstract animal and concrete animal subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Define the required interface for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Represent a dog"""
        
    def sound(self):
        """Return the dog's sound"""
        return "Bark"
    

class Cat(Animal):
    """Represent a cat"""

    def sound(self):
        """Return the cat's sound"""
        return "Meow"

        
