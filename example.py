#!/usr/bin/env python3
"""
Welcome to Python Playground!

This is a simple example file to get you started with Python development
in GitHub Codespaces.
"""

def hello_playground():
    """A simple function to demonstrate Python in the playground."""
    print("🐍 Welcome to Python Playground! 🚀")
    print("This environment is ready for Python development.")
    return "Hello from Python Playground!"


def demonstrate_libraries():
    """Demonstrate some of the included libraries."""
    try:
        import numpy as np
        import pandas as pd
        from rich.console import Console
        
        console = Console()
        console.print("✅ Libraries loaded successfully!", style="green")
        
        # Simple numpy example
        arr = np.array([1, 2, 3, 4, 5])
        console.print(f"NumPy array: {arr}", style="blue")
        
        # Simple pandas example
        df = pd.DataFrame({'numbers': [1, 2, 3], 'letters': ['a', 'b', 'c']})
        console.print("Pandas DataFrame:", style="blue")
        console.print(df)
        
    except ImportError as e:
        print(f"Some libraries are not available: {e}")
        print("Run 'pip install -r requirements.txt' to install dependencies")


if __name__ == "__main__":
    hello_playground()
    print()
    demonstrate_libraries()