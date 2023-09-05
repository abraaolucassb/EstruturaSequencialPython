"""8. Create a program that asks you how much you earn per hour and the number of hours worked in the month. Calculate and
display your total salary for the month."""

hour = float(input('How much do you earn per hour? '))
hours_worked = float(input('How many hours did you work in the month? '))

salary = hour * hours_worked

print(f'Your total salary is: {salary}.')
