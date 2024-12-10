import random
import math


# Function to generate a list of random numbers

def generate_random_numbers(n, lower=1, upper=100):
    return [random.randint(lower, upper) for _ in range(n)]


# Function to calculate the sum of a list of numbers

def calculate_sum(numbers):
    return sum(numbers)


# Function to calculate the average of a list of numbers

def calculate_average(numbers):
    return sum(numbers) / len(numbers) if numbers else 0


# Function to calculate the minimum value of a list of numbers

def calculate_min(numbers):
    return min(numbers)


# Function to calculate the maximum value of a list of numbers

def calculate_max(numbers):
    return max(numbers)


# Function to calculate the standard deviation of a list of numbers

def calculate_standard_deviation(numbers):
 if len(numbers) <= 1:
  return 0
 mean = calculate_average(numbers)
 variance = sum((x - mean) ** 2 for x in numbers) / (len(numbers) - 1)  # divide by len(numbers) - 1 for sample std dev
 return math.sqrt(variance)


# Function to sort a list in ascending order

def sort_numbers(numbers):
    return sorted(numbers)


# Function to sort a list in descending order

def sort_numbers_desc(numbers):
    return sorted(numbers, reverse=True)


# Function to find the median of a list of numbers

def calculate_median(numbers):
    n = len(numbers)
    if n == 0:
        return 0
    numbers.sort()
    middle = n // 2
    if n % 2 == 0:
        return (numbers[middle - 1] + numbers[middle]) / 2
    return numbers[middle]


# Function to remove duplicates from a list

def remove_duplicates(numbers):
    return list(set(numbers))


# Function to count occurrences of each number in a list

def count_occurrences(numbers):
    count_dict = {}
    for num in numbers:
        count_dict[num] = count_dict.get(num, 0) + 1
    return count_dict


# Function to find the most common number in a list

def find_most_common(numbers):
    count_dict = count_occurrences(numbers)
    return max(count_dict, key=count_dict.get)


# Function to generate a random set of numbers and perform calculations

def perform_calculations():
    numbers = generate_random_numbers(250)

    print("Generated Numbers:")
    print(numbers)

    total_sum = calculate_sum(numbers)
    print("\nSum of numbers:", total_sum)

    average = calculate_average(numbers)
    print("Average of numbers:", average)

    minimum = calculate_min(numbers)
    print("Minimum value:", minimum)

    maximum = calculate_max(numbers)
    print("Maximum value:", maximum)

    standard_deviation = calculate_standard_deviation(numbers)
    print("Standard Deviation:", standard_deviation)

    median = calculate_median(numbers)
    print("Median value:", median)

    sorted_numbers = sort_numbers(numbers)
    print("Sorted numbers in ascending order:")
    print(sorted_numbers)

    sorted_numbers_desc = sort_numbers_desc(numbers)
    print("Sorted numbers in descending order:")
    print(sorted_numbers_desc)

    unique_numbers = remove_duplicates(numbers)
    print("Unique numbers:", unique_numbers)

    most_common = find_most_common(numbers)
    print("Most common number:", most_common)


# Function to demonstrate using loops and conditions

def loop_example():
    print("\nLoop Example:")
    for i in range(1, 11):
        if i % 2 == 0:
            print(f"{i} is even")
        else:
            print(f"{i} is odd")


# Function to demonstrate using nested loops

def nested_loops_example():
    print("\nNested Loops Example:")
    for i in range(1, 6):
        for j in range(1, 6):
            print(f"({i}, {j})", end=" ")
        print()


# Function to demonstrate a simple if-else block

def if_else_example(x):

    if x > 0:
        print(f"{x} is positive")
    elif x < 0:
        print(f"{x} is negative")
    else:
        print(f"{x} is zero")


# Function to demonstrate basic list operations

def list_operations():
    print("\nList Operations Example:")
    my_list = [1, 2, 3, 4, 5]
    print("Original list:", my_list)

    my_list.append(6)
    print("After appending 6:", my_list)

    my_list.remove(2)
    print("After removing 2:", my_list)

    my_list.insert(2, 7)
    print("After inserting 7 at index 2:", my_list)

    my_list.pop()
    print("After popping the last element:", my_list)


# Function to demonstrate string manipulation

def string_example():
    text = "Hello, Python World!"
    print("\nString Example:")
    print("Original text:", text)
    print("Uppercase:", text.upper())
    print("Lowercase:", text.lower())
    print("Split by space:", text.split())
    print("Replaced 'Python' with 'Java':", text.replace("Python", "Java"))


# Function to demonstrate dictionary usage

def dictionary_example():
    print("\nDictionary Example:")
    my_dict = {'name': 'Alice', 'age': 30, 'city': 'New York'}
    print("Original dictionary:", my_dict)
    print("Accessing 'name':", my_dict['name'])

    my_dict['age'] = 31
    print("After updating 'age':", my_dict)

    my_dict['country'] = 'USA'
    print("After adding 'country':", my_dict)

    del my_dict['city']
    print("After deleting 'city':", my_dict)


# Function to demonstrate basic function usage

def function_example():
    print("\nFunction Example:")

    def greet(name):
        return f"Hello, {name}!"

    print(greet("Alice"))
    print(greet("Bob"))


# Function to demonstrate a simple while loop

def while_loop_example():
    print("\nWhile Loop Example:")
    counter = 1
    while counter <= 5:
        print(f"Counter: {counter}")
        counter += 1


# Function to demonstrate using try-except for error handling

def try_except_example():
    print("\nTry-Except Example:")
    try:
        x = 10 / 0
    except ZeroDivisionError:
        print("Error: Division by zero!")
    else:
        print("Division was successful.")
    finally:
        print("This will always run.")


# Main function to run all examples

def main():

    perform_calculations()
    loop_example()
    nested_loops_example()
    if_else_example(10)
    list_operations()
    string_example()
    dictionary_example()
    function_example()
    while_loop_example()
    try_except_example()


# Run the main function

if __name__ == "__main__":
    main()
