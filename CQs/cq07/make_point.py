"""CQ07 - Point class tester."""

__author__ = "730607632"

# Import the Point class from the cq07 folder
from CQs.cq07.point import Point

# Create an original Point with x = 1.0 and y = 2.0
original_point: Point = Point(1.0, 2.0)
print("Original Point:", original_point)  # Expected: x: 1.0; y: 2.0

# Use the non-mutating scale method to get a new scaled Point
scaled_point: Point = original_point.scale(3)
print("Scaled Point (non-mutating):", scaled_point)  # Expected: x: 3.0; y: 6.0

# Confirm that original_point did NOT change after calling scale()
print("Original Point after scale():", original_point)  # Should still be x: 1.0; y: 2.0

# Use the mutating method scale_by to update original_point
original_point.scale_by(3)
print("Original Point after scale_by():", original_point)  # Expected: x: 3.0; y: 6.0

# Create a new Point to test operator overloading
p2: Point = Point(2.0, 3.0)

# Use the * operator, which calls __mul__ to return a new scaled Point
p3: Point = p2 * 2
print("Operator * result:", p3)  # Expected: x: 4.0; y: 6.0

# Use the + operator, which calls __add__ to shift both x and y
p4: Point = p2 + 1.5  # Adds 1.5 to both x and y
print("Operator + result:", p4)  # Expected: x: 3.5; y: 4.5
