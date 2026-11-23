def mean(numbers, amount):
    total = 0

    for numeral in range(0, amount):
        total += numbers[numeral]

    return float(total / amount)

def median(numbers, amount):
    sorted(numbers)

    if amount % 2 != 0:
        return float(numbers(amount / 2))

    return float((numbers[int((amount - 1) / 2)] + numbers[int(amount / 2)])/2.0)

digits = [2, 5, 1, 6, 3, 8, 9, 10, 4, 7]
size = len(digits)

print(f"\nAmaya is a girl in Grade 6 who is practicing questions for her Mathematics exam tomorrow.\nShe wants to check if her answers for finding the mean and median of an array {digits}.\nThis program will help her to find the solution.\n")

print(f"ANSWERS :-\nMean : {mean(digits, size)}\nMedian : {median(digits, size)}\n")