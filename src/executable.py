"""
File: executable.py
Purpose: Defines the abstract Executable base class for python-oop-review.
Author: IoT Solution Development Staff
Date: 2025-03-27
Version: 1.0
License: MIT

This module provides the Executable abstract base class, illustrating abstraction in OOP.
It serves as the foundation for Task and Process classes, defining common behavior for entities
that require resources to execute, central to the process simulation in python-oop-review.
"""

from abc import ABC, abstractmethod
from src.resource import Resource
from typing import List

class Executable(ABC):
    """Abstract base class for entities that can be executed with resource requirements.

    Demonstrates abstraction and serves as a base for Task and Process.
    """

    def __init__(self, name: str, description: str, required_resources_names: List[str], duration_in_units: int):
        """Initialize an Executable entity.

        Args:
            name: The unique identifier for the entity.
            description: A description of the entity's purpose.
            required_resources_names: Names of resources required for execution.
            duration_in_units: Duration of execution in time units.

        Raises:
            ValueError: If name is empty or duration is not positive.
        """
        if not name:
            raise ValueError("Executable name cannot be empty")
        if duration_in_units <= 0:
            raise ValueError(f"Duration for '{name}' must be positive")
        self._name = name
        self._description = description
        self._required_resources_names = required_resources_names
        self._duration_in_units = duration_in_units
        self._assigned_resources: List[Resource] = []

    @property
    def name(self) -> str:
        """Get the entity's unique identifier."""
        return self._name

    @property
    def required_resources_names(self) -> List[str]:
        """Get the names of required resources."""
        return self._required_resources_names

    @property
    def duration_in_units(self) -> int:
        """Get the execution duration."""
        return self._duration_in_units

    def assign_resources(self, resource_pool: List[Resource]) -> None:
        """Assign required resources from a pool.

        Args:
            resource_pool: The pool of available resources.

        Raises:
            RuntimeError: If any required resource is unavailable.
        """
        self._assigned_resources.clear()
        if not self._required_resources_names:
            return

        for resource_name in self._required_resources_names:
            found = False
            for resource in resource_pool:
                if resource.name == resource_name and resource.is_available_for_use():
                    resource.allocate()
                    self._assigned_resources.append(resource)
                    found = True
                    break
            if not found:
                self.release_resources()
                raise RuntimeError(f"Resource '{resource_name}' not available for '{self._name}'")

    def release_resources(self) -> None:
        """Release all assigned resources."""
        for resource in self._assigned_resources:
            try:
                resource.release()
            except Exception as e:
                print(f"Warning: Failed to release resource '{resource.name}' in '{self._name}': {e}")
        self._assigned_resources.clear()

    @abstractmethod
    def execute(self) -> None:
        """Execute the entity using assigned resources.

        Raises:
            RuntimeError: If resources are not properly assigned.
        """
        pass

    def can_execute(self, resource_pool: List[Resource]) -> bool:
        """Check if the entity can be executed with the given resource pool.

        Args:
            resource_pool: The pool of available resources.

        Returns:
            True if all required resources are available, False otherwise.
        """
        if not self._required_resources_names:
            return True
        for resource_name in self._required_resources_names:
            if not any(r.name == resource_name and r.is_available_for_use() for r in resource_pool):
                return False
        return True