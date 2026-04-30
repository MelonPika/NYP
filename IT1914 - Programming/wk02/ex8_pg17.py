str1 = input("Enter string 1 (< 5 chars) : ")
str2 = input("Enter string 2 (< 5 chars) : ")


print(f"\n{str1}\t{str2}\n{str2}\t{str1}")
print(f"\n{str1:<30}{str2:>10}\n{str2:^30}{str1:10}")
# string format specification
# {var:<10.2f}     => alignment: < > ^
#       => number of spaces reserved for the value
#       => .2 is the number of decimal places
#       => f/d/s is the data type to be printed

# escape sequence starts with a '\'
# '\n'  -> newline
# '\t'  -> tab
# '\\'  -> '\'
# '\r'  -> carriage return
# '\"'  -> '"'