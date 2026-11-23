def minimum(digit, amount):
    temporary = digit[0]

    for numeral in range(1, amount):
        temporary = min(temporary, digit[numeral])

    return temporary

def maximum(digit, amount):
    temporary = digit[0]

    for numeral in range(1, amount):
        temporary = max(temporary, digit[numeral])

    return temporary

numbers = [12, 1234, 45, 60, 1]
size = len(numbers)

print(f"\nTapelo is a boy in Grade 1 who is practicing questions for his Mathematics exam tomorrow.\nHe wants to check if his answers for finding the smallest and biggest number in an array {numbers}.\nThis program will help him to find the solution.\n")
print(f"ANSWERS :-\nMaximum Number : {maximum(numbers, size)}\nMinimum Number : {minimum(numbers, size)}")