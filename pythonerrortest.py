# broken_script.py

import math

def compute_area(radius)
    # SyntaxError: missing colon
    return math.pi * radius**2

def calculate_average(numbers):
    total = sum(numbers)
    count = len(numbers)
    average = total / coun  #  NameError: typo “coun” instead of “count”
    # Missing return statement

def main():
    nums = [10, 20, 30]
    #  calculate_average returns None, so this will print “Average: None”
    print("Average:", calculate_average(nums))
    # compute_area won’t run because of the syntax error above
    print("Area for radius 5:", compute_area(5))

if __name__ == "__main__":
    main()
