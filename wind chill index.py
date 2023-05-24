t=int(input("Enter the temperature"))
w=int(input("Enter the windspeed"))
wind_chill_index=13.12+0.6216*t-11.37*w**0.16+0.395*t*w**0.16
print("The wind chill index is",wind_chill_index)
