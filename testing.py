"""
Example usage of Tracegraph's module tracing functionality.
"""

from tracegraph import trace_module, Colors, save_trace, trace
import time

# Custom colors
custom_colors = {
    "function": Colors.RED,    # Function names
    "args": Colors.YELLOW,     # Arguments
    "returns": Colors.MAGENTA, # Return values
    "error": Colors.BLUE,      # Error messages
    "tree": Colors.WHITE,      # Tree structure
}

# Example of generator function tracing
@trace(show_time=True)
def fibonacci(n):
    """Generate Fibonacci numbers up to n."""
    if n < 0:
        raise ValueError("Cannot generate Fibonacci sequence for negative numbers")
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

print("\nTesting Fibonacci generator:")
# Use the generator
for num in fibonacci(5):
    print(f"Got Fibonacci number: {num}")

# Example with error handling in generator
@trace(show_time=True)
def countdown(n):
    """Count down from n to 0."""
    if n < 0:
        raise ValueError("Cannot count down from negative number")
    while n >= 0:
        yield n
        n -= 1

print("\nTesting countdown generator with error:")
try:
    for num in countdown(-1):
        print(f"Countdown: {num}")
except ValueError as e:
    print(f"Error caught: {e}")

print("\nTesting countdown generator with success:")
# This should work fine
for num in countdown(3):
    print(f"Countdown: {num}")

# Create a module with multiple functions
class MathModule:
    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    @staticmethod
    def multiply(a, b):
        return a * b

    @staticmethod
    def divide(a, b):
        return a / b

    @staticmethod
    def complex_calculation(x, y):
        # This function calls other functions in the module
        sum_result = MathModule.add(x, y)
        diff_result = MathModule.subtract(x, y)
        return MathModule.multiply(sum_result, diff_result)

# Trace all functions in the module
trace_module(MathModule,show_time=True)

# Test the traced functions
print("\nTesting basic operations:")
result1 = MathModule.add(5, 3)
result2 = MathModule.subtract(10, 4)
result3 = MathModule.multiply(6, 7)
result4 = MathModule.divide(20, 5)

print("\nTesting complex calculation:")
# This will show the nested function calls
result5 = MathModule.complex_calculation(10, 6)
print(f"Final result: {result5}")  # Should be (10+6) * (10-6) = 16 * 4 = 64

# Example with custom colors
print("\nTesting with custom colors:")
custom_colors = {
    "function": Colors.RED,
    "args": Colors.YELLOW,
    "returns": Colors.MAGENTA,
    "error": Colors.BLUE,
    "tree": Colors.WHITE,
}

# Create a new module for colored tracing
class ColoredModule:
    @staticmethod
    def process(x):
        return x * 2

    @staticmethod
    def analyze(y):
        return ColoredModule.process(y) + 1

# Trace with custom colors
trace_module(ColoredModule, colors=custom_colors, show_time=True)

# Test the colored functions
result6 = ColoredModule.analyze(5)
print(f"Colored result: {result6}")  # Should be (5*2) + 1 = 11

# Save the trace as a graph
save_trace("trace", format="png", title="Module Tracing Example")

# @trace(colors=custom_colors, show_time=True)
# def calculate_tax(income):
#     return income * 0.3

# @trace(colors=custom_colors, show_time=True)
# def calculate_net_income(income):
#     time.sleep(2)
#     return income - calculate_tax(income)

# calculate_net_income(100000)