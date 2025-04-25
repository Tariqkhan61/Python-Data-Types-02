# This Topic will cover all the data Types in Python
# DATA TYPES
# 1) Integer
num_int:int = 10
print(num_int, type(num_int), num_int)

# 2) Float
num_float:float = 64.5
print(num_float, type(num_float), num_float)

# 3) Complex Number
num_complex: complex = 3 + 7j
print(num_complex, type(num_complex), num_complex)

# 4) Accessing Real and Imaginary Parts
z = 3 + 4j
print("Real Part:",z.real)
print("Imaginary Part:",z.imag)

# 5) Boolean
is_bool: bool = True
print(is_bool, type(is_bool), is_bool)
my_bool: bool = False
print(my_bool, type(my_bool), my_bool)

# 6) Sequence Types
# a) String. A sequence of characters enclosed in quotes.
double_quotes: str = "Hello World"
print(double_quotes, type(double_quotes))
single_quotes: str = 'I am Tariq'
print(single_quotes, type(single_quotes))
multi_quotes: str = ''' I am a student of Computer Science. I am learning Python. '''
print(multi_quotes, type(multi_quotes))
my_string: str = ''' I'm studying at Governor's University of Information Technology.'''
print(my_string, type(my_string))

# b) List. A mutable sequence of elements.
my_list: list = [1,2,3,4]
print(my_list, type(my_list))
my_list_1: int =[1,2,3, "Java", 4.5, True]
print(my_list_1)

# Tuple
my_tuple: tuple = (1,2,3,4)
print(my_tuple, type(my_tuple))

# C) Range. A sequence of numbers.
my_range: range = range(1, 10, 2)  # Creates a range from 1 to 10 with a step of 2
print(type(my_range), f"my_range.step = {my_range.step}")  # Corrected print statement

for i in my_range:  # Iterate directly over my_range
    print(i)  # Print each value in the range

# Range of even numbers
# A simple example using range to generate even numbers
even_numbers: range = range(2, 14, 2)  # Starts at 2, ends before 12, steps by 2
print("Even numbers in the range:")
for num in even_numbers:
    print(num)

# 4) Set Types
# a) Set. An unordered collection of unique elements.
my_set: set = {1,2,33,4,4,5}
print(type(my_set), my_set)

# b) Frozenset. An immutable version of a set.
frozen_set = frozenset([11,2,3,4,4,5])
print(type(frozen_set),"frozen_set =", frozen_set)

# 5) Mapping Types
# a) Dictionary. A collection of key-value pairs.
my_dict:dict = {"name":"Tariq", "age": 55, "is_student": True, "courses": ["Python", "Java Script"]}
print(type(my_dict), my_dict)

# 8) Binary Types
# a) Bytes. Immutable sequence of bytes.
bytes_data: bytes = b"Hello"
print(type(bytes_data), bytes_data)

