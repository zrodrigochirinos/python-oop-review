"""
File: resource.py
Purpose: Defines the abstract Resource base class for python-oop-review.
Author: IoT Solution Development Staff
Date: 2025-03-27
Version: 1.0
License: MIT

This module provides the Resource abstract base class, illustrating abstraction in OOP.
It serves as the foundation for ConsumableResource and UsableResource, defining a common
interface for resource management in the process simulation, including allocation,
release, and usage tracking.
"""

from abc import ABC, abstractmethod
from enum import Enum

class ResourceType(Enum):
    """Enumeration defining resource types."""
    CONSUMABLE = "Consumable"
    USABLE = "Usable"

class Resource(ABC):
    """Abstract base class for resources used in executable tasks or processes.

    This class defines the interface for resources, demonstrating abstraction.
    """

    def __init__(self, name: str, resource_type: ResourceType):
        """Initialize a Resource with a name and type.

        Args:
            name: The unique identifier for the resource.
            resource_type: The type of resource (Consumable or Usable).
        """
        self._name = name
        self._is_available = True
        self._resource_type = resource_type

    @property
    def name(self) -> str:
        """Get the resource's unique identifier."""
        return self._name

    @property
    def resource_type(self) -> ResourceType:
        """Get the resource type."""
        return self._resource_type

    @abstractmethod
    def is_available_for_use(self) -> bool:
        """Check if the resource is available for allocation.

        Returns:
            True if the resource can be allocated, False otherwise.
        """
        pass

    @abstractmethod
    def allocate(self) -> None:
        """Allocate the resource for use.

        Raises:
            RuntimeError: If the resource cannot be allocated.
        """
        pass

    @abstractmethod
    def release(self) -> None:
        """Release the resource after use."""
        pass

    @abstractmethod
    def use(self) -> None:
        """Define how the resource is utilized during execution."""
        pass