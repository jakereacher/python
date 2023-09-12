n = int(input("Enter a number:"))
sum_even_digits = 0

while n > 0:
    digit = n % 10
    if digit % 2 == 0:
        sum_even_digits += digit
    n = n // 10
    print(digit)
    print(n)
if sum_even_digits > 0:
    print("Sum of even digits:", sum_even_digits)
else:
    print("No even digits in the number.")
