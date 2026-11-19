#!/usr/bin/env python3
"""Define a rectangle that inherits from BaseGeometry."""
from base_geometry import BaseGeometry


class Rectangle(BaseGeometry):
    """Represent a rectangle with private, validated dimensions."""

    def __init__(self, width, height):
        """Initialize a rectangle with positive integer dimensions."""
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
