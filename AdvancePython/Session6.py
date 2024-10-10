#lambda
numbers = [1, 2, 3, 4, 5]
# استفاده از lambda برای محاسبه مربع اعداد
squares = list(map(lambda x: x ** 2, numbers))
print(squares)  # خروجی: [1, 4, 9, 16, 25]


#map
# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# List of Celsius temperatures
celsius_temps = [0, 20, 30, 40]

# Using map to apply the conversion function to each element
fahrenheit_temps = list(map(celsius_to_fahrenheit, celsius_temps))

print(fahrenheit_temps)


numbers = [1, 2, 3, 4, 5]
# تعریف یک تابع lambda که به هر عدد 2 اضافه کند
result = list(map(lambda x: x + 2, numbers))
print(result)  # خروجی: [3, 4, 5, 6, 7]

#zip
# Two lists
names = ["Alice", "Bob", "Charlie"]
ages = [24, 30, 28]

# Using zip to combine names and ages
paired_data = list(zip(names, ages))

print(paired_data)


numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
# هر عدد با یک حرف جفت می‌شود
result = list(zip(numbers, letters))
print(result)  # خروجی: [(1, 'a'), (2, 'b'), (3, 'c')]

list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Using map with zip and lambda to multiply corresponding elements
products = list(map(lambda x: x[0] * x[1], zip(list1, list2)))

print(products)

#filter
# List of numbers
numbers = [4, 12, 7, 15, 9, 22, 5]

# Function to check if a number is greater than 10
def greater_than_ten(num):
    return num > 10

# Using filter to get numbers greater than 10
filtered_numbers = list(filter(greater_than_ten, numbers))

print(filtered_numbers)


numbers = [1, 2, 3, 4, 5, 6]
# فیلتر کردن اعداد فرد
result = list(filter(lambda x: x % 2 != 0, numbers))
print(result)  # خروجی: [1, 3, 5]

#mergh map&filter
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# فیلتر کردن اعداد زوج و سپس محاسبه مربع آن‌ها
result = list(map(lambda x: x ** 2, filter(lambda x: x % 2 == 0, numbers)))
print(result)  # خروجی: [4, 16, 36, 64]
