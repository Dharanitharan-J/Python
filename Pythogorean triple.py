def check_pythagorean_triple(n1, n2, n3):
    if n1**2 + n2**2 == n3**2:
        return 1
    else:
        return 0

def main():
    n1 = int(input("Enter the first number: "))
    n2 = int(input("Enter the second number: "))
    n3 = int(input("Enter the third number: "))

    if n1 < n2 < n3:
        result = check_pythagorean_triple(n1, n2, n3)
        print(result)
    else:
        print("The numbers should be in increasing order.")

if __name__ == '__main__':
    main()
