
def factorial(n):
    if n < 0:
        return "Negative numbers are not allowed"

    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

def fibonacci(n):
    sequence = []
    a, b = 0, 1

    for _ in range(max(0, n)):
        sequence.append(a)
        a, b = b, a + b

    return sequence

def structure_to_dictionary(fields, values):
    if len(fields) != len(values):
        raise ValueError("Fields and values must have equal length")

    return dict(zip(fields, values))

if __name__ == "__main__":
    print("Factorial of 5:", factorial(5))
    print("First 7 Fibonacci numbers:", fibonacci(7))

    fields = ["name", "age", "course"]
    values = ["Divyanshi", 19, "CSE AI & ML"]

    print("Dictionary:", structure_to_dictionary(fields, values))