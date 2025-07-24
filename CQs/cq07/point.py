"""CQ07 - Point Class with Mutating and Non-Mutating Methods."""

__author__ = "730607632"

from __future__ import (
    annotations,
)  # Required to reference Point before it's fully defined


class Point:
    x: float
    y: float

    def __init__(self, x_init: float, y_init: float):
        """Construct a Point with initial x and y values."""
        self.x = x_init  # Initialize x
        self.y = y_init  # Initialize y

    def scale_by(self, factor: int) -> None:
        """Mutates this Point by scaling both x and y by a factor."""
        self.x *= factor
        self.y *= factor

    def scale(self, factor: int) -> Point:
        """Returns a new Point scaled by the given factor (non-mutating)."""
        return Point(self.x * factor, self.y * factor)

    def __str__(self) -> str:
        """Returns a nicely formatted string representation of the Point."""
        return f"x: {self.x}; y: {self.y}"

    def __mul__(self, factor: int) -> Point:
        """Overloads the * operator to scale a Point."""
        return self.scale(factor)

    def __add__(self, amount: int) -> Point:
        """Overloads the + operator to add a number to x and y."""
        return Point(self.x + amount, self.y + amount)
