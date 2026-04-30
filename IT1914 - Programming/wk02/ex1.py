'''
variable name
- consists of letters, numbers and '_'
- cannot start with number
- cannot use any of the Python reserved

- try to use a meaningful name
- try to use two-words
'''



totalHour = 10.50       # camelCase
total_hour = 10.50      # snake_case
TotalHour = 10.50       # PascalCase

rate = 12.35
pay = total_hour * rate

# print using string modulo operator %
print('Total Hour = %.0f, Hourly Rate = %.1f, Salary = $%.2f' % (total_hour, rate, pay))

# print using string format()
print('Total Hour = {0:.0f}, Hourly Rate = {1:.1f}, Salary = ${2:.2f}'.format(total_hour, rate, pay))

# print using f-string
print(f'Total Hour = {total_hour:.0f}, Hourly Rate = {rate:.1f}, Salary = ${pay:.2f}')