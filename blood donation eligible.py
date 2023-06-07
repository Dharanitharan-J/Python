def check_eligibility(name, age, weight):
    if age > 18 and weight > 40:
        return 1
    else:
        return 0

def main():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    weight = int(input("Enter your weight: "))

    result = check_eligibility(name, age, weight)

    print(result)

if __name__ == '__main__':
    main()
