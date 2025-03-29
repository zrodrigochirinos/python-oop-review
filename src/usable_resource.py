"""
File: usable_resource.py
Purpose: Implements the UsableResource class for python-oop-review.
Author: IoT Solution Development Staff
Date: 2025-03-27
Version: 1.0
License: MIT

This module defines the UsableResource class, inheriting from Resource to model reusable resources
like a CPU. It showcases inheritance and polymorphism in OOP, providing a distinct implementation
of resource management for the process simulation in python-oop-review.
"""

from src.resource import Resource, ResourceType

class UsableResource(Resource):
    """Usable resource that is occupied during use, such as a CPU.

    Demonstrates inheritance and polymorphism from Resource.
    """

    def __init__(self, name: str, capacity: int):
        """Initialize a UsableResource with a name and capacity.

        Args:
            name: The unique identifier for the resource.
            capacity: The capacity of the resource (e.g., GHz).

        Raises:
            ValueError: If capacity is not positive.
        """
        super().__init__(name, ResourceType.USABLE)
        if capacity <= 0:
            raise ValueError(f"Capacity for resource '{name}' must be positive")
        self._capacity = capacity

    def is_available_for_use(self) -> bool:
        """Check if the resource is available.

        Returns:
            True if the resource is not currently allocated, False otherwise.
        """
        return self._is_available

    def allocate(self) -> None:
        """Allocate the resource, marking it as unavailable.

        Raises:
            RuntimeError: If the resource is already allocated.
        """
        if not self._is_available:
            raise RuntimeError(f"Usable resource '{self._name}' is already allocated")
        self._is_available = False

    def release(self) -> None:
        """Release the resource, making it available again."""
        if self._is_available:
            print(f"Warning: Attempted to release already free usable resource '{self._name}'")
        self._is_available = True

    def use(self) -> None:
        """Display the resource usage details."""
        print(f"    Using usable resource '{self._name}' (capacity: {self._capacity} GHz)")