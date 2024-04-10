numbers = []

while True:
    user_input = input("Enter a number (or 'done' to finish): ")
    if user_input.lower() == "done":
        break
    numbers.append(float(user_input))

count = len(numbers)
total_sum = sum(numbers)
average = total_sum / count

print("Count:", count)
print("Sum:", total_sum)
print("Average:", average)
