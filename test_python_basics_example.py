import unittest
import random
from statistics import mean, median, stdev

# Import the functions from the original script (assuming they are in python_basics_example.py)
from python_basics_example import (
    generate_random_numbers,
    calculate_sum,
    calculate_average,
    calculate_min,
    calculate_max,
    calculate_standard_deviation,
    sort_numbers,
    sort_numbers_desc,
    calculate_median,
    remove_duplicates,
    count_occurrences,
    find_most_common,
    loop_example,
    nested_loops_example,
    if_else_example,
    list_operations,
    string_example,
    dictionary_example,
    function_example,
    while_loop_example,
    try_except_example
)

class TestPythonBasicsExample(unittest.TestCase):

    def test_generate_random_numbers(self):
        numbers = generate_random_numbers(250)
        self.assertEqual(len(numbers), 250)
        self.assertTrue(all(1 <= num <= 100 for num in numbers))

    def test_calculate_sum(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(calculate_sum(numbers), 15)

    def test_calculate_average(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(calculate_average(numbers), 3)

    def test_calculate_min(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(calculate_min(numbers), 1)

    def test_calculate_max(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(calculate_max(numbers), 5)

    def test_calculate_standard_deviation(self):
        numbers = [1, 2, 3, 4, 5]
        expected_std_dev = stdev(numbers)  # This should be calculated as sample std dev
        self.assertAlmostEqual(calculate_standard_deviation(numbers), expected_std_dev, places=2)

    def test_sort_numbers(self):
        numbers = [5, 4, 3, 2, 1]
        self.assertEqual(sort_numbers(numbers), [1, 2, 3, 4, 5])

    def test_sort_numbers_desc(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(sort_numbers_desc(numbers), [5, 4, 3, 2, 1])

    def test_calculate_median(self):
        numbers = [1, 2, 3, 4, 5]
        self.assertEqual(calculate_median(numbers), 3)

    def test_remove_duplicates(self):
        numbers = [1, 2, 2, 3, 4, 4, 5]
        self.assertEqual(remove_duplicates(numbers), [1, 2, 3, 4, 5])

    def test_count_occurrences(self):
        numbers = [1, 2, 2, 3, 4, 4, 5]
        expected_count = {1: 1, 2: 2, 3: 1, 4: 2, 5: 1}
        self.assertEqual(count_occurrences(numbers), expected_count)

    def test_find_most_common(self):
        numbers = [1, 2, 2, 3, 4, 4, 5]
        self.assertEqual(find_most_common(numbers), 2)

    def test_loop_example(self):
        # We won't test the output directly, but we'll make sure no exceptions are raised
        try:
            loop_example()
            loop_success = True
        except Exception as e:
            loop_success = False
        self.assertTrue(loop_success)

    def test_nested_loops_example(self):
        try:
            nested_loops_example()
            nested_loops_success = True
        except Exception as e:
            nested_loops_success = False
        self.assertTrue(nested_loops_success)

    def test_if_else_example(self):
        try:
            if_else_example(10)
            if_else_success = True
        except Exception as e:
            if_else_success = False
        self.assertTrue(if_else_success)

    def test_list_operations(self):
        try:
            list_operations()
            list_operations_success = True
        except Exception as e:
            list_operations_success = False
        self.assertTrue(list_operations_success)

    def test_string_example(self):
        try:
            string_example()
            string_example_success = True
        except Exception as e:
            string_example_success = False
        self.assertTrue(string_example_success)

    def test_dictionary_example(self):
        try:
            dictionary_example()
            dictionary_example_success = True
        except Exception as e:
            dictionary_example_success = False
        self.assertTrue(dictionary_example_success)

    def test_function_example(self):
        try:
            function_example()
            function_example_success = True
        except Exception as e:
            function_example_success = False
        self.assertTrue(function_example_success)

    def test_while_loop_example(self):
        try:
            while_loop_example()
            while_loop_success = True
        except Exception as e:
            while_loop_success = False
        self.assertTrue(while_loop_success)

    def test_try_except_example(self):
        try:
            try_except_example()
            try_except_success = True
        except Exception as e:
            try_except_success = False
        self.assertTrue(try_except_success)


if __name__ == '__main__':
    unittest.main()
