# print("Hello", "World!", sep= ", ")

# print("Hello", end= " ")
# print("World!")

# print("a\tb\tc")
# print("a\tb\tc\td\te\tf")

# print("\\Hello World!\\")

# print("0123456789012345678901234567")
# print("Rank".ljust(5), "Player".ljust(20), "HR".rjust(3), sep="")
# print('1'.center(5), "Barry Bonds".ljust(20), "762".rjust(3), sep="")
# print('2'.center(5), "Hank Aaron".ljust(20), "755".rjust(3), sep="")
# print('3'.center(5), "Babe Ruth".ljust(20), "714".rjust(3), sep="")

# print("There are {0}% probability that the stock market will crash tomorrow and {1}% probability that it will rally.".format(10, 50))

# print("0123456789012345678901234567")
# print("{0:^5s} {1:<20s} {2:>3s}".format("Rank", "Player", "HR"))
# print("{0:^5n} {1:<20s} {2:>3n}".format(1, "Barry Bonds", 762))
# print("{0:^5n} {1:<20s} {2:>3n}".format(2, "Hank Aaron", 755))
# print("{0:^5n} {1:<20s} {2:>3n}".format(3, "Babe Ruth", 714))

print("The area of {0:s} is {1:,d} square miles.".format("Texas", 268820))
str1 = "The population of {0:s} is {1:2%} of the U.S. population"
print(str1.format("Texas", 26448000 / 309000000))

str2 = "Of the U.S. population, {1:2%} resides in {0:s}"
print(str2.format("Texas", 26448000 / 309000000))
