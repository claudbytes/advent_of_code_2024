def read_input_and_check_levels(input_file: str) -> int:
    safe_count = 0
    with open(input_file, "r") as input_file:
        for level in input_file:
            level_list = [int(num) for num in level.strip().split(" ")]
            if is_level_safe(level_list):
                safe_count += 1
    return safe_count


            

def is_level_safe(level_list: list[int]) -> bool:
    """
    A level list is considered safe if either one is both are true:
       * all increasing or all decreasing
       * any two adjacent levels differ by at least one and most three 
    """

    decreasing = True
    increasing = True
    
    for idx in range(len(level_list) - 1):
        diff = level_list[idx + 1] - level_list[idx]
        
        # Check if the difference is within the range [1, 3]
        if not (1 <= abs(diff) <= 3):
            return False
        
        # Determine if the list is increasing or decreasing
        if diff > 0:
            decreasing = False
        elif diff < 0:
            increasing = False
    return increasing or decreasing



def main() -> None:
    safe_count = read_input_and_check_levels("input.txt")
    print(f"There is a total of {safe_count} safe levels")
    

if __name__ == "__main__":
    main()