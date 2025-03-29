"""
File: consumable_resource.py
Purpose: Implements the ConsumableResource class for python-oop-review.
Author: IoT Solution Development Staff
Date: 2025-03-27
Version: 1.0
License: MIT

This module defines the ConsumableResource class, inheriting from Resource to model
resources that can be consumed like memory. It demonstrates inheritance and encapsulation in OOP by managing a finite
capacity that decreases with use, integral to the process simulation in python-oop-review.
"""

from src.resource import Resource, ResourceType

class ConsumableResource(Resource):
    """Consumable resource that depletes upon use, such as memory.

    Demonstrates inheritance from Resource.
    """

    def __init__(self, name: str, capacity: int):
        """Initialize a ConsumableResource with a name and capacity.

        Args:
            name: The unique identifier for the resource.
            capacity: The total capacity of the resource (e.g., MB).

        Raises:
            ValueError: If capacity is not positive.
        """
        super().__init__(name, ResourceType.CONSUMABLE)
        if capacity <= 0:
            raise ValueError(f"Capacity for resource '{name}' must be positive")
        self._total_capacity = capacity
        self._remaining_capacity = capacity

    def is_available_for_use(self) -> bool:
        """Check if the resource has remaining capacity.

        Returns:
            True if remaining capacity is greater than 0, False otherwise.
        """
        return self._remaining_capacity > 0

    def allocate(self) -> None:
        """Allocate one unit of the resource, reducing its remaining capacity.

        Raises:
            RuntimeError: If no capacity remains to allocate.
        """
        if self._remaining_capacity <= 0:
            raise RuntimeError(f"No remaining capacity for consumable resource '{self._name}'")
        self._remaining_capacity -= 1
        self._is_available = self._remaining_capacity > 0

    def release(self) -> None:
        """Release the resource, updating availability status.

        Note:
            Does not restore capacity; external replenishment is required.
        """
        if self._remaining_capacity == 0 and not self._is_available:
            print(f"Warning: Consumable resource '{self._name}' is depleted and cannot be reused without replenishment")
        self._is_available = self._remaining_capacity > 0

    def use(self) -> None:
        """Display the resource usage details."""
        print(f"    Using consumable resource '{self._name}' (remaining: {self._remaining_capacity}/{self._total_capacity} MB)")

    @property
    def remaining_capacity(self) -> int:
        """Get the remaining capacity of the resource."""
        return self._remaining_capacity