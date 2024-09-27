# average.py
numbers = input("Enter numbers separated by spaces: ")
num_list = list(map(float, numbers.split()))
average = sum(num_list) / len(num_list)
print(f"The average is: {average}")
