def calculate_final_charge(age, fare):
    if age >= 60:
        final_charge = fare - (fare * 0.2)
        return final_charge
    else:
        return fare

def main():
    fare = 1020
    age = int(input("Enter your age: "))
    
    final_charge = calculate_final_charge(age, fare)
    
    print(f"Final traveling charge: Rs {final_charge}")

if __name__ == '__main__':
    main()
