def find_missing_number(l1):
    n = len(l1) + 1  # including missing number
    Expected_result = n * (n + 1) // 2
    Actual_result = sum(l1)
    missing_number = Expected_result - Actual_result
    return missing_number


l1 = [1, 2, 3, 5, 6]
missing = find_missing_number(l1)
print("Missing number: ", missing)
