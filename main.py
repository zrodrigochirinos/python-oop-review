"""
File: main.py
Purpose: Entry point for the python-oop-review project demonstrating OOP concepts.
Author: IoT Solution Development Staff
Date: 2025-03-27
Version: 1.0
License: MIT

This script simulates a compilation process where a Process manages Tasks,
utilizing Consumable (Memory) and Usable (CPU) resources, showcasing
encapsulation, inheritance, polymorphism, and abstraction in Python.
"""

from src.process import Process
from src.task import Task
from src.usable_resource import UsableResource
from src.consumable_resource import ConsumableResource

def main():
    """Main function to demonstrate OOP concepts via process simulation."""
    try:
        # Compilation process for main.c
        compilation_process = Process("CompileMain", "Compile main.c to main.exe",
                                      ["CentralProcessingUnit", "Memory"], 15)

        # Add resources to the pool
        compilation_process.add_resource(UsableResource("CentralProcessingUnit", 3))
        compilation_process.add_resource(ConsumableResource("Memory", 4096))

        # Define compilation tasks
        compilation_process.add_task(Task("ScanSourceCode", "Tokenize main.c",
                                          ["CentralProcessingUnit", "Memory"], 2))
        compilation_process.add_task(Task("ParseSyntax", "Build syntax tree from tokens",
                                          ["CentralProcessingUnit", "Memory"], 3))
        compilation_process.add_task(Task("PerformStaticAnalysis", "Check syntax tree for errors",
                                          ["CentralProcessingUnit", "Memory"], 4))
        compilation_process.add_task(Task("GenerateCode", "Generate machine code",
                                          ["CentralProcessingUnit", "Memory"], 3))
        compilation_process.add_task(Task("LinkBinary", "Link object files into main.exe",
                                          ["CentralProcessingUnit", "Memory"], 2))

        # Run successful compilation
        print("Starting compilation simulation...")
        compilation_process.run()

        # Simulate compilation with limited memory
        print("\nSimulating compilation with limited memory...")
        limited_compilation = Process("CompileLimited", "Compile main.c with low memory",
                                      ["CentralProcessingUnit", "Memory"], 15)
        limited_compilation.add_resource(UsableResource("CentralProcessingUnit", 3))
        limited_compilation.add_resource(ConsumableResource("Memory", 2))
        limited_compilation.add_task(Task("ScanSourceCode", "Tokenize main.c",
                                          ["CentralProcessingUnit", "Memory"], 2))
        limited_compilation.add_task(Task("ParseSyntax", "Build syntax tree from tokens",
                                          ["CentralProcessingUnit", "Memory"], 3))
        limited_compilation.run()

    except Exception as e:
        print(f"Critical error in main: {e}")
        exit(1)

if __name__ == "__main__":
    main()