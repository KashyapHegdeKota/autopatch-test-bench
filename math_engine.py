def calculate_average(numbers):
    #BUG: This will crash with a ZeroDivisionError if the list is empty
    # A perfect case for the AI to fix!
    return sum(numbers) / len(numbers)