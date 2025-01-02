def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list case explicitly
    return sum(numbers) / len(numbers)

#Improved version with exception handling for more robustness
def calculate_average_robust(numbers):
    try:
        if not numbers:
            return 0
        return sum(numbers) / len(numbers)
    except TypeError as e:
        print(f"Error calculating average: {e}")
        return None