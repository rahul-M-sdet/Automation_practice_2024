def extract_digit(s1):
    return [int(char) for char in s1 if char.isdigit()]


s1 = "AWe12345sdr"
digits = extract_digit(s1)
print(digits)
