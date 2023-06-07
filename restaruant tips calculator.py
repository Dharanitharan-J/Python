def calculate_tip(food_rating, service_rating, ambience_rating, bill_amount):
    if food_rating >= 4 and service_rating >= 4 and ambience_rating >= 4:
        tip_percentage = 0.1
    elif service_rating >= 3 and ambience_rating >= 3:
        tip_percentage = 0.05
    else:
        tip_percentage = 0.01
    
    tip_amount = tip_percentage * bill_amount
    return tip_amount


# Read input ratings and bill amount
food_rating = int(input("Food Rating (1-5): "))
service_rating = int(input("Service Rating (1-5): "))
ambience_rating = int(input("Ambience Rating (1-5): "))
bill_amount = float(input("Bill Amount: "))

# Calculate the tip amount
tip_amount = calculate_tip(food_rating, service_rating, ambience_rating, bill_amount)

# Print the tip amount
print(f"Tip Amount: ${tip_amount:.2f}")




