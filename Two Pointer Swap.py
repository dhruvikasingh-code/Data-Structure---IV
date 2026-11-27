def reversing(digit):
    arraying, numeral, numbering = list(range(1, digit + 1)), 0, digit - 1

    while numeral < numbering:
        arraying[numeral], arraying[numbering] = arraying[numbering], arraying[numeral]

        numeral += 1 ; numbering -= 1

    return arraying

print("\nLacie is sleeping in her class about how to swap an array without using built - in functions or slicing. When preparing for her exams, she revised only the built - in function. In the exam paper, she was told to reverse an array manually only. Lacie is panicking because this is her final exam. Can you help her?")

number = int(input("\nEnter the size of the array : "))

print(f"RESULT : {reversing(number)}")