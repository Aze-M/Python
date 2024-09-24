def main():
    numbers = [3, 1, 5, 7, 9, 2, 8, 6]
    largest = find_largest(numbers)  # This function is missing
    print(f"The largest number is: {largest}")

def find_largest(in_num:list[int]) -> int:
    in_num.sort()
    return in_num.pop()

if __name__ == "__main__":
    main()
