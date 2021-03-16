friends = ["Aqila","Anila","Neha", "Rizvee","Mashfiq"]
numbers = [4,5,6,12,65,78,98,35,456]

print(friends)
# add list with list
friends.extend(numbers)
print(friends)
# add one by one value
friends.append("Creed")
numbers.append(654456)
# add at a particular position
friends.insert(1, "kelly") #index position, "value"
# remove a single value
friends.remove("Creed")
# Pops the last element
friends.pop()
# Search:
friends.index("Anila") #returns index value
# Count the number of similar elements:
friends.count("Anila")
# Sorts the list:
friends.sort()
numbers.sort()
# Reverse the list
numbers.reverse()
# Copy a list
friends2 = friends.copy()
# remove the whole list
friends.clear()