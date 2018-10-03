# define the lists
friends = [
	["Pieter", " "],
	["Jantje", " "],
	["Greta", " "]
]

# length of the name
for friend in friends:
	print(friend[0])
	print(len(friend[0]))


# create a for loop
for friend in friends:
	# ask each person personally what their favorite snack is and add to multi-list
	friend[1] = input("What is your favourite snack " + friend[0] + "? ")
	# print the favorite snack of each person as a response
	print(friend[0] + " your favourite snack is " + friend[1])