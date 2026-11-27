def secondest(digit, length):
 
    largest = second = -2147483648
    for numeral in range(length):
        if (digit[numeral] > largest):
            
            second = largest
            largest = digit[numeral]
            
        elif (digit[numeral] > second and digit[numeral] != largest):
            second = digit[numeral]
        
 
    print(f"Second Largest : {second}")
 
number = [1, 2, 3, 4, 5, 6, 7, 8, 9]
size = len(number)

secondest(number, size)