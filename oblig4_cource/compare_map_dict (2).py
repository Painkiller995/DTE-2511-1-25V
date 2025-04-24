# filename: compare_map_dict.py
import time
from random import randint

from map_uten_duplikater_fn import Map  # lag din egen import


def test_map_implementation():
    custom_map = Map()
    python_dict = {}

    # Test inserting elements
    num_elements = 100000
    keys = [randint(1, num_elements) for _ in range(num_elements)]
    values = [randint(1, num_elements) for _ in range(num_elements)]

    # Test custom Map
    start = time.time()
    for key, value in zip(keys, values):
        custom_map.put(key, value)
    custom_map_insertion_time = time.time() - start

    # Test Python dict
    start = time.time()
    for key, value in zip(keys, values):
        python_dict[key] = value
    python_dict_insertion_time = time.time() - start

    # Test retrieving elements
    start = time.time()
    for key in keys:
        custom_map.get(key)
    custom_map_retrieval_time = time.time() - start

    start = time.time()
    for key in keys:
        python_dict.get(key)
    python_dict_retrieval_time = time.time() - start

    # Test removing elements
    start = time.time()
    for key in keys:
        custom_map.remove(key)
    custom_map_removal_time = time.time() - start

    start = time.time()
    for key in keys:
        python_dict.pop(key, None)
    python_dict_removal_time = time.time() - start

    print("Custom Map:")
    print(f"Insertion time: {custom_map_insertion_time:.4f} seconds")
    print(f"Retrieval time: {custom_map_retrieval_time:.4f} seconds")
    print(f"Removal time: {custom_map_removal_time:.4f} seconds")

    print("\nPython dict:")
    print(f"Insertion time: {python_dict_insertion_time:.4f} seconds")
    print(f"Retrieval time: {python_dict_retrieval_time:.4f} seconds")
    print(f"Removal time: {python_dict_removal_time:.4f} seconds")

if __name__ == "__main__":
    test_map_implementation()