def calculate_bonus(salary, years_of_service):
    if years_of_service > 10:
        bonus_percentage = 10
    elif years_of_service > 6:
        bonus_percentage = 8
    else:
        bonus_percentage = 5
    
    bonus = salary * (bonus_percentage / 100)
    return bonus

def main():
    salary = float(input("Enter the salary: "))
    years_of_service = int(input("Enter the years of service: "))

    bonus = calculate_bonus(salary, years_of_service)

    print(f"Bonus: {bonus}")

if __name__ == '__main__':
    main()
