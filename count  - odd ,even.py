start = int(input("Enter the starting number: "))
end = int(input("Enter the ending number: "))

count_even = 0
count_odd = 0

for num in range(start, end + 1):
    if num % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

print("Even:", count_even)
print("Odd:", count_odd)
