"""
File: process.py
Purpose: Implements the Process class for python-oop-review.
Author: IoT Solution Development Staff
Date: 2025-03-27
Version: 1.0
License: MIT

This module defines the Process class, inheriting from Executable to manage a sequence of tasks.
It demonstrates composition and polymorphism in OOP, orchestrating tasks and resources in the
compilation simulation for python-oop-review, showcasing hierarchical process management.
"""

from src.executable import Executable
from src.resource import Resource
from typing import List

class Process(Executable):
    """Concrete implementation of Executable for managing a sequence of tasks.

    Demonstrates composition and polymorphism.
    """

    def __init__(self, name: str, description: str, required_resources_names: List[str], duration_in_units: int):
        """Initialize a Process to manage a sequence of tasks.

        Args:
            name: The unique identifier for the process.
            description: A description of the process's purpose.
            required_resources_names: Names of resources required if acting as a task.
            duration_in_units: Duration of execution in time units.
        """
        super().__init__(name, description, required_resources_names, duration_in_units)
        self._resource_pool: List[Resource] = []
        self._tasks: List[Executable] = []

    def add_resource(self, resource: Resource) -> None:
        """Add a resource to the process's resource pool.

        Args:
            resource: The resource to add.
        """
        self._resource_pool.append(resource)

    def add_task(self, task: Executable) -> None:
        """Add a task to the process's sequence.

        Args:
            task: The task to add.
        """
        self._tasks.append(task)

    def execute(self) -> None:
        """Execute the process by running its sequence of tasks.

        Raises:
            RuntimeError: If resources are not properly assigned or tasks fail.
        """
        if self._required_resources_names and len(self._assigned_resources) != len(self._required_resources_names):
            raise RuntimeError(f"Resources not properly assigned for process '{self._name}'")
        print(f"Executing process '{self._name}': {self._description} (Duration: {self._duration_in_units} units)")
        if self._assigned_resources:
            for resource in self._assigned_resources:
                resource.use()

        for task in self._tasks:
            try:
                if task.can_execute(self._resource_pool):
                    task.assign_resources(self._resource_pool)
                    print("  ", end="")
                    task.execute()
                    task.release_resources()
                else:
                    print(f"  Task '{task.name}' skipped: insufficient resources")
            except Exception as e:
                print(f"  Error in '{task.name}': {e}")

    def run(self) -> None:
        """Run the process standalone, managing its own resource pool.

        Raises:
            RuntimeError: If insufficient resources are available to start.
        """
        try:
            if not self._required_resources_names or self.can_execute(self._resource_pool):
                if self._required_resources_names:
                    self.assign_resources(self._resource_pool)
                self.execute()
                self.release_resources()
                print(f"Process '{self._name}' completed.")
            else:
                raise RuntimeError(f"Insufficient resources in pool to start '{self._name}'")
        except Exception as e:
            print(f"Error in process '{self._name}': {e}")