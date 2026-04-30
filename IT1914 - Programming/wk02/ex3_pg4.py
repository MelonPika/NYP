numS = 2 #number of small room
numB = 3 #number of Big room

sTables = input('Enter number of tables in small room: ')
bTables = input('Enter number of tables in big room: ')

totalSmall = numS * int(sTables)
totalBig = numB * int(bTables)
totalTable = totalSmall + totalBig

print(f"Total Tables = {totalTable}" )

# a = 1
# b = 3

# a, b = 1, 3