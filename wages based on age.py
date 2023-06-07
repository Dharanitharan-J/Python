def calculate_wages(age, gender):
    if age >= 18 and age < 30:
        if gender == 'M':
            wages = 700
        elif gender == 'F':
            wages = 750
    elif age >= 30 and age <= 40:
        if gender == 'M' or gender == 'F':
            wages = 800
    else:
        return None
    
    return wages

def calculate_total_payment(wages, days):
    if wages is not None:
        total_payment = wages * days
        return total_payment
    else:
        return None

def main():
    name = input("Enter the name: ")
    age = int(input("Enter the age: "))
    gender = input("Enter the gender (M or F): ")
    days = int(input("Enter the number of days: "))

    wages = calculate_wages(age, gender)
    total_payment = calculate_total_payment(wages, days)

    if total_payment is not None:
        print(f"Name: {name}")
        print(f"Wages per day: Rs {wages}")
        print(f"Total amount to be paid: Rs {total_payment}")
    else:
        print("Invalid age or gender.")

if __name__ == '__main__':
    main()
