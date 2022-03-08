# from ctypes import sizeof


# myvar = "Say it ain't so"
# print(myvar)

# myvar2 = "spam & eggs"

# spam= "spam"
# eggs= "eggs"

# print(myvar2[0:3])

# spam_and_eggs = spam + " & " + eggs

# print (spam_and_eggs)

# print(len(spam_and_eggs))

# print(spam_and_eggs.upper())

# praise = "Good Doggie"

# count = praise.upper().count("G")

# print ("Count: ", count)

# town = input("Enter the town of your city: ")

fullName = input("Enter a full name: ")
n = fullName.findr(" ")
print("Last name: ", fullName[n+1:])
print("First name: ", fullName[:n])