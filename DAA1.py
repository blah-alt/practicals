# Iterative Fibonacci (Efficient)
def fibonacci_iterative(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

# Recursive Fibonacci with Step Count (Inefficient)
step_count = 0

def fibonacci_recursive(n):
    global step_count
    step_count += 1  # Count each function call as a step
    if n <= 1:
        return n
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)

# Function to call both methods and display results
def main():
    n = int(input("Enter the position in Fibonacci sequence: "))
    
    # Iterative Fibonacci Calculation
    result_iter = fibonacci_iterative(n)
    print(f"Iterative approach: Fibonacci number at position {n} is {result_iter}")
    
    # Recursive Fibonacci Calculation with Step Count
    global step_count
    step_count = 0  # Reset step count before calculation
    result_recur = fibonacci_recursive(n)
    print(f"Recursive approach: Fibonacci number at position {n} is {result_recur}")
    print(f"Recursive approach step count: {step_count}")

# Run the program
main()
