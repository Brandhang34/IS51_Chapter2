num1 = 1
num2 = 10
num3 = 1000
sum_of_all_numbers = num1 + num2 + num3

print("Sum is {0:n}".format(sum_of_all_numbers))

list_of_numbers = [1, 10, 1000]
list_of_words = ["abc", "cde", "fgh"]

print("sum is:  ", sum(list_of_numbers))
print("max value is: ", max(list_of_numbers))
print("min value is: ", min(list_of_numbers))
print("num of occurence: ", list_of_numbers.count(2))
print("length of list: ", len(list_of_numbers))
print("index of value 10 is: ", list_of_numbers.index(10))
print("reversed list: ", list_of_words.reverse())

list_of_numbers2 = [3, 100, 5]
print(list_of_numbers2)

list_of_numbers3 = list_of_numbers + list_of_numbers2
print(list_of_numbers3)