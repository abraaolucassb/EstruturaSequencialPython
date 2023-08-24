"""4. Make a Program that asks for the 4 bimonthly grades and shows the average.
"""

print('*AVERAGE PROGRAM*')

grade_one = float(input('Enter the grade 1: '))
grade_two = float(input('Enter the grade 2: '))
grade_three = float(input('Enter the grade 3: '))
grade_four = float(input('Enter the grade 4: '))

sum_operation = grade_one + grade_two + grade_three + grade_four

average_operation = sum_operation / 4

print(f'The average is: {average_operation}.')
