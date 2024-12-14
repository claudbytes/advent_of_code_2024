from typing import List, Tuple

def read_input(text_file: str) -> Tuple[List[int], List[int]]:
    left_list: list = []
    right_list: list = []

    with open(text_file, "r") as input_file:
        for line in input_file:
            left_value = int(line[0:5].strip()) 
            right_value = int(line[8:13].strip())
            left_list.append(left_value)
            right_list.append(right_value)
    return left_list, right_list


def get_ordered_lists(left_list: list, right_list: list) -> Tuple[List[int], List[int]]:
    return sorted(left_list), sorted(right_list)


def calculate_total_distance(left: list, right: list) -> int:
    assert len(left) == len(right), f"Error: Lists have different lengths (left: {len(left)}, right: {len(right)})"
    total_dist: int = 0
    for val in range(0, len(left)):
        total_dist += abs(left[val] - right[val])

    return total_dist



