"""
File: task.py
Purpose: Implements the Task class for python-oop-review.
Author: IoT Solution Development Staff
Date: 2025-03-27
Version: 1.0
License: MIT

This module defines the Task class, inheriting from Executable to represent individual compilation
stages. It demonstrates encapsulation and inheritance in OOP, encapsulating task-specific behavior
and resource requirements for the process simulation in python-oop-review.
"""

from src.executable import Executable

class Task(Executable):
    """Concrete implementation of Executable for individual compilation tasks.

    Demonstrates encapsulation and inheritance.
    """

    def __init__(self, name: str, description: str, required_resources_names: list[str], duration_in_units: int):
        """Initialize a Task for a compilation stage.

        Args:
            name: The unique identifier for the task.
            description: A description of the task's purpose.
            required_resources_names: Names of resources required for execution.
            duration_in_units: Duration of execution in time units.
        """
        super().__init__(name, description, required_resources_names, duration_in_units)

    def execute(self) -> None:
        """Execute the task using assigned resources.

        Raises:
            RuntimeError: If resources are not properly assigned.
        """
        if len(self._assigned_resources) != len(self._required_resources_names):
            raise RuntimeError(f"Resources not properly assigned for task '{self._name}'")
        print(f"Executing task '{self._name}': {self._description} (Duration: {self._duration_in_units} units)")
        for resource in self._assigned_resources:
            resource.use()