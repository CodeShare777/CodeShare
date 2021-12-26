#!/usr/bin/env python3
import timeit
import random

def find_data(data_structure_to_search, value_to_find):
    is_string_found = value_to_find in data_structure_to_search
    return is_string_found

def append_random_value(data_structure_to_test):
    value_to_append = random.random()
    if isinstance(data_structure_to_test, set):
        data_structure_to_test.add(value_to_append)
    elif isinstance(data_structure_to_test, list):
        data_structure_to_test.append(value_to_append)

data_structure = list() # Change this to set() to see the magic
for i in range(500):
    append_random_value(data_structure)

time_to_run = timeit.timeit("find_data(data_structure, 1.0)", number=int(1e6), globals=globals())
print(f"It took {time_to_run:.2f} seconds to search in {type(data_structure).__name__} of length {len(data_structure)}.")
