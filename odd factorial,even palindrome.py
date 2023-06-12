def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def is_palindrome(number):
    number_str = str(number)
    reversed_str = number_str[::-1]
    if number_str == reversed_str:
        return True
    else:
        return False

number = int(input("Enter an integer: "))

if number % 2 != 0: 
    fact = factorial(number)
    num_digits = len(str(fact))
    print("Factorial of", number, "is", fact)
    print("Number of digits in the factorial:", num_digits)
else:  
    if is_palindrome(number):
        print(number, "is a palindrome.")
    else:
        print(number, "is not a palindrome.")
