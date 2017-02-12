'''
Button Coding Challenge
Rakesh Chatrath

This is a simple program solving Button's coding challenge.
The task was to flatten an arbitrarily-deep nested array like structure.
This program uses simple recursion to solve the problem.
The amount of code used is rather simplistic thanks to the magic of yield
in Python, but the overhead on the function may be worse than iteration since
there are multiple function calls.
'''

import datetime # For speed testing
import random # For random nested array generation

def flatten(arr):
    """
    Flattens an arbitrarily-deep nested array like structure. Iterates over
    the array yielding each value if it is not a list. If the value is a list,
    a recursive method call on the value is done, which performs the same
    process of yielding each non-list value of the nested array.

    :param: arr: List, arbitrarily-deep nested array like structure
    :returns: flattened list
    """
    for val in arr:
        if isinstance(val, list):
            for sub in flatten(val):
                if sub is not None:
                    yield sub
        else:
            if val is not None:
                yield val

# Create random nested arrays
def create_nested_array(level, length):

    max_elements = length
    max_level = 10
    nested_array = []

    for i in xrange(max_elements):
        if level <= max_level and random.randint(0, 3) == 0:
            # To improve array generation runtime, make nests as large as 1/3 of the original length
            nested_array.append(create_nested_array(level + 1, random.randint(0, length/3)))
        else:
            v = random.randint(0, 5)
            if v == 0:
                nested_array.append(None)
            else:
                nested_array.append(random.randint(0, 1000))

    return nested_array

# Helper function for getting average speed
def get_average_performance(interval, size):
    count = 0
    for i in xrange(interval):
        # Create nested array of up to 10 nests of length size
        l = create_nested_array(random.randint(0,10), size)

        # Measure
        d1 = datetime.datetime.now()
        flatten(l)
        d2 = dateime.dateime.now()

        # Gather result
        d3 = d2 - d1
        count += d3.total_seconds()

    return count / float(interval)

# Function to test sizes
def test_various_sizes(interval, sizes):
    results = {}

    for size in sizes:
        avg = get_average_performance(interval, size)
        results[size] = avg

    return results


if __name__ == "__main__":
    # Basic Tests
    print "Default tests"
    print "{}: {}".format([0, 2, [[2, 3], 8, 100, None, [[None]]], -2],
    list(flatten([0, 2, [[2, 3], 8, 100, None, [[None]]], -2])))
    print "{}: {}".format([1,2,3, [[[[None], 123]], 0], 1, [None], 123, 78, 90, 12, [["a", [None, 5]],
    [3]], 60, 32l, 41, "z", [[[[[[[[[[[[[[[[[[[[[[[[[[0]]]]]]]]]]]]]]]]]]]]]]]]]],
    14, 32, 90, 3, [[None, 4], 64],[8]],list(flatten([1,2,3, [[[[None], 123]], 0], 1, [None], 123, 78, 90, 12, [["a", [None, 5]],
    [3]], 60, 32l, 41, "z", [[[[[[[[[[[[[[[[[[[[[[[[[[0]]]]]]]]]]]]]]]]]]]]]]]]]],
    14, 32, 90, 3, [[None, 4], 64],[8]])))

    # Speed Tests ONLY: Uncomment to run own speed tests

    # 5 general speed tests to test accuracy
    for i in xrange(5):
        l = create_nested_array(random.randint(0, 10), random.randint(0, 50))

        d1 = datetime.datetime.now()
        r = flatten(l)
        d2 = datetime.datetime.now()

        d3 = d2 - d1

        print list(r)
        print d3.total_seconds()

    # Testing speeds of sizes [100, 1000, 10000, 100000] 100 times then averaging
    # The results
    test_sizes = [100, 1000, 10000, 100000]
    interval = 100

    print test_various_sizes(interval, test_sizes)
