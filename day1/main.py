from utils import read_input, get_ordered_lists, calculate_total_distance

def main() -> None:
    left, right= read_input("input.txt")
    ordered_left, ordered_right = get_ordered_lists(left, right)

    tot_distance:int = calculate_total_distance(ordered_left, ordered_right)
    print(f"**** total distance calculated: {tot_distance}")

    

if __name__ == "__main__":
    main()