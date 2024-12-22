# multiplication_table.py

# Prompt the user to input a number
number = int(input("Enter a number to see its multiplication table: "))

# Loop through numbers 1 to 10 and calculate the multiples
for i in range(1, 11):
    # Use the required format for the print statement
    print(f"{number} * {i} = {number * i}")
