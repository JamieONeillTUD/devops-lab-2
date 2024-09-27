# average.py
numbers = input("Enter numbers separated by spaces: ")
num_list = list(map(float, numbers.split()))
largest = max(num_list)
smallest = min(num_list)
average = sum(num_list) / len(num_list)
print(f"The average is: {average}")
print(f"The largest is: {largest}")
print(f"The smallest is: {smallest}")
