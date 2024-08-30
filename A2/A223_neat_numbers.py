for i in range(101,1000):
    # Finds sum of the current number's digits.
    sum_of_digits = sum(int(digit) for digit in str(i))
    # Checks if the current number is 'neat'. A number is 'neat' if
    # it is divisible by the sum of its digits.
    if i%sum_of_digits == 0:
        print(i)