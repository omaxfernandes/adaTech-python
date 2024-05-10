numbers = [1, 3, 12, 8, 2]
numbers2 = [1, 2, 3, 4, 5]
print(numbers)
print("")

# append, insert, extend, pop, remove, clear, sort, reverse
print("append, add a item in the end of list") 
numbers.append(5)
print(numbers)
print("")

# Insert
print("insert, add a item in the specific position")
numbers.insert(2, 10)
print(numbers)
print("")

# extend
print("extend, add a list in the end of list")
numbers.extend(numbers2)
print(numbers)
print("")

# pop
print("pop, remove a item in the specific position")
numbers.pop()
print(numbers)
print("")
numbers.pop(2)
print(numbers)
print("")

# Remove
print("remove, remove a item in the list")
numbers.remove(1)
print(numbers)
print("")

#  count
print("count, count how many times a item in the list")
print(numbers.count(2))
print("")

# index 
print("index, find the position of a item in the list", numbers.index(12))
print("")

#  sort
print("sort, sort the list")
numbers.sort()
print(numbers)
numbers.sort(reverse=True)
print(numbers)


